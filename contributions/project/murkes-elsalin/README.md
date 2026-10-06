# Assignment Proposal

## Title
DevOps pipeline for library React application

## Names and KTH ID

Felicia Murkes (murkes@kth.se) <br>
Elsa Linnéusson (elsalin@kth.se)

## Deadline
11 October 2026

## Category
Project

## Description
We are going to use a library website with Next.js/React (TypeScript), backed by a database in firebase for 
catalog and user data. Core features include book/media search and catalog browsing, user accounts and 
loan/reservation status. In the future an admin interface for managing the catalog is planned.

For this project we are going to implement a CI pipeline via a GitHub Actions workflow (lint + unit tests with Jest),
CD via GitHub Actions auto-deploying to Firebase Hosting/Vercel on merge to main; IaC via a small Terraform 
config for the core Firebase resources (Firestore, Hosting). GitHub as the development platform with basic 
branch protection; quality/security automation via Dependabot and GitHub's built-in secret scanning

**Relevance:** This project directly applies the core DevOps concepts taught in the course, continuous integration, 
continuous delivery, infrastructure as code, and automated quality/security checks to a real, working application. 
The repository currently has no DevOps practices in place and is under active development, making it a good candidate for this project.
