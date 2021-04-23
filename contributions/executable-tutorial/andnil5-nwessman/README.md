# Executable tutorial: CI workflow using GitHub actions for Node.js, Express app, Jest and ESLint - PR [#1269](https://github.com/KTH/devops-course/pull/1269)

Continuous Integration (CI) is the practice of creating a smooth integration process on your software projects by continuously merging the developers' branches into the main branch. For this, to work we need to assert each merge's correctness before they can be integrated into the main repository, and for this, we use automated tests.   

This tutorial will go through the steps of setting up a pre-built Express application that we then use to set up automatic testing with `Jest` and `Supertest` and linting with `ESLint`, explaining the fundamentals of testing and linting in the process. Finally, we apply our newly acquired knowledge when we set up `Continuous Integration (CI)` with testing/linting using `GitHub Actions`.

### Tutorial outline:
1. Background
2. Before you begin
3. Express application overview and set up
4. Automated integration testing for API endpoints with Jest and Supertest
5. Mocking the data model
6. Static code analysis with ESLint
7. Continous Integration with GitHub Actions
8. Testing the GitHub Action

## Katacoda link

- [Katacoda Executable Tutorial](https://www.katacoda.com/nwessman/scenarios/ci)

## GitHub links

- [GitHub - Katacoda branch](https://github.com/nwessman/katacoda-scenarios)
- [GitHub - Tutorial project](https://github.com/nwessman/katacoda-scenarios/tree/express-app)
- [GitHub - Complete Tutorial project](https://github.com/nwessman/katacoda-scenarios/tree/express-app-complete)

## Feedback links

- [Feedback - Elin Ryman](https://github.com/KTH/devops-course/pull/1269#issuecomment-823304162)
- [Feedback - Agnes Forsberg](https://github.com/KTH/devops-course/pull/1269#issuecomment-823306034)
- [Feedback - Follow up documentation](https://github.com/KTH/devops-course/pull/1269#issuecomment-824204630)

## Members
Anders Nilsson (andnil5@kth.se)  
Github: [andnil5](https://github.com/andnil5)

Niklas Wessman (nwessman@kth.se)  
Github: [nwessman](https://github.com/nwessman)

## Grading - We strive to meet the following grading criteria
|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) | X |  | X |
|If local execution, runs on Linux | X |  | X  |
|The tutorial gives enough background | X |  | X |
|The tutorial is easy to follow  | X |  |  |
|The tutorial is original, no such tutorial exists on the web | Not all-in-one |  |  |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | X |  |  |
|The tutorial is successful (attracts comments and success) | |  |  |
|The language is correct | X |  | X |
