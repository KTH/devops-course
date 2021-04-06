const core = require('@actions/core');
const github = require('@actions/github');
var atob = require('atob');

async function main() {
  try {
    // `who-to-greet` input defined in action metadata file
    const token = core.getInput('repo-token');
    const minimalWordCountLimit = core.getInput('minimal-wordcount')
    const remarkableWordCountLimit = core.getInput('remarkable-wordcount')
    const octokit = github.getOctokit(token);
    // Get the JSON webhook payload for the event that triggered the workflow
    const payload = JSON.stringify(github.context.payload, undefined, 2);
    console.log(`The event payload: ${payload}`);
    const owner = github.context.payload.repository.owner.login;
    console.log(`The owner of the repo is ${owner}`)
    const dir = '/contributions/course-automation/augustjo-grunler'

    var issue_number = github.context.payload.pull_request._links.issue.href.split("/")
    issue_number = issue_number[issue_number.length-1]
    
    const repoName = github.context.repo.repo
    console.log(`Pull request to: ${repoName}`)
    // Extract The file with the feedback
    var file = await getReadme(octokit,owner,repoName,dir)
    const path = file.path
    console.log(`path is: ${path}`)
    core.setOutput("readme_path", path)
    var rawText = atob(file.content)
    var wordCount = getMDwordCount(rawText)
    var wordCountReached = getWordCountVerdict(wordCount,minimalWordCountLimit,remarkableWordCountLimit)

    //build comment body
    var comment = createCommentBody(file.name, wordCount, wordCountReached)
    buildAndPostComment(issue_number,comment, octokit)

    changed_files = github.context.payload.pull_request.changed_files;
    core.setOutput('changed_files', changed_files); 
  } catch (error) {
    core.setFailed(error.message);
  } 
}

function getMDwordCount(string) {
  str = string.replace(/([#*>+|/_@±/\[\]\\{}<-`]+)/g,"");
  str = str.replace(/(\s)+/g," ");
  return str.split(" ").length;
}

var getReadme = function(octokit, owner, repo, dir, callingBranch='master') {
  return new Promise((resolve,reject) => {octokit.request('GET /repos/{owner}/{repo}/readme/{dir}', {
    owner: owner,
    repo: repo,
    dir: dir
  }).then(file =>{ 
    x = atob(file.data.content)
    resolve(file.data)
  }).catch(err => {
    console.log(err)
  }) 
  })
 
}

function getWordCountVerdict(wordCount, acceptableLimit, remarkableLimit) {
  let wc = parseInt(wordCount);
  let verdict = (wc < acceptableLimit) ? 'no': (wc >= remarkableLimit ? 'yes, remarkable' : 'yes');
  return verdict;
}

//TODO: add time aspect
function createCommentBody(filename, wc, verdict ) {
  let comment = '';
  let fileString = `File checked: ${filename}. \n`;
  let wordCountString = `Substantiated: ${verdict} (${wc} words) \n`;
  comment = comment + fileString + wordCountString;
  return comment;
}

//TODO: issue number
async function buildAndPostComment(issue_number, message, octokit) {
  const comment = await octokit.issues.createComment({
    owner: github.context.repo.owner,
    repo: github.context.repo.repo,
    issue_number,
    body: message,
  });
}
/*
let words = '600'
let verdict = getWordCountVerdict(words, '500', "1000");
let message = createCommentBody('README.md', words, verdict)
console.log(message);
*/
main()
