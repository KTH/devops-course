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
