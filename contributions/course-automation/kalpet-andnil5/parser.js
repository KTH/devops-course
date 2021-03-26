const fs = require('fs');
const { join, resolve } = require('path');

module.exports = {
  readFile(file) {
    try {
      const data = fs.readFileSync('./kth-id.txt', 'utf8')
      return { data };
    } catch (error) {
      return { error: 'Could not resolve path to KTH ids file.' }
    }
  },
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
    return { data, error: !data.base || !data.head || !data.owner || !data.repo };
  },
  parseKTHEmail(file) {
    const { data, error } = this.readFile(file);
    if (error) return { error }
    const ma = data.match(/-----[^-----]+-----/);
    // TODO: ÄNDRA MEDDELANDET
    if (ma.length === 0) return { error: 'Something is wrong with the format, make sure to user ----- osvosv...'}
    const res = ma[0].match(/(([\w\d\._%+-]+)@kth.se)/g);
    // TODO: KOLLA VAD matchen returnerar om den inte finner någon matchning, är den en tom list är det lugnt,
    // annars borde vi skicka med ett error meddelande (kunde inte hitta några kth idn typ)
    return ma[0].match(/(([\w\d\._%+-]+)@kth.se)/g);
  },
};
