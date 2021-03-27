const core = require('@actions/core');
const { context, getOctokit } = require('@actions/github');
const Parser = require('./utils/parser');

try {
  console.log('Retreving valid kthIDs');
  const kthIDs = Parser.parseKTHIdsFile();

  console.log('Parsing PR payload and repo data.');
  const contextData = Parser.parseContext(context);

  // Use compareCommits in order to find where README file is located,
  // want to check members in readme in case a non-kths github is used
  getOctokit(core.getInput('token')).repos.compareCommits(contextData)
    .then(response => {
      if (response.status !== 200) throw Error('Could not fetch changed files!');

      console.log('Finding README file location');
      const readme = Parser.parseReadmePath(response);
      console.log('README File location:', readme, '\n');
      const ids = Parser.parseKTHEmail(readme);
      console.log('RESULT:');
      console.log('\tKTH-ids found in README:\n\t', ids);
      const validIDs = ids.filter(id => kthIDs.includes(id));
      const invalidIDs = ids.filter(id => !validIDs.includes(id));
      console.log('\tValid KTH-ids found in README:\n', '\t', validIDs, '\n');
      if (invalidIDs.length > 0) throw Error('\tInvalid KTH-ids in README:', '\t', invalidIDs, '\n');
  }).catch(error => {
    core.setFailed(error.message);
  });
} catch (error) {
  core.setFailed(error.message);
}