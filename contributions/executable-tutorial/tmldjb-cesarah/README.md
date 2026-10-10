# Assignment Proposal

## Title

Safe Database Migrations in Continuous Delivery: Migration Linting and the Expand/Contract Pattern

## Names and KTH ID

- Tomás Brito (tmldjb@kth.se)
- Cesar Aceves Hernández (cesarah@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We will create an executable tutorial on Killercoda about changing a database schema without breaking a running application. Code changes are easy to roll back, schema changes are not, and during a rolling deploy the old and the new version of an app run against the same database at the same time.

The tutorial starts from a small web service backed by PostgreSQL, with traffic running against it. First, the learner applies a naive migration (renaming a column) with dbmate and watches the old version of the service start failing. Then they add squawk, a linter for PostgreSQL migrations, as a check in a small CI script, and see it block the same migration before it reaches the database. Finally, they redo the change with the expand/contract pattern: add the new column with a trigger that keeps both columns in sync, backfill it, roll out the new version, and only drop the old one once nothing reads it anymore. A last step shows the difference between a normal index build, which blocks writes, and `CREATE INDEX CONCURRENTLY`.

Everything runs in the browser with pinned versions and no accounts. Each step has a check script, and the tutorial includes an architecture diagram and a reflection on when this approach is worth the extra steps and when it is not.

**Relevance**

Continuous delivery assumes that any commit can be deployed safely, but database migrations are often the part that still needs a maintenance window. Zero-downtime deploys require the schema to work with two versions of the application at once, which is the same problem canary and blue-green releases deal with. Checking migrations automatically in CI is a shift-left practice that turns knowledge about locks and breaking changes into a repeatable gate.

**Link to tutorial**

- Tutorial on Killercoda: https://killercoda.com/tomasmbrito/scenario/safe-db-migrations
- Source code: https://github.com/tomasmbrito/safe-db-migrations-tutorial
