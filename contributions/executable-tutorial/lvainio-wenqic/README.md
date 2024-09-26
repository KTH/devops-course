# Assignment Proposal

## Title

SAST in go using gosec

## Names and KTH ID

- Leo Vainio (lvainio@kth.se)
- Wenqi Cao (wenqic@kth.se)

## Deadline

- Task 2

## Category

- Executable Tutorial

## Description

To make the tutorial I will use Killercoda. Gosec is a security scanner for the go language which identifies common vulnerabilities. My idea is to create a mock project in go that contains some vulnerabilities and then show in the tutorial how gosec can be used to identify these vulnerabilities. I will show how gosec is installed and will give some different examples on how to use it. I might also show how it can be integrated with GitHub Actions.

**Relevance**

Detecting vulnerabilities as soon as new code is commited to the code base is great since it is often easier and cheaper to fix these issues when they are found early. Scanning the source code for known vulnerabilities, which is what gosec does, is one way to detect security issues early on. Having security integrated in the DevOps workflow also alleviates the potential bottleneck of having a completely separate security team having to review each new update, which could delay deployment.