# Assignment Proposal

## Title

BlueBuild: The Cloud-Native Desktop Paradigm

## Names and KTH ID

  - Iñigo Aréjula Aísa (inigoaa@kth.se)
  - Pere Mateu Raventós (peremr@kth.se)

## Deadline

- Week 5

## Category

- Presentation

## Description

[BlueBuild](https://blue-build.org/) is a tool that leverages the concept of a cloud-native desktop. It integrates DevOps workflows into the process of building Linux distribution images, offering a new way for users to interact with their computers. The entire operating system is defined declaratively in a YAML file and built using GitHub Actions pipelines. The resulting images are immutable, meaning users cannot modify them, ensuring consistency and reproducibility across all images.

A key advantage is that since the whole build process runs in the cloud, errors are caught in the pipeline, guaranteeing a functional operating system, so you will always boot.

As an atomic operating system, BlueBuild promotes the use of isolated subsystems, reducing system bloat and preventing operating system instability.

**Relevance**

This tool brings all that we have learn from DevOps methodology to a more traditional domain. It enables us to define our infrastructure (operating system) as code, providing benefits such as reproducibility, version control, and portability.