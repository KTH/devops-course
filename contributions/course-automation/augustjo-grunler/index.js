const core = require('@actions/core');
const github = require('@actions/github');
var atob = require('atob');


async function main() {
  try {
    // Constants
    const token = core.getInput('repo-token')
    const minimalWordCountLimit = core.getInput('minimal-wordcount')
    const remarkableWordCountLimit = core.getInput('remarkable-wordcount')
    const deadline = new Date(core.getInput('deadline'))
    const octokit = github.getOctokit(token)
    const repoName = github.context.repo.repo
    const owner = github.context.payload.repository.owner.login
    const branch = github.context.payload.pull_request.head.ref


    var issue_number = github.context.payload.pull_request._links.issue.href.split("/")
    issue_number = issue_number[issue_number.length-1]
    let timeOfSubmission = github.context.payload.pull_request.head.repo.pushed_at
    timeOfSubmission = new Date(timeOfSubmission)

    // get changed files from pullrequest
    var files = await getChangedfiles(owner, repoName, issue_number, octokit)
    //Find README
    files = files.filter(file => file.filename.includes('README.md'))
    files = files.filter(file => file.filename.includes('feedback'))

    //Get the README's directory
    let dir = files[0].filename.split('/')
    const reducer = (accumulator, word) => accumulator + "/" + word
    dir.pop()
    dir = dir.reduce(reducer)
  
    // Extract The readme file with the feedback from the correct directory
    var file = await getReadme(octokit,owner,repoName,dir,branch)
    const path = file.path
    var markdown = atob(file.content)

    //Calculate feedback word count
    var wordCount = getMDwordCount(markdown)
    var wordCountReached = getWordCountVerdict(wordCount,minimalWordCountLimit,remarkableWordCountLimit)

  
    //build comment body
    var comment = createCommentBody(file.name, path, wordCount, wordCountReached, timeOfSubmission, deadline)
    buildAndPostComment(issue_number,comment, octokit)

  } catch (error) {
    core.setFailed(error.message);
  } 
}

function getMDwordCount(string) {
  str = string.replace(/([#\*>\+|/_@±/\[\]\\{}<±\-`]+)/g,"");
  str = str.replace(/(\s)+/g," ");
  str = str.trim();
  return str.split(" ").length;
}

// this function gets all the changed files in a pullrequest
var getChangedfiles = async function(owner,repo,issue_number,octokit) {
  return new Promise((resolve,reject) => {octokit.request('GET /repos/{owner}/{repo}/pulls/{pull_number}/files', {
    owner: owner,
    repo: repo,
    pull_number: issue_number
  }).then(files => {
    resolve(files.data)
  }).catch(err =>{
    console.log(err)
    reject(err)
  })
})
}

// this function fetches a readme in a specific directory on github
var getReadme = async function(octokit, owner, repo, dir, callingBranch='master') {
  return new Promise((resolve,reject) => {octokit.request('GET /repos/{owner}/{repo}/readme/{dir}', {
    owner: owner,
    repo: repo,
    dir: dir,
    ref: callingBranch
  }).then(file =>{ 
    x = atob(file.data.content)
    resolve(file.data)
  }).catch(err => {
    console.log(err)
  }) 
  })
 
}

function checkDeadline(deadline, timeOfSubmission) {
  if (deadline > timeOfSubmission) {
    return true
  } else {
    return false
  }
}

function getWordCountVerdict(wordCount, acceptableLimit, remarkableLimit) {
  let wc = parseInt(wordCount);
  let verdict = (wc < acceptableLimit) ? 'no': (wc >= remarkableLimit ? 'yes, remarkable!' : 'yes');
  return verdict;
}

function createCommentBody(filename, path, wc, verdict, timeOfSubmission, deadline ) {
  let comment = 'Checking basic feedback requirements. \n';
  let fileString = `**File checked**: ${filename} (${path}). \n`;
  fileString += ` **Path:** ${path} \n `;
  let wordCountString = `**Passes word limit**: ${verdict} (${wc} words). \n`;
  //check time of submission
  let timeApproved = checkDeadline(deadline,timeOfSubmission)
  let timeCheckString = timeApproved? `The feedback was submitted in time` : `The feedback was submitted after the deadline`
  timeCheckString += ` (submitted at: ${timeOfSubmission.toString()}). \n`;
  comment = comment + fileString + wordCountString +  timeCheckString;
  return comment;
}

async function buildAndPostComment(issue_number, message, octokit) {
  const comment = await octokit.issues.createComment({
    owner: github.context.repo.owner,
    repo: github.context.repo.repo,
    issue_number,
    body: message,
  });
}

main()
