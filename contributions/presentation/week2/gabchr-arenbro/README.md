# Assignment Proposal

## Title

Introducing MemLab for automated memory leak detection in JavaScript applications

## Names and KTH ID

  - Gabriel Christensson (gabchr@kth.se)
  - Martin Arenbro (arenbro@kth.se)

## Deadline

Week 2

## Category

Presentation

## Description

Memory leaks are generally associated programming languages that require manual memory management such as C and C++. For this reason, memory leak testing is commonly overlooked when developing applications in garbage collected languages. However, some types of memory leaks can still occur and may be difficult to spot during development, especially when not looking for them.

Last year, Facebook/Meta released a framework called MemLab for detecting JavaScript memory leaks in web applications. The tool has great potential for helping developers boost their application's performance and user experience by increasing page responsiveness and interaction speed. 

**Relevance**

MemLab is a very recent tool that enables automated testing of applications' memory performance. The tool can be integrated into CI pipelines with ease, and find performance related issues that traditional testing frameworks may not be able to find.