# Assignment Proposal

## Title
Event-Driven Security: A Containerized SOAR Tutorial with Flask, Ansible, and Docker

## Names and KTH ID
- Leo Hansson Åkerberg (leo3@kth.se)

## Deadline
Task 3

## Category
Executable tutorial

## Description
This executable tutorial demonstrates how to build an event-driven, containerized SOAR (Security Orchestration, Automation, and Response) workflow. This project aims to create a realistic DevSecOps pipeline that responds dynamically to security events.

The tutorial will be hosted on a platform like mybinder.org, providing a browser-based environment with Flask, Ansible, and Docker and the user of the tutorial will execute the following automated workflow: 

1.  **Setup:** The user will start a simple Nginx web server running inside a Docker container and a Flask application to serve as a webhook. 
2.  **Trigger:** The user sends a suspicious IP address to a specific endpoint on the Flask web application, simulating an alert from a monitoring tool. 
3.  **Enrichment:** The Flask app triggers an Ansible playbook, which queries APIs like AbuseIPDB and VirusTotal to analyze the IP. 
4.  **Response:** Based on the analysis, Ansible generates a report. If the IP is deemed malicious (for example, a high abuse score), the playbook dynamically updates a blocklist on the running Nginx container and reloads its configuration to block the IP without service interruption.

This tutorial provides hands-on experience with building an automated security response system that integrates web services and containerization. 

** Relevance **
This proposal is relevant to DevOps and DevSecOps by demonstrating an automated and "as-code" approach to security operations: 

* **Automation of Complex Workflows:** It automates a complete workflow from trigger to response, which showcases automation.
* **Event-Driven Architecture:** The use of a Flask webhook to trigger the process shows event-driven practices that are used in DevOps environments.
* **Immutable Infrastructure Principles:** By managing the state of a running container through code (Ansible), the tutorial includes configuration management and infrastructure as code.
* **Practical DevSecOps:** This is an example of embedding automated security controls directly into operational workflows. 
