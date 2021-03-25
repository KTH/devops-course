const core = require('@actions/core');
const github = require('@actions/github');

const kthIDs = [
  'andnil5',
  'kalpet',
  'johanbes',
];

try {
  // Get the JSON webhook payload for the event that triggered the workflow
  const payload = JSON.stringify(github.context.payload, undefined, 2)
  console.log(`The event payload: ${payload}`);
  // throw Error('');
} catch (error) {
  core.setFailed(error.message);
}