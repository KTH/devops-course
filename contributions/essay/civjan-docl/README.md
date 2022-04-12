# Assignment Proposal

## Title

The Cold Start Problem: How container lifecycle influences serverless functions

## Names and KTH ID
  - Ben Civjan (civjan@kth.se)
  - Diego Chahuan (docl@ug.kth.se)

## Deadline

Deadline task 3

## Category

Essay

## Description

When working with the servless computing model a common problem that developers face is the cold start problem. This occurs when your preferred cloud provider needs to start your runtime container because an inactive function was called. This is highly correlated with the Docker lifecycle because it is entirely based on container startup cost, the cost of keeping a container running, and the trade offs between pausing or killing a running container (i.e Docker lifecycle).