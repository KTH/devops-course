# Assignment Proposal

## Title

Implementation of a DevOps pipeline for a small, open-source Flask application

## Names and KTH ID

  - Alexander Wigren (wig@kth.se)
  - Dawa Arkhang (arkhang@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

Our proposed project consists of implementing a simple but robust CI/CD pipeline for a small open-source project, utilizing IaC to deploy it in the cloud. Specifically, the application we have chosen is a simple CRUD implementation utilizing Flask and SQLAlchemy, generously provided by its author Samim Sarkar, which may be found [here](https://github.com/iamsamimsarkar/flask-crud-sqlite?utm_source=chatgpt.com).

We have used the grading criteria to outline the following plan which we believe satisfies all the requirements for the project:

- CI: GitHub Actions will be used to run the CI pipeline on pull requests and pushes. We will run automated tests with pytest and perform static code analysis with Ruff (Thereby fulfilling the additional requirement for using a quality/static analysis element), verifying that the application can be successfully built as a Docker image.

- CD: After changes are merged to the main branch and all CI checks pass, our application will be automatically built as a Docker image and then deployed to our chosen cloud infrastructure (Our current plan is to use Google Cloud if everything works out).

- IaC: To enable our deployment of the application, we will use Terraform as our IaC solution to define and manage the cloud infrastructure.

- Quality/Security Automation: As we mentioned in the CI bullet, we intend to use Ruff to perform static analysis.

If you have any thoughts or feedback on our plan, we would be happy to hear it! 

**Relevance**

We believe the above project plan is satisfactory from a relevance perspective. We use many different types of automation to enable CI/CD, following DevOps principles. We use infrastructure as Code principles with Terraform and we also take advantage of a quality automation with Ruff. The tools we have chosen are well known and mature, being used in the real world for production pieplines.
