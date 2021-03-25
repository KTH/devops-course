const core = require('@actions/core');
const github = require('@actions/github');


const kthIDs = [
  'andnil5',
  'kalpet',
  'johanbes',
  'KallePettersson'
];

try {
  // Get the JSON webhook payload for the event that triggered the workflow
  const payload = JSON.stringify(github.context, undefined, 2)
  // console.log(github.context);
  console.log(`The event payload: ${payload}`);

  if (!kthIDs.includes(github.context.payload.pull_request.user.login))
    throw Error('The user is not registered in the course.');
} catch (error) {
  core.setFailed(error.message);
}