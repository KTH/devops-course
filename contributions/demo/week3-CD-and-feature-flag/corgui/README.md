# Assignment Proposal

## Title

Demonstration of Continuous Deployment of a Tauri app

## Names and KTH ID

-   Corentin Guilloteau (corgui@kth.se)

## Deadline

Task 1

## Category

Demo

## Description

Tauri is a rust based GUI framework which allows creating smaller, faster and more secure desktop applications with a
web frontend. Tauri allows developers to easily add an automatic updater in their app.

In this demo I showed how a developer can implement a pipeline to deploy automatically a new version of its Tauri
application. The work consist on the creation of a CircleCI pipeline, a server to hold and serve updates metadata and
the actual application used for the demonstration.

During the demo, I showed a real time deployment of a new version of the app, and I explained how it is related to CD.

This demo also includes an easter egg, to find it you should probably take a closer look at the dialog window asking for
whether a new update should be installed.

[Repository for the demo](https://github.com/corentinguilloteau/kth-devops-tauri-CD)
