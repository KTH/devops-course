# Assignment Proposal

## Title

Automating dependency management and versioning using NuGet packages

## Names and KTH ID

  - Halan Ouensanga (halano@kth.se)
  - Nolan Blanc (nmsblanc@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

We want to present the NuGet package manager, and how it allows developers to create, share, and import public or private dependencies for .NET applications. Developped by Microsoft as the official package manager for the .NET framework, package updates towards remote galleries can be integrated in CI/CD pipelines to automatically provide new versions when new code is merged. It is especially useful for sharing code between repositories: since development teams often choose to split their code into different repos to separate concerns further, it makes it easier to keep their dependencies up to date.

**Relevance**

When companies have people working in parallel on different parts of an app, and packages are regularly updated with new code, versioning, automatic updates, tests, and conflict checks need to be operational. It can be especially tricky if new pushes use code that is not up to date, or when the same dependency is being worked on in two different places. 
