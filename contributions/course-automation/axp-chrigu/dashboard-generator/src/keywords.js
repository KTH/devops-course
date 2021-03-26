const fetch = require("node-fetch");

const DEVOPS_TECHNOLOGIES_URL =
    "https://raw.githubusercontent.com/wmariuss/awesome-devops/master/README.md";

const AWESOME_TECHNOLOGIES_URL =
    "https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md";

const PATTERN = /\[(.+)\]\((.+)\)/g;

const REMOVE_PATTERN = /# Awesome DevOps.*---/gs;

/**
 *
 * @param {string} data
 * @returns {{name: string, link: string}[]}
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
            match[1] !== "Testing"
        ) {
            result.push({ name: match[1], link: match[2] });
        }
    }
    return result;
};

const getAwesomeKeywords = () => {
    return fetch(AWESOME_TECHNOLOGIES_URL)
        .then((res) => res.text())
        .then(parseResponse);
};

const getDevopsKeywords = () => {
    return fetch(DEVOPS_TECHNOLOGIES_URL)
        .then((res) => res.text())
        .then(parseResponse);
};

const getKeywords = () => {
    const promises = [getAwesomeKeywords(), getDevopsKeywords()];
    return Promise.all(promises).then(([awesome, devops]) => {
        return [...awesome, ...devops];
    });
};

const categorizeKeywords = async (data) => {
    /**
     * @type {{name: string, link: string}[]}
     */
    const keywords = await getKeywords();

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
                            ...task,
                            year: yearKey,
                        });
                    }
                });
            });
        });
    }
    console.log(result);
    return result;
};

module.exports.categorizeKeywords = categorizeKeywords;
