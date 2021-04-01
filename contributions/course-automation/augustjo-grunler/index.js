const core = require('@actions/core');
const github = require('@actions/github');


async function doSomething() {
  try {
    // `who-to-greet` input defined in action metadata file
    const token = core.getInput('repo-token');
    const octokit = github.getOctokit(token);
    const repoName = github.context.payload.repository.full_name;
    console.log(`Pull request to: ${repoName}`)
    const time = (new Date()).toTimeString();
    changed_files = github.payload.pull_request.changed_files;
    core.setOutput("Number of changed files: ", changed_files);
    // Get the JSON webhook payload for the event that triggered the workflow
    const payload = JSON.stringify(github.context.payload, undefined, 2)
    console.log(`The event payload: ${payload}`);
  } catch (error) {
    core.setFailed(error.message);
  } 
}

function calculateWords(fileName) {
//check file type
//TODO
}

function getChangedFiles(owner, repo, path, callingBranch='master') {
  //TODO
  //const files = octokit.repos.getContents({owner, repo, path, branch});
  //return files;
}

doSomething()

