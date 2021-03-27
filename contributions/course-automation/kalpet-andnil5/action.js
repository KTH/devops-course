const core = require('@actions/core');
const { context, getOctokit } = require('@actions/github');
const { ROOT } = require('./config');
const Parser = require('./parser');


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
      // Find path to README file
      const files = response.data.files;
      const filteredFiles = files.map(file => file.filename.split('/'))
        .filter(file => file.length > 3 && file[0] === 'contributions' );
      if (filteredFiles.length < 1) throw Error('Could not find path to README.md');

      const readme = [ROOT, ...filteredFiles[0].splice(0,3), 'README.md'].join('/');
      console.log('README File location:', readme);
      const ids = Parser.parseKTHEmail(readme);
      console.log('KthIDs found in README:\n', ids, '\n');
      const validIDs = ids.filter(id => kthIDs.includes(id));
      const invalidIDs = ids.filter(id => !validIDs.includes(id));
      console.log('Valid kthIDs found:\n', validIDs, '\n');
      if (invalidIDs.length > 0) throw Error('Invalid KTHids in README file:', invalidIDs, '\n');
  }).catch(error => {
    core.setFailed(error.message);
  });
} catch (error) {
  core.setFailed(error.message);
}