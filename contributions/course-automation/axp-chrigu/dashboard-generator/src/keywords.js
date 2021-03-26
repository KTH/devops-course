const fetch = require("node-fetch");

const DEVOPS_TECHNOLOGIES_URL =
    "https://raw.githubusercontent.com/wmariuss/awesome-devops/master/README.md";
const AWESOME_TECHNOLOGIES_URL =
    "https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md";

const PATTERN = /\[(.+)\]\((.+)\)/g;

const REMOVE_PATTERN = /# Awesome DevOps.*---/gs;

/**
 *
 * @typedef {import('./dataCollection').Result} DataCollectionResult
 *
 */

/**
 *
 * @typedef Keywords
 * @type {{name: string, link: string}[]}
 *
 * @typedef KeywordReturn
 * @type {{
 *           [keyword: string]: {
 *                  link: string:
 *                  tasks: {
 *                      [category: string]: {
 *                               authors: string[],
 *                               link: string,
 *                               title: string,
 *                               year: number,
 *                      }[]
 *                  }
 *              }
 *           }
 *        }}
 */

/**
 *
 * @param {string} data
 * @returns {Keywords}
 */
const parseResponse = (data) => {
    const filtered = data.replace(REMOVE_PATTERN, "");
    const matches = filtered.matchAll(PATTERN);

    const result = [];

    for (const match of matches) {
        if (
            !match[2].startsWith("#") &&
            match[1] !== "here" &&
            match[1] !== "Learning" &&
            match[1] !== "Tips" &&
            match[1] !== "Core" &&
            match[1] !== "Readme" &&
            match[1] !== "Testing" &&
            match[1].length > 2
        ) {
            result.push({ name: match[1], link: match[2] });
        }
    }
    return result;
};

/**
 * Returns keywords from the Awesome GitHub repo
 * @returns {Promise<Keywords>}
 */
const getAwesomeKeywords = () => {
    return fetch(AWESOME_TECHNOLOGIES_URL)
        .then((res) => res.text())
        .then(parseResponse);
};

/**
 * Returns keywords from the Awesome DevOps technologies GitHub repo
 * @returns {Promise<Keywords>}
 */
const getDevopsKeywords = () => {
    return fetch(DEVOPS_TECHNOLOGIES_URL)
        .then((res) => res.text())
        .then(parseResponse);
};

/**
 * Remove duplicates from list
 * @param {Keywords} list
 * @returns {Keywords}
 */
const removeDuplicates = (list) => {
    return list.filter(
        (keyword, index) =>
            list.findIndex((a) => a.name === keyword.name) === index
    );
};

/**
 * Return all keywords from different data sources
 * @returns {Keywords}
 */
const getKeywords = () => {
    const promises = [getAwesomeKeywords(), getDevopsKeywords()];
    return Promise.all(promises).then(([awesome, devops]) => {
        return removeDuplicates([...awesome, ...devops]);
    });
};

/**
 * Categorize of with mentions of technologies
 * @param {DataCollectionResult} data
 * @returns {Promise<KeywordReturn>}
 */
const categorizeKeywords = async (data) => {
    const keywords = await getKeywords();
    /**
     * @type {KeywordReturn}
     */
    const result = {};
    for (const keyword of keywords) {
        [...data.year.entries()].forEach(([yearKey, year]) => {
            year.categories.forEach((category) => {
                category.tasks.forEach((task) => {
                    if (task.content && task.content.includes(keyword.name)) {
                        if (!(keyword.name in result)) {
                            result[keyword.name] = {
                                link: keyword.link,
                                tasks: {},
                            };
                        }
                        if (!(category.name in result[keyword.name].tasks)) {
                            result[keyword.name].tasks[category.name] = [];
                        }
                        result[keyword.name].tasks[category.name].push({
                            authors: task.authors,
                            link: task.link,
                            title: task.title,
                            year: yearKey,
                        });
                    }
                });
            });
        });
    }

    return result;
};

module.exports.categorizeKeywords = categorizeKeywords;
