const fs = require("fs");
const path = require("path");

const repoUrl = "https://github.com/KTH/devops-course/tree/2021/";

/**
 * Result type of data collection
 * @typedef Result
 * @type {{
 *  summary: {
 *    nrTotal: number
 *  },
 *  year: Map<number, {
 *      nrTotal: number,
 *      categories: {
 *          name: string,
 *          tasks: {
 *              authors: string[],
 *              link: string,
 *              title: string,
 *              content: string
 *          }[]
 *       }[]
 *  }>
 * }}
 */

// Traverse the project directory and look for all the contributions folders, collect task data on every folder
async function* traverse(dir) {
    for await (const d of await fs.promises.opendir(dir)) {
        const a = new Map();
        const entry = path.join(dir, d.name);
        if (d.isDirectory()) {
            if (d.name.includes("contributions")) {
                const currentTime = new Date();
                // If folder name contains the year, use it, otherwise it is contributions for the current year
                year = isNaN(d.name.slice(-4))
                    ? currentTime.getFullYear()
                    : parseInt(d.name.slice(-4));
                // Collect the data of a given years contributions
                yield* a.set(year, collectYearData(entry));
            } else {
                // Found non-task associated file, skip
                yield* traverse(entry);
            }
        }
    }
}

async function* collectYearData(dir) {
    const categories = [];
    let totalTaskCount = 0;
    // Go trough the directory and find all category directories
    for await (const categoryDir of await fs.promises.opendir(dir)) {
        if (categoryDir.isDirectory()) {
            const categoryPath = path.join(dir, categoryDir.name);
            const { taskCount, data } = await collectCategoryData(categoryPath);
            totalTaskCount += taskCount;
            categories.push({ name: categoryDir.name, tasks: data });
        }
    }
    categories.unshift(totalTaskCount);
    yield* categories;
}

async function collectCategoryData(categoryPath) {
    const categoryData = [];
    let taskCount = 0;
    // Go trough all the task in a given category directory
    for await (const taskDir of await fs.promises.opendir(categoryPath)) {
        if (taskDir.isDirectory()) {
            // If folder is called weekX, its the presentation folder where tasks are divided into weeks,
            // iterate over the specific week folders
            if (
                taskDir.name.includes("week") ||
                taskDir.name.includes("weak")
            ) {
                const entry = path.join(categoryPath, taskDir.name);
                for await (const presentationTaskDir of await fs.promises.opendir(
                    entry
                )) {
                    if (presentationTaskDir.isDirectory()) {
                        const presentationEntry = path.join(
                            entry,
                            presentationTaskDir.name + "/README.md"
                        );
                        taskCount++;
                        categoryData.push(
                            collectDataFromFile(presentationEntry)
                        );
                    }
                }
            }
            // Not the presentation folder, task folders are located here, read the task README and collect the data
            else {
                const entry = path.join(
                    categoryPath,
                    taskDir.name + "/README.md"
                );
                taskCount++;
                categoryData.push(collectDataFromFile(entry));
            }
        }
    }
    return { taskCount: taskCount, data: categoryData };
}

function collectDataFromFile(entry) {
    const result = {
        title: null,
        authors: null,
        link: (repoUrl + entry).slice(0, -10),
        content: null,
    };
    try {
        const data = fs.readFileSync(entry, "utf-8");
        // Parse md file for authors, title and link
        const { title: t, authors: a } = parseMd(data);
        result.title = t ? t.replace(/`/g, "") : t;
        result.authors = a;
        result.content = data ? data.replace(/`/g, "") : data;
    } catch (error) {
        console.log(error.message);
    }
    return result;
}

// Parse a given string in md format, return authors and title
function parseMd(mdContent) {
    // Find title by locating first h1 in the markdown, and taking that as title
    const titleRegex = /^# (.*$)/gim;
    let title = mdContent.match(titleRegex);
    if (title != null) title = title[0].slice(2);

    // Find author by locating line where kth-email is listed, taking it as the author
    const authorRegex = /(.*@kth.se.*)/gim;
    let authors = mdContent.match(authorRegex);
    if (authors != null)
        authors = authors.map((authString) => {
            // Remove all characters of type (#,*,|,-), leading whitespace and line breaks
            const result = authString
                .replace(/[#*|-]/g, "")
                .replace(/^[ \t0-9.]+/, "")
                .replace("</br>", "")
                .replace("<br>", "");
            return result;
        });

    return { title: title, authors: authors };
}

/**
 *
 * @returns {Result}
 */
async function collectDashboardData() {
    const year = new Map();
    let totalTaskCount = 0;
    // Wait for all data items to be collected
    for await (const p of traverse("./")) {
        const allItems = [];
        for await (const item of p[1]) {
            allItems.push(item);
        }
        // add number of tasks in year to the total number of tasks
        totalTaskCount += allItems[0];
        // Map the year of the contributions to its number of tasks and the tasks
        year.set(p[0], { nrTotal: allItems[0], categories: allItems.slice(1) });
    }
    const returnData = { summary: { nrTotal: totalTaskCount }, year };
    return returnData;
}

module.exports.collectDashboardData = collectDashboardData;
