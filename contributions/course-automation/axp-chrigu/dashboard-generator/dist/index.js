module.exports =
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ 14:
/***/ ((module, __unused_webpack_exports, __nccwpck_require__) => {

const fs = __nccwpck_require__(747);
const path = __nccwpck_require__(622);

// collectDashboardData().then(data => {
//     console.log(data);
// });

const repoUrl = "https://github.com/KTH/devops-course/tree/2021/";

// Traverse the project directory and look for all the contributions folders, collect task data on every folder
async function* traverse(dir) {

    for await (const d of await fs.promises.opendir(dir)) {
        const a = new Map();
        const entry = path.join(dir, d.name);
        if (d.isDirectory()) {
            if(d.name.includes('contributions')){
                const currentTime = new Date();
                // If folder name contains the year, use it, otherwise it is contributions for the current year
                year = isNaN(d.name.slice(-4)) ? currentTime.getFullYear() : parseInt(d.name.slice(-4))
                // Collect the data of a given years contributions
                yield* a.set(year, collectYearData(entry));
            }
            else{
                // Found non-task associated file, skip
                yield* traverse(entry);
            }
        }
    }
}

async function* collectYearData(dir){
    const categories = [];
    let totalTaskCount = 0;
    // Go trough the directory and find all category directories
    for await (const categoryDir of await fs.promises.opendir(dir)) {
        if(categoryDir.isDirectory()){
            const categoryPath = path.join(dir, categoryDir.name);
            const {taskCount, data} = await collectCategoryData(categoryPath);
            totalTaskCount += taskCount;
            categories.push({'name': categoryDir.name, 'tasks': data});
        }
    }
    categories.unshift(totalTaskCount);
    yield* categories;
}

async function collectCategoryData(categoryPath){
    const categoryData = [];
    let taskCount = 0;
    // Go trough all the task in a given category directory
    for await (const taskDir of await fs.promises.opendir(categoryPath)) {
        if(taskDir.isDirectory()){
            // If folder is called weekX, its the presentation folder where tasks are divided into weeks,
            // iterate over the specific week folders
            if(taskDir.name.includes("week") || taskDir.name.includes("weak")){
                const entry = path.join(categoryPath, taskDir.name); 
                for await (const presentationTaskDir of await fs.promises.opendir(entry)) {
                    if(presentationTaskDir.isDirectory()){
                        const presentationEntry = path.join(entry, presentationTaskDir.name+"/README.md");
                        taskCount++;
                        categoryData.push(collectDataFromFile(presentationEntry));
                    }
                }
            }
            // Not the presentation folder, task folders are located here, read the task README and collect the data
            else{
                const entry = path.join(categoryPath, taskDir.name+"/README.md");
                taskCount++;
                categoryData.push(collectDataFromFile(entry));
            }
        }
    }
    return {'taskCount': taskCount, 'data': categoryData};
}

function collectDataFromFile(entry){
    const result = {'title': null, 'authors': null, 'link': (repoUrl+entry).slice(0, -10), 'content': null}
    try{
        const data = fs.readFileSync(entry, 'utf-8');
        // Parse md file for authors, title and link
        const {title: t, authors: a} = parseMd(data);
        result.title = t.replace(/`/g, "");;
        result.authors = a;
        result.content = data.replace(/`/g, "");;
    } catch(error){
        console.log(error.message);
    }
    return result;
}

// Parse a given string in md format, return authors and title
function parseMd(mdContent){
    
    // Find title by locating first h1 in the markdown, and taking that as title
    const titleRegex = /^# (.*$)/gim
    let title = mdContent.match(titleRegex);
    if(title != null) title = title[0].slice(2);

    // Find author by locating line where kth-email is listed, taking it as the author
    const authorRegex = /(.*@kth.se.*)/gim
    let authors = mdContent.match(authorRegex);
    if(authors != null ) authors = authors.map(authString => {
        // Remove all characters of type (#,*,|,-), leading whitespace and line breaks
        const result = authString
        .replace(/[#*|-]/g, "")
        .replace(/^[ \t0-9.]+/, "")
        .replace("</br>", "")
        .replace("<br>", "");
        return result;
    });

    return {'title': title, 'authors': authors};
}

async function collectDashboardData() {
    const year = new Map();
    let totalTaskCount = 0;
    // Wait for all data items to be collected
    for await (const p of traverse('./')){
        const allItems = [];
        for await (const item of p[1]) {
            allItems.push(item);
        }
        // add number of tasks in year to the total number of tasks
        totalTaskCount += allItems[0];
        // Map the year of the contributions to its number of tasks and the tasks
        year.set(p[0], {'nrTotal': allItems[0], 'categories': allItems.slice(1)});
    }
    const returnData = {'summary':{ 'nrTotal': totalTaskCount}, year}
    return returnData;    
}

module.exports.collectDashboardData = collectDashboardData;

/***/ }),

/***/ 736:
/***/ ((__unused_webpack_module, __unused_webpack_exports, __nccwpck_require__) => {

const core = __nccwpck_require__(470);
const { collectDashboardData } = __nccwpck_require__(14);
const { parseJson } = __nccwpck_require__(589);

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

/***/ }),

/***/ 589:
/***/ ((module) => {

/**
 * Result type of data collection
 * @typedef Result
 * @type {{
 *  summary: {
 *    nrTotal: number
 *  },
 *  year: {
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
 * }
 * }}
 */

/**
 *
 * @param {Result[number]["categories"][number]["tasks"][number]["authors"]} authors
 * @returns
 */
const parseAuthors = (authors) => {
    if(authors) return authors.join(" & ");
    return "Authors not found";
};

/**
 *
 * @param {string[]} markdown
 * @param {Result[number]["categories"][number]} category
 */
const parseCategory = (markdown, category) => {
    markdown.push(`### ${category.name}`);
    category.tasks.forEach((task) => {
        markdown.push(
            `- ${parseAuthors(task.authors)} - [${task.title || "Title not found"}](${task.link})`
        );
    });
    return markdown;
};

/**
 * Generate a map with number of submissions each year per category
 * @param {Map} yearsData
 * @returns {Map}
 */
const getYearPerCategory = (yearsData) => {
    const yearPerCategory = new Map();
    for(const [key, value] of yearsData.entries()){
        value.categories.forEach(category => {
            const categoryData = yearPerCategory.get(category.name);
            if(categoryData){
                categoryData[key] = category.tasks.length;
            }
            else{
                const c = {};
                c[key] = category.tasks.length;
                yearPerCategory.set(category.name, c);
            }
        })
    };
    
    return yearPerCategory;
}

/**
 * Generate a markdown table that summarises number of sumbissions per year and category
 * @param {Map} yearsData
 * @returns {string}
 */
const generateSummaryTable = (yearsData) => {
    const data = getYearPerCategory(yearsData);
    let markdown = [];
    const years = Array.from(yearsData.keys());
    // Header
    let header = "| Category |";
    years.forEach(year => {
        header += ` ${year} |`;
    });
    markdown.push(header);
    
    // Specify alignment
    markdown.push("|-|-|-|")

    // Generate rows in the form | category | submissions year X | submissions year X+1 | ... |
    for(const [key, value] of data){
        let row = `| ${key} |`;
        years.forEach(year => {
            const count = value[year] ? value[year] : 0;
            row += ` ${count} |`;
        })
        markdown.push(row);
    }

    let totalRow = `| **Total** |`;
    years.forEach(year => {
        totalRow += ` ${yearsData.get(year).nrTotal} |`;
    })
    markdown.push(totalRow);
    
    return markdown.join("\r\n");
}

/**
 * Parse the JSON object to a markdown string
 * @param {Result} result
 * @returns {string}
 */
const parseJson = (result) => {
    let markdown = [];
    // Add title
    markdown.push("# Dashboard");
    // Add total summary
    markdown.push(`Total submissions: ${result.summary.nrTotal}`);
    // Add table summary
    markdown.push("## Submissions per year");
    markdown.push(generateSummaryTable(result.year));

    // Add years
    [...result.year.keys()]
        .sort((a, b) => parseInt(b) - parseInt(a))
        .forEach((yearKey) => {
            const year = result.year.get(yearKey);
            markdown.push(`## ${yearKey}`);
            markdown.push(`Submissions this year: ${year.nrTotal}`);

            year.categories.forEach((category) => {
                markdown = parseCategory(markdown, category);
            });
        });

    return markdown.join("\r\n");
};

module.exports.parseJson = parseJson;


/***/ }),

/***/ 470:
/***/ ((module) => {

module.exports = eval("require")("@actions/core");


/***/ }),

/***/ 747:
/***/ ((module) => {

"use strict";
module.exports = require("fs");;

/***/ }),

/***/ 622:
/***/ ((module) => {

"use strict";
module.exports = require("path");;

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __nccwpck_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		if(__webpack_module_cache__[moduleId]) {
/******/ 			return __webpack_module_cache__[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		var threw = true;
/******/ 		try {
/******/ 			__webpack_modules__[moduleId](module, module.exports, __nccwpck_require__);
/******/ 			threw = false;
/******/ 		} finally {
/******/ 			if(threw) delete __webpack_module_cache__[moduleId];
/******/ 		}
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat */
/******/ 	
/******/ 	__nccwpck_require__.ab = __dirname + "/";/************************************************************************/
/******/ 	// module exports must be returned from runtime so entry inlining is disabled
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	return __nccwpck_require__(736);
/******/ })()
;