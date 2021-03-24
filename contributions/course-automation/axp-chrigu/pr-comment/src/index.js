const core = require("@actions/core");
const github = require("@actions/github");

const main = async () => {
    try {
        const message = core.getInput("message");
        const githubToken = core.getInput("GITHUB_TOKEN");

        const context = github.context;
        if (context.payload.pull_request == null) {
            core.setFailed("No pull request found.");
            return;
        }
        const pull_request_number = context.payload.pull_request.number;

        const octokit = github.getOctokit(githubToken);

        octokit.issues.createComment({
            ...context.repo,
            issue_number: pull_request_number,
            body: message,
        });
    } catch (error) {
        core.setFailed(error.message);
    }
};

main();
