# Assignment Proposal

## Title

MLOps for a malware domain name detector

## Names and KTH ID

- Vilhelm Prytz (vprytz@kth.se)
- Filip Dimitrijevic (filipdi@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

In malware, it is common to use a Domain Generation Algorithm ([DGA](https://en.wikipedia.org/wiki/Domain_generation_algorithm)) to generate a large number of domain names, and use these domain names to find its command-and-control server. The idea here is to build a simple classifier that flags such names. The focus of the project will be the complete MLOps pipeline around it. Hence, the model will be quite deliberately simple (character n-grams and one scikit-learn logistic regression per DGA family). We aim to follow the design as outlined by Colin Raffel in [Building Machine Learning Models Like Open Source Software](https://cacm.acm.org/opinion/building-machine-learning-models-like-open-source-software/): when a model change is submitted as a pull request, it will be tested automatically, and released with semantic versioning.

The model will be packaged in a Docker image with a simple API endpoint that accepts a domain name and returns its DGA family, and a boolean whether it is considered malicious or not.

- Development platform: GitHub for the repository, actions and packages.
- Data: the top 100 000 domain names from the [Tranco](https://tranco-list.eu) list as normal examples, and generated domains for each DGA family as malicious examples. Data tests run before training.
- CI: We will use GitHub actions, every PR will train the model and run tests. We will use test data to evaluate on each model change whether False-Positive Rate (FPR) or False-Negative Rate (FNR) has changed. These metrics will be compared to the latest release metrics, to indicate whether the model has improved or not. If it gets worse, or is below the accepted threshold, the test will fail and therefore block the merge.
- CD: A merge to main should deploy the next version of the model and API as a GitHub release. GitHub actions will be used to deploy the new API image on a Raspberry Pi (at home) that runs the Docker image with the API endpoint. This will use Tailscale to connect to the RPI. If a new version of the image fails a health check, it should roll back.
- Infrastructure as Code: we will make use of an Ansible playbook that sets up a fresh Raspberry Pi OS to have the necessary stack to run the API.
- Quality and security automation: Dependabot for dependencies, GitHub secret scanning, and Semgrep for static analysis. The model files are stored with [skops](https://skops.readthedocs.io/en/stable/).
- AI-assisted tools: we plan to use AI assisted tools for helping with the boilerplate related to the model setup here, since it is not part of the course material. We will do the actual implementation of the workflows and pipeline ourselves. We plan to document this in the report and in the README of the project.

**Relevance**

MLOps is when we apply DevOps practices to machine learning. We treat the data and configuration as source code and the model as the build artifact, as outlined in Raffel's article. So every change would be versioned and tested in CI on some parameters and compared to the previous release. It would then be deployed automatically (CD). Hence, this project would cover most of the MLOps lifecycle (data preparation, training, review, CI, CD).
