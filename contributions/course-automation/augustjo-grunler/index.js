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

    const repoName = github.context.payload.repository.full_name;
    console.log(`Pull request to: ${repoName}`)

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

function getChangedFiles(owner, repo, path, callingBranch='master') {
  //TODO
  //const files = octokit.repos.getContents({owner, repo, path, branch});
  //return files;
}

doSomething()

