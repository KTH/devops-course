# Assignment Proposal

## Title
Contribute to the Rust implementation of Apache Arrow

## Names and KTH ID
  - Jonathan Arns (jarns@kth.se)

## Deadline
- Task 2

## Category
- Open source

## Description

Apache Arrow is a multilanguage data format and processing library with implementations in many languages.
The contribution would be to either implement a small new feature, like a new processing kernel for a specific
data-transformation or a bug-fix in the [arrow-rs][https://github.com/apache/arrow-rs] codebase, as well as testing
the proposed changes.


Example issues:
https://github.com/apache/arrow-rs/issues/3963
https://github.com/apache/arrow-rs/issues/3969

**Relevance**

While it first and foremost targets the big data community, I still think there
is relevant overlap, specifically in (real-time) monitoring systems, where Arrow is used under the hood.
For example, Apache Arrow is used heavily
by InfluxDB, a leading timeseries database with clear devops use-cases for monitoring and metrics data.
