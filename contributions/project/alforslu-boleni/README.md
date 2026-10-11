# Assignment Proposal

## Title

Reproducible CI/CD for a C++ Matrix Calculator

## Names and KTH ID

  - Alexander Forslund (alforslu@kth.se)
  - Jonatan Bölenius (boleni@kth.se)

## Deadline

- Task 1

## Category

- Project

## Description

We will implement a DevOps workflow around an existing C++ matrix library developed for a previous course. This library support matrix arithmetic, row column operations, and stream input/output. It already has a GoogleTest suite. We will reuse this implementation in a web interface that interfaces directly with the library.

The frontend will be developed with AI assistance using HTML, CSS and JS. The webserver will be packaged in a minimal python docker container that runs flask and calculations. Our cache, Redis, will be running in another container, and is meant to minimize calculation time for heavier operations (+ reduce I/O overhead of launching a Matrix binary process and reading results).

- CI: GitHub Actions will compile the library, run the unit tests, and build the docker image on pull requests and pushes to main. Integration tests will verify that HTTP requests to the docker container results in the same answer as the C++ code provides, as well as testing frontend availability.

- CD: Through GitHub actions we can setup a auto-deploy feature upon main branch changes to deploy the application through the Release section on GH. The releases will include a copy of the exact tested Docker image as an archive. It will also include its checksum, the configuration and startup instructions. Failed tests or quality checks will prevent publication.

- Infrastructure as code: By using Docker Compose we can manage container interconnecitivity (health checks, dependencies & communication) between the calculations and the cache database, redis.

- Development platform: GitHub.

- Quality and security automation: Dependabot for dependencies, valgrind and Cppcheck (in CI) for C++ quality checking.

- Documented use of AI-assisted tools: AI will be used, as mentioned, for the frontend. Other than that, we will implement all DevOps-related features ourselves. Any applications will be mentioned in the report.

**Relevance**

The project demonstrates how a C++ library can become a reproducibly built web application. Its focus is maintaining correctness, and handling the integration of two separate programs (C++-Matrix library & web application) in one single docker container, while simultaneously connecting this system to another system (the Redis cache).

The focus is automating the reproducibility of the project, instead of actually implementing the website/API/library functionality.
