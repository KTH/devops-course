# Assignment Proposal

## Title

Automating Code Coverage Analysis in CI Pipeline

## Names and KTH ID

- Tianning Liang (tianning@kth.se)
- Peiyang Zheng (peiyang@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

This project aims to integrate a code coverage analysis tool (such as JaCoCo or Emma) into a CI pipeline. The coverage analysis will provide insights into the proportion of code exercised by tests, ensuring the robustness of the application. Additionally, the project will automate the process of saving coverage reports to the cloud, enabling historical comparisons and trend analysis.

Stretch Goal: Automate the entire process using GitHub Actions, ensuring that every code change triggers a coverage analysis and stores the results automatically.

**Relevance**

Code coverage is crucial for assessing the effectiveness of unit tests in covering the codebase. While running tests is essential, it’s equally important to understand which parts of the code are tested and which are not. This helps in identifying untested areas, reducing the risk of bugs. By integrating code coverage into the CI pipeline, we ensure that every change is scrutinized not only for correctness but also for completeness in terms of testing.

Additionally, by storing historical coverage data, teams can track their progress in improving test coverage over time. This historical perspective can be valuable in understanding the impact of refactoring, adding new features, or making other significant changes to the codebase.
