# Essay
## Students
Mindaugas Varkalys varkalys@kth.se @MindaugasVarkalys  
Vincent Lohse vplohse@kth.se @olapiv

## Topic
How well does NodeJS + MariaDB API scale on Kubernetes cluster?

## Description
There are tons of companies which are using MariaDB database and NodeJS for large-scale systems. However, there are articles stating that both technologies are bad at scaling. 
So we would like to check that by doing benchmarks on NodeJS and MariaDB running on Kubernetes cluster and write an essay about the results.
The goal is to find out how the number of nodes affects the performance of NodeJS web server and MariaDB separately as well as our API which uses both of these technologies.

## Preliminary structure
- Introduction
- Background
    - What is NodeJS?
    - What is MariaDB?
    - What is Kubernetes?
- Setup 
    - Simple API - explain our API used for benchmarking
    - NodeJS - explain configurations used for benchmarking NodeJS
    - MariaDB - explain configurations used for benchmarking MariaDB 
- Benchmarking
    - NodeJS - explain benchmarking tools and results of NodeJS web server
    - MariaDB - explain benchmarking tools and results of MariaDB
    - API - explain benchmarking tools and results of API which uses NodeJS and MariaDB
- Conclusions 
