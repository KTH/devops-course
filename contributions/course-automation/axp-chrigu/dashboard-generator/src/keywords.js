const fetch = require("node-fetch");

const DEVOPS_TECHNOLOGIES_URL =
    "https://raw.githubusercontent.com/wmariuss/awesome-devops/master/README.md";

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
        if (!match[2].startsWith("#")) {
            result.push({ name: match[1], link: match[2] });
        }
    }

    return result;
};

const getKeywords = () => {
    return fetch(DEVOPS_TECHNOLOGIES_URL)
        .then((res) => res.text())
        .then(parseResponse);
};

module.exports.getKeywords = getKeywords;
