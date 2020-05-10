# Semantic Release Slack Notification Plugin

We created a plugin for [semantic-release](https://github.com/semantic-release/semantic-release) that notifies the user about any failed or possibly successful releases, on Slack. The finalized project is now avaliable publicly and open source at GitHub and NPM as [semantic-release-slack-bot](https://github.com/juliuscc/semantic-release-slack-bot). The bot can automatically publish messages upon both failure and success when running semantic release in your projects. The proposal is [here](Proposal.md).

## Group members

-   Julius Celik [jcelik@kth.se](mailto:jcelik@kth.se)
-   Hannes Rabo [hrabo@kth.se](mailto:hrabo@kth.se)

## DevOps in the project

The project itself uses _Continuous Delivery_ (CD) with [git-cz](https://github.com/commitizen/cz-cli), [semantic-release](https://github.com/semantic-release/semantic-release), and [CircleCI](https://circleci.com/gh/juliuscc/semantic-release-slack-bot). To maintain code quality for future development we also used [husky](https://github.com/typicode/husky), [lint-staged](https://github.com/okonet/lint-staged), [prettier](https://prettier.io/), [eslint](https://eslint.org/). This ensured that all code uploaded followed a common code standard, and used static analysis to reduce bugs.

## Challenges

The most difficult hurdle was to publish a working app to the Slack App Directory. To create an app and make it public and easily installable, a server wich can integrate using OAuth is required.

A simples server was published using an AWS Lambda function to perform this basic task of integrating with slack.

## Links

-   [Source code on GitHub](https://github.com/juliuscc/semantic-release-slack-bot)
-   [Plugin on NPM](https://www.npmjs.com/package/semantic-release-slack-bot)
