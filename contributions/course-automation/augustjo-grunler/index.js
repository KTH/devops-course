const core = require('@actions/core');
const github = require('@actions/github');
const base64 = require('base-64');
const utf8 = require('utf8');
var atob = require('atob');

async function doSomething() {
  try {
    // `who-to-greet` input defined in action metadata file
    const token = core.getInput('repo-token');
    const octokit = github.getOctokit(token);
    // Get the JSON webhook payload for the event that triggered the workflow
    const payload = JSON.stringify(github.context.payload, undefined, 2);
    console.log(`The event payload: ${payload}`);
    const owner = github.context.payload.repository.owner.login;
    console.log(`The owner of the repo is ${owner}`)
    const dir = '/contributions/course-automation/augustjo-grunler'

    const repoName = github.context.repo.repo
    console.log(`Pull request to: ${repoName}`)

    getChangedFiles(octokit,owner,repoName,dir)

    changed_files = github.context.payload.pull_request.changed_files;
    core.setOutput('changed_files', changed_files); 
  } catch (error) {
    core.setFailed(error.message);
  } 
}

function calculateWords(fileName) {
//check file type
//TODO
}

async function getChangedFiles(octokit, owner, repo, dir, callingBranch='master') {
  //TODO
  /*
  octokit.rest.repos.getContents({owner, repo, path}).then(file => {
    console.log(file)
  });
  */
  octokit.request('GET /repos/{owner}/{repo}/readme/{dir}', {
    owner: owner,
    repo: repo,
    dir: dir
  }).then(data =>{ 
    console.log(data.data.content)
    x = atob(data.data.content)
    console.log(x)
  }).catch(err => {
    console.log(err)
  })
  //return files;
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
async function buildAndPostComment(issue_number, message) {

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
doSomething()
