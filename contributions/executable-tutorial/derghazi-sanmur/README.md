# Assignment Proposal

## Title

Safe Releases with Progressive Delivery on Kubernetes: Health Checks, Rollback, and Their Limits

## Names and KTH ID

- Ziyad Derghazi (derghazi@kth.se)
- Sangeetha Murugesan (sanmur@kth.se)

## Deadline

- task 3

## Category

- Executable tutorial

## Description

We will build an executable tutorial on Killercoda that shows how a release can be rolled out gradually and stopped automatically when the new version is broken.
The reader starts with version 1 of a small Flask application backed by Redis, running with three replicas behind a Kubernetes Service. The app has a `/healthz` endpoint that pings Redis and returns 503 if it can't reach it, and a `/` route that increments and returns a counter stored in Redis.
The reader first rolls out a working version 2 and watches traffic switch over cleanly, with the Service always answering. Then the reader rolls out version 3, which points at the wrong Redis service. Its `/healthz` check fails, the new pods never become ready, and the rollout stalls while users keep getting version 2 the whole time. The reader inspects why the rollout stalled, rolls back manually with `kubectl rollout undo`, and then automates the same behaviour with a release script that applies a manifest, waits for the rollout to succeed within a time limit, and rolls back automatically if it does not.
Next, the reader deploys a version 4 that passes `/healthz` (Redis is fine) but whose `/` route is broken for an unrelated reason. This shows that a readiness check only tests what it is told to test, and that a rollout can succeed while the application is still broken.
Finally, the reader compares the same broken rollout under two rollout strategies: the default rolling update and one with `maxUnavailable: 0`. This shows the trade-off between rolling out fast and staying at full capacity throughout the release.

The tutorial ends with a reflection on what readiness checks can and cannot catch, and on when a team would need a canary or blue-green release with metrics-based analysis instead of a plain rolling update.

**Relevance**

This tutorial belongs to the Continuous Delivery topic. A release should not depend on someone watching it and hoping nothing goes wrong. With rolling updates and readiness probes, the platform itself decides whether a new version may receive traffic, and an automated rollback limits the damage of a bad release before a person has to react. The tutorial also shows the limits of this approach: a readiness probe is only as good as what it checks, and rollout speed can be traded against capacity. It focuses on how a release reaches users and how a bad one is stopped, which is a different part of DevOps from our earlier tasks.