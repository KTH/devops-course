# Assignment Proposal

## Title

The Crowdstrike bug, and the importance of high-quality testing

## Names and KTH ID

  - Gustav Henningsson (ghenn@kth.se)
  - Viktor Fornstad (vikfor@kth.se)

## Deadline

- Week 2

## Category

- Presentation

## Description

We want to take a look at the Crowdstrike bug that happened in July of this year. 
Crowdstrike is a company that sells anti-malware services, endpoint protection software, and threat-intelligence services.
On the 19th of July 2024, a new version of one of their softwares caused over 8 million Windows computers to crash, due to a array out-of-bounds memory exception.
This was not caught in any of the testing done by Crowdstrike prior to deployment. The tests used Regular Expressions, and wildcard matching that missed the oob-exception every time. 
Since the software in question is running in kernel level 0, this was catastrophic for the computer, and caused an system-wide crash. 
We will look at how the automated testing failed, aswell as what Crowdstrike have done(or could have done) to fix it. 

**Relevance**

The bug in the update should have been caught by the automated testing Crowdstrike ran before deployment. 
However, due to the way that the tests were set up, this issue slipped through all tests and made it to live. 
This issue higlights the importance of not only having tests, but writing good tests. Just because your commit passes all tests does not mean that it's 100 procent safe. 
