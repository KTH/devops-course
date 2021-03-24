const core = require("@actions/core");

/**
 * Result type of data collection
 * @typedef Result
 * @type {{
 *  summary: {
 *    nrTotal: number
 *  },
 *  [year: number]: {
 *      nrTotal: number,
 *      categories: {
 *          name: string,
 *          tasks: {
 *              authors: string[],
 *              link: string,
 *              title: string
 *          }[]
 *       }[]
 *  }
 * }}
 */

try {
    const time = new Date().toTimeString();
    core.setOutput("dashboard", `dashboard - ${time}`);
} catch (error) {
    core.setFailed(error.message);
}
