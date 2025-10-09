# Assignment Proposal

## Title

Fuzzing in your CI with OSS-Fuzz: detect unexepected bugs early.

## Names and KTH ID

- Guillaume ROBOAM (roboam@kth.se)
- Birger Karlsson (birgerk@kth.se)

## Deadline

Week 2

## Category

Presentation

## Description

We want to cover the topic of fuzzing.
For this, we will use OSS-Fuzz, an open-source tool developped by Google to integrate your fuzzers into your CI pipeline.


We will explain what OSS-Fuzz is, who uses it, for what purposes and how you can integrate simply it in your own CI pipeline.

We will cover the importance of using those tools by leveraging some real critical examples of vulnerabilities that could have been / have been prevented by fuzzing. 


**Relevance**

OSS-Fuzz is designed to perform continuous fuzzing at each PR to avoid bugs early. It's a powerfull and easy tool to integrate in your CI pipeline.

Fuzzing is part of the security standards promoted by ISO for environments where money/lives are at stakes. It can also be leveraged to detect bugs caused by unexpected inputs, not covered by other form of testing at first.
