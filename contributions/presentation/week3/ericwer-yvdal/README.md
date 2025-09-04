# Assignment Proposal

## Title

The power of canary releases in CD pipelines: Monitoring and Rollback

## Names and KTH ID

- Eric Wernström (ericwer@kth.se)
- August Yvdal (yvdal@kth.se)

## Deadline

- Week 3

## Category

- Presentation

## Description

We wish to present the process of automated rollback in CD pipelines with canary releases, focusing on how canary releases can help with validating the stability of new versions in production environments. A canary release is a deployment strategy where a new version is released to only a subset of users, by redirecting their traffic away from the current stable version to a “beta release”. Data like error rates and latency can be collected from the canary release, giving the development team an image of how the version performs under real pressure. The presentation will cover the process of collecting data on the canary, the benefits and downsides of this strategy, and what happens when the canary release is not stable enough. For this, we will bring up the example of such a setup using Prometheus as a monitoring tool, and Kubernetes/Flagger as a method of version rollback.

**Relevance**

Despite CI/CD pipelines often having extensive test suites, it is not guaranteed that said tests are up-to-date and able to catch everything which may go wrong when a change is deployed to production. By using canary releases the production/operations and developer teams get to analyze how new releases work on live users. Automated test suites catch many issues before release but they cannot fully replicate real world conditions. Automated rollback mechanisms, as seen with tools like Prometheus and Flagger in Kubernetes, ensure that if a canary underperforms, the system can quickly return to a stable state without manual intervention. This lines up with principles of DevOps like automation and fast feedback.
