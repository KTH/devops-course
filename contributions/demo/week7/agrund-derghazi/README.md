# Assignment Proposal

## Title

Chaos engineering: circuit breaker for a severed dependency link

## Names and KTH ID

- <Adrian Grund> (agrund@kth.se)
- <Ziyad Derghazi> (derghazi@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

We containerise a Vite/React frontend, Python backend and Elasticsearch, with
Toxiproxy between backend and Elasticsearch. We sever that link live and show the
backend's circuit breaker open, degrade gracefully, then close again on its own once
the link returns, no manual intervention. Time permitting, we contrast this with a
naive watcher that kills and respawns the backend instead, showing live that this
just loops, since the new container hits the same severed link.

**Relevance**

Covers chaos and resilience engineering (week 7 preparatory material): steady state,
injected fault, observation, rollback, at the dependency level rather than the
infrastructure level of most prior demos. The respawn comparison shows that
remediation must act on the fault's actual location, tying into monitoring and
automated operational response.