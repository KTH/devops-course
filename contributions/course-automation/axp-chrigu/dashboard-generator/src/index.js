const core = require("@actions/core");
const { collectDashboardData } = require("./dataCollection");
const { parseJson } = require("./markdown");

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

// try {
//     const time = new Date().toTimeString();
//     core.setOutput("dashboard", `dashboard - ${time}`);
// } catch (error) {
//     core.setFailed(error.message);
// }

async function generateDashboard(){
    try{
        const data = await collectDashboardData();
        const md = parseJson(data);
        core.setOutput("dashboard", md);
    } catch(error) {
        core.setFailed(error.message);
    }
}

generateDashboard();