# Assignment Proposal

## Title
Infrastructure as Code and Automated Security Scanning with Terraform, Checkov, and Trivy

## Names and KTH ID
- Anna Remmare ([remmare@kth.se](mailto:remmare@kth.se))
- Derfesh Mariush ([derfesh@kth.se](mailto:derfesh@kth.se))

## Deadline
- Task 3

## Category
- Executable tutorial

## Description

This executable tutorial shows how to set up cloud infrastructure with code and how to automatically check for security problems when a change is pushed.

The tutorial runs in Google Colab: [Infrastructure as Code and Automated Security Scanning](https://colab.research.google.com/drive/1ETQWbnib6EFdHSxfSBiuiHWRrj-kfKW-#scrollTo=kKTe5WQtZQuj). The example project is a food-planning website built with JavaScript, Node.js, and React. It is hosted on Firebase and uses Firestore to store planned dinners.

The tutorial uses one repository, [IaC-Testing](https://github.com/derfeshMariush/IaC-Testing), and one pipeline:

1. **Infrastructure as code**
   - Terraform creates a Google Cloud project, enables Firebase and Firestore, registers the web app, and creates the Firebase config used by the website.
   - `terraform apply` creates the setup and `terraform destroy` removes it, so the same setup can be run again from the notebook.

2. **Security checks in GitHub Actions**
   - A push to `main` starts the checks.
   - **Checkov** checks the Terraform files and fails the pipeline if Cloud Audit Logging is missing (`CKV2_GCP_5`).
   - **Trivy** checks the project dependencies and fails the pipeline if the `@grpc/grpc-js` pin is removed and a known serious vulnerability is included.
   - The notebook shows the failed check and then restores the clean files so the pipeline passes again.

The tutorial follows a change from the initial push to the security checks and shows both a failed and a passing result.

Relevance

Setting up cloud resources by clicking around in a console can be easy to get wrong, and it is also difficult for the rest of the team to see exactly what has changed. Security checks can have the same problem if they are done manually. Problems may be found late or not at all.

With this setup, the infrastructure is stored in Terraform, so it can be created, changed, and removed using git. GitHub Actions runs Checkov and Trivy when changes are pushed. Checkov checks the infrastructure files, while Trivy checks the project dependencies for known vulnerabilities. If a problem is found, the pipeline fails.

Colab makes it possible to run the whole example in the browser. The user can create the project, remove it, push a change with a security problem, and then restore the correct files.

The tutorial combines **infrastructure as code, continuous integration, and security checks** in one workflow that can be run and tested by the user.
