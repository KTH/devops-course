# Assignment Proposal

## Title

Green health check, wrong model

## Names and KTH ID

  - Tomás Brito (tmldjb@kth.se)
  - Henrique Cavaco (hjcr@kth.se)

## Deadline

Week 4

## Category

Demo

## Description

A CD pipeline decides whether a new version can go live by asking whether it is healthy: does it answer, is it fast, is the response the right shape. That works for ordinary software, because ordinary software fails loudly. A model does not. It keeps answering in milliseconds, with a 200 and the right shape, and it is wrong.

Our example is a small web service that reads a customer review and says whether it is positive or negative. Two versions of it run side by side: the one currently in production, and a candidate waiting to be promoted. The candidate differs by one line of deployment config, which stops the review being lower-cased before the model sees it. The model was trained on lower-cased text, so a review written in capitals arrives as words it has never seen, and it starts guessing.

What we will show, in this order:

- The app in the browser. The same review in lower case and then in capitals gets two different answers. Everyone sees the failure.
- The pipeline on that same commit: build, five unit tests, shadow deploy and health check, all green. Everything a normal CD pipeline knows how to ask says this is ready to ship.
- A behavioural gate that replays a labelled set of reviews through both versions, sees accuracy fall from 0.96 to 0.75, and blocks the promotion before any real user reaches the candidate.
- We find the line, fix it live, push, and watch the pipeline promote.

We finish with where this runs out: the labelled set goes stale, the threshold is a judgement call rather than something you can derive, shadowing doubles the compute, and requests with side effects cannot be mirrored at all.

**Relevance**

Progressive delivery and quality gates are standard CD practice, and here we apply them to a component that is not deterministic. The failure we use, training-serving skew, is a common way models break in production. The point of the demo is that availability and correctness are different questions, and the usual health check treats them as one.
