# Assignment Proposal

## Title

Introducing API sanity checker for C++

## Names and KTH ID
  - Arami Alfarhani (aramia@kth.se)
  - Nils Löfberg (nilslof@kth.se)

## Deadline

- Week 2

## Category

- Demo
## Description
## Description

We wish to demonstrate the use of <https://lvc.github.io/api-sanity-checker/> and explain its role (and sanity/smoke testing more generally) within devops more generally. It works by quickly generating shallow tests for each public function of a library, and then running them.

**Relevance**
It can be used to quickly check the functionality or "sanity" of a library in a more general sense, and quickly create a base for further testing. The eventual errors can outline where input should be restricted and where unexpected behaviour is encountered. Furthermore, the use of the tool can serve as a crude basis to check for more general regression, as a regression in the number of tests passed can indicate underlying problems in an update. 
