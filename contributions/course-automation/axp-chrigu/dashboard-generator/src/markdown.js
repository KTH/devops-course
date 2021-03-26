/**
 *
 * @typedef {import('./dataCollection').Result} DataCollectionResult
 *
 * @typedef {import('./keywords').KeywordReturn} Keywords
 *
 * @typedef {ReturnType<DataCollectionResult["year"]['get']>} Year
 */

/**
 *
 * @param {Year["categories"][number]["tasks"][number]['authors']} authors
 * @returns {string}
 */
const parseAuthors = (authors) => {
    if (authors) return authors.join(" & ");
    return "Authors not found";
};

/**
 *
 * @param {string[]} markdown
 * @param {Year["categories"][number]} category
 */
const parseCategory = (markdown, category) => {
    markdown.push(`### ${category.name}`);
    category.tasks.forEach((task) => {
        markdown.push(
            `- ${parseAuthors(task.authors)} - [${
                task.title || "Title not found"
            }](${task.link})`
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
    for (const [key, value] of yearsData.entries()) {
        value.categories.forEach((category) => {
            const categoryData = yearPerCategory.get(category.name);
            if (categoryData) {
                categoryData[key] = category.tasks.length;
            } else {
                const c = {};
                c[key] = category.tasks.length;
                yearPerCategory.set(category.name, c);
            }
        });
    }

    return yearPerCategory;
};

/**
 * Generate a markdown table that summarises number of sumbissions per year and category
 * @param {Map} yearsData
 * @returns {string}
 */
const generateSummaryTable = (yearsData) => {
    const data = getYearPerCategory(yearsData);
    let markdown = [];
    const years = Array.from(yearsData.keys());
    // Header and alignment
    let header = "| Category |";
    let alignment = "|-|";
    years.forEach((year) => {
        header += ` ${year} |`;
        alignment += "-|";
    });
    markdown.push(header);
    markdown.push(alignment);

    // Generate rows in the form | category | submissions year X | submissions year X+1 | ... |
    for (const [key, value] of data) {
        let row = `| ${key} |`;
        years.forEach((year) => {
            const count = value[year] ? value[year] : 0;
            row += ` ${count} |`;
        });
        markdown.push(row);
    }

    let totalRow = `| **Total** |`;
    years.forEach((year) => {
        totalRow += ` ${yearsData.get(year).nrTotal} |`;
    });
    markdown.push(totalRow);

    return markdown.join("\r\n");
};

/**
 * @param {Keywords} keywords
 * @return {string}
 */
const generateKeywordTable = (keywords) => {
    let markdown = [];
    markdown.push("## Keywords");
    // Header
    markdown.push("| Keyword | Submissions |");

    // Specify alignment
    markdown.push("|-|-|");
    // Generate rows in the form | keyword | submissions |
    for (const [keyword, value] of Object.entries(keywords)) {
        let row = `| [${keyword}](#${keyword.replace(/\s/g, "-")}) |`;
        let submissions = 0;
        for (const category of Object.values(value.tasks)) {
            submissions += category.length;
        }
        row += ` ${submissions} |`;
        markdown.push(row);
    }

    return markdown.join("\r\n");
};

/**
 * @param {Keywords} keywords
 * @return {string}
 */
const generateKeywordCategories = (keywords) => {
    let markdown = [];

    for (const [keyword, value] of Object.entries(keywords)) {
        markdown.push(`### [${keyword}](${value.link})`);
        for (const [category, tasks] of Object.entries(value.tasks)) {
            markdown.push(`#### ${category}`);
            for (const task of tasks) {
                markdown.push(
                    `- ${parseAuthors(task.authors)} - [${
                        task.title || "Title not found"
                    }](${task.link}) (${task.year})`
                );
            }
        }
    }

    return markdown.join("\r\n");
};

/**
 * Parse the JSON object to a markdown string
 * @param {Result} result
 * @param {Keywords} keywords
 * @returns {string}
 */
const parseJson = (result, keywords) => {
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
    // Add keyword summary
    markdown.push(generateKeywordTable(keywords));
    markdown.push(generateKeywordCategories(keywords));

    return markdown.join("\r\n");
};

module.exports.parseJson = parseJson;
