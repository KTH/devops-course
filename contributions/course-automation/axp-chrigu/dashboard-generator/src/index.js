const core = require("@actions/core");
const { collectDashboardData } = require("./dataCollection");
const { categorizeKeywords } = require("./keywords");
const { parseJson } = require("./markdown");

async function generateDashboard() {
    try {
        const data = await collectDashboardData();
        const keywords = await categorizeKeywords(data);
        const md = parseJson(data, keywords);
        core.setOutput("dashboard", md);
    } catch (error) {
        core.setFailed(error.message);
    }
}

generateDashboard();
