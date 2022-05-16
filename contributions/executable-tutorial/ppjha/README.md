# Assignment Proposal

## Title

Secure Linux webserver 

## Names and KTH ID
  - Philip Hamelink (ppjha@kth.se)
## Deadline

Task 3 May 3, 17h Stockholm time

## Category

Executable tutorial

## Description

I want to create a step-by-step guide on how to deploy a secure webserver on linux.
Starting from a default project that includes an API server and a React website, I want to show how you can secure the webserver 
by enabling basic ssh access as a non-root user, set up a firewall to only allow incoming https requests. I then want to show how you can
set up a reverse proxy with nginx to serve either API requests or the static website's files. 

I plan on doing a step by step demonstration, explaining every notion and showing the results to the user (for example when restricting ssh access
to only non-root users, show that access is denied by letting the user try anyway).

Final submission links: 

Katacoda-Scenario Repository: https://github.com/phamelink/katacoda-scenarios/tree/main/secure-server-tutorial

Katacoda-Scenario Tutorial: https://katacoda.com/phamelink/scenarios/secure-server-tutorial
