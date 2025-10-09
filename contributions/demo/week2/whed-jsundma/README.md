# Assignment Proposal

## Title

Automatic Testing for Evil Regexes

## Names and KTH ID

  - William Hedenskog (whed@kth.se)
  - Joakim Sundman (jsundma@kth.se)

## Deadline

Week 2

## Category

Demo

## Description

This demonstration will show an implementation of an [Evil Regex detector](https://github.com/davisjam/vuln-regex-detector) installed (if possible) in a Docker image connected to Github Actions, that is automatically run against pull requests. The program inside Docker will scan the files for regex patterns that could cause [ReDoS](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) if left in the source code. If any bad patterns are found, the PR will be rejected along with a comment.

**Relevance**

The program we plan on using can only run on Ubuntu and takes quite some time to install. This will be the perfect use case for automatic testing on a remote server, to avoid every developer having to run the tests locally, potentially with different configurations. 
