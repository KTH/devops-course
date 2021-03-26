const { join, resolve } = require('path');
const ACTION_DIRECTORY = resolve(__dirname);
module.exports = {
  KTH_IDS_FILE: join(ACTION_DIRECTORY, 'kth-ids.txt'),
  ROOT: join(ACTION_DIRECTORY, '..', '..', '..'),
};

