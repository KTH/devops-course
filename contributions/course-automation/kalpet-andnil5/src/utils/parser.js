const fs = require('fs');
const { KTH_IDS_FILE } = require('../config/config');

module.exports = {
  /**
   * Reads the content of the file with the given path.
   * 
   * @param {string} file the full path of the file.
   * @returns {string} the content of the file.
   */
  readFile(file) {
    const data = fs.readFileSync(file, 'utf8');
    return data;
  },
  /**
   * Uses context in @actions/Github to find data associated with PullRequest.
   * Data is used when comparing two commits.
   * @param {context} context in @actions/Github
   * @returns data = {base:base sha for PR, head:head sha for PR, owner:owner of repo, repo: the repo  }
   */
  parseContext(context) {
    const data = {
        base: context.payload.pull_request &&
              context.payload.pull_request.base &&
              context.payload.pull_request.base.sha
              ? context.payload.pull_request.base.sha
              : undefined,
        head: context.payload.pull_request &&
              context.payload.pull_request.head &&
              context.payload.pull_request.head.sha
              ? context.payload.pull_request.head.sha
              : undefined,
        owner: context.repo && context.repo.owner
                ? context.repo.owner : undefined,
        repo:  context.repo && context.repo.repo
                ? context.repo.repo : undefined,
    };
    if (!data.base || !data.head || !data.owner || !data.repo) {
      throw Error(`Head, base, owner or repo are missing from the payload for this `+
      `${context.eventName} event. Please submit an issue on this action's GitHub repo.`
      );
    }
    return data;
  },
  /**
   * Extracts kth addresses from file, format of the file needs to 
   * have a specific structure, structured is described in README.
   * @param {string} file the full path of the README file.
   * @returns array of kth addresses in README file
   */
  parseKTHEmail(file) {
    const error = (type) => `
      Incorrect format for the member section
      - ${type}
      
      Make sure to use the following format:
      ## Members
      -----
      <Student1Name> (<Username1>@kth)
      Github: [<GithubID1>](<linkToGithubProfile1>)

      <Student2Name> (<Username2>@kth)
      Github: [<GithubID2>](<linkToGithubProfile2>)

      -----`;

    const data = this.readFile(file);
    const memberSection = data.match(/-----[^-----]+-----/);
    if (!memberSection) throw Error(
      error('Could not find the opening and closing \'-----\' tag.')
    );
    const addresses = memberSection[0].match(/(([\w\d\._%+-]+)@kth.se)/g);
    if (!addresses) throw Error(error('Could not find the kth email addresses.'))

    return addresses
  },
  /**
   * Retrives valid kthIDs from the file `KTH_IDS_FILE` defined
   * in config.
   * 
   * @returns {string[]} An array of valid KTH ids.
   */
  parseKTHIdsFile() {
    const data = this.readFile(KTH_IDS_FILE);
    return data.split(/[\s,;]+/g);
  },
  /**
   * Find path of the `README.md` file of the contribution directory.
   * 
   * @param {Object} response commit comparison object.
   * @returns {string} The path of the `README.md` file.
   */
  parseReadmePath(response) {
    const filteredFiles = response.data.files
      .map(file => file.filename.split('/'))
      .filter(file => file.length > 3 && file[0] === 'contributions' );
    if (filteredFiles.length < 1) {
      throw Error('Could not find path of the README.md file in the contribution directory.');
    }
    return [...filteredFiles[0].splice(0,3), 'README.md'].join('/');
  }
};
