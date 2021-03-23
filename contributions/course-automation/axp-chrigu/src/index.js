const core = require("@actions/core");

try {
    const time = new Date().toTimeString();
    core.setOutput("dashboard", `dashboard - ${time}`);
} catch (error) {
    core.setFailed(error.message);
}
