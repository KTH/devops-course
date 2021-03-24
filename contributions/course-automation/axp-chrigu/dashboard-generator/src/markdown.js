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

/**
 *
 * @param {Result[number]["categories"][number]["tasks"][number]["authors"]} authors
 * @returns
 */
const parseAuthors = (authors) => {
    return authors.join(" & ");
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
            `- ${parseAuthors(task.authors)} - [${task.title}](${task.authors})`
        );
    });
    return markdown;
};

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

    // Add years
    Object.keys(result)
        .filter((key) => key !== "summary")
        .sort((a, b) => parseInt(b) - parseInt(a))
        .forEach((yearKey) => {
            const year = result[parseInt(yearKey)];
            markdown.push(`## ${yearKey}`);
            markdown.push(`Submissions this year: ${year.nrTotal}`);

            year.categories.forEach((category) => {
                markdown = parseCategory(markdown, category);
            });
        });

    return markdown.join("\r\n");
};

module.exports.parseJson = parseJson;
