const core = require('@actions/core');
const github = require('@actions/github');


async function doSomething() {
  try {
    // `who-to-greet` input defined in action metadata file
    const token = core.getInput('repo-token');
    const octokit = github.getOctokit(token);
    // Get the JSON webhook payload for the event that triggered the workflow
    const payload = JSON.stringify(github.context.payload, undefined, 2);
    console.log(`The event payload: ${payload}`);
    const owner = github.context.payload.repository.login;
    console.log(`The owner of the repo is ${owner}`)
    const pathOfFiles = '/contributions/course-automation/augustjo-grunler/*.md'

    const repoName = github.context.payload.repository.full_name;
    console.log(`Pull request to: ${repoName}`)

    getChangedFiles(octokit,owner,repoName,pathOfFiles)

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

function getChangedFiles(octokit, owner, repo, path, callingBranch='master') {
  //TODO
  octokit.rest.repos.getContents({owner, repo, path}).then(file => {
    console.log(file)
  });
  //return files;
}

doSomething()

