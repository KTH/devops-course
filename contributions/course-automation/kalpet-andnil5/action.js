const core = require('@actions/core');
import { context, getOctokit } from '@actions/github'


const kthIDs = [
  'andnil5',
  'kalpet',
  'johanbes',
  'KallePettersson'
];

try {
  // Get the JSON webhook payload for the event that triggered the workflow
  const payload = JSON.stringify(context, undefined, 2)
  // console.log(context);
  // console.log(`The event payload: ${payload}`);
  // const changedFiles = core.getInput("changed-files");
  // console.log(changedFiles)

  // const client = new GitHub(core.getInput('token', {required: true}))
  const client = getOctokit(core.getInput('token'));

  const base = context.payload.pull_request?.base?.sha
  const head = context.payload.pull_request?.head?.sha

  if (!base || !head) {
    core.setFailed(
      `The base and head commits are missing from the payload for this ${context.eventName} event. ` +
        "Please submit an issue on this action's GitHub repo."
    );
  }

  client.repos.compareCommits({
    base,
    head,
    owner: context.repo.owner,
    repo: context.repo.repo
  }).then(response => {
    if (response.status !== 200) throw Error('Could not fetch changed files!');
    const files = response.data.files;

    const filteredFiles = files
      .map(file => file.filename.split('/'))
      .filter(file => file.length > 3 && file[0] === 'contributions' );
    if (filteredFiles.length < 1) throw Error('Could not find path to README.md');
    const readme = [...filteredFiles[0].splice(0,3), 'README.md'].join('/')
    console.log(readme)
    console.log(filteredFiles);
    if (!kthIDs.includes(context.payload.pull_request.user.login))
    throw Error('The user is not registered in the course.');
  }).catch(error => {
    core.setFailed(error.message);
  });

} catch (error) {
  core.setFailed(error.message);
}