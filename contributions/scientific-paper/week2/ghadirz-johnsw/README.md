# Assignment Proposal

## Title

Piranha: Reducing Feature Flag Debt at Uber

## Names and KTH ID

- Hossein Ghadirzadeh (ghadirz@kth.se)
- John Swärd (johnsw@kth.se)

## Deadline

- Week 2

## Category

- Scientific paper

## Description

We want to present "Piranha: Reducing Feature Flag Debt at Uber" (ICSE-SEIP 2020).

Feature flags let teams roll out new code gradually, but once a flag's outcome is decided, the branching logic around it usually just stays in the codebase as dead weight instead of getting cleaned up.

Piranha is Uber's automated tool for finding and safely refactoring away that leftover code once a flag goes stale, it parses the AST, generates a diff, and hands it to the flag's original author to review.

We'll walk through how it decides a flag is stale, how the refactoring itself works across Objective-C, Java, and Swift, and the real deployment numbers from Uber (1,381 flags cleaned up, most diffs landing without changes).

**Relevance**

Feature flags are a core CI/testing-automation practice, but they quietly create technical debt if nobody ever removes them, this paper is a concrete example of treating that cleanup as an automated part of the pipeline rather than manual chores nobody gets to. It connects directly to Week 2's theme of testing automation and continuous integration.
