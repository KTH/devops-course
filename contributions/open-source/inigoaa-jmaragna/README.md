# Assignment Proposal

## Title

_--enable-feature: Consider removing no-default-scrape-port_

## Names and KTH ID

  - Jacopo Maragna (jmaragna@kth.se)
  - Íñigo Aréjula Aísa (inigoaa@kth.se)

## Deadline

- Task 3 

## Category

- open-source

## Description

Prometheus has different features available. However, some of them are not immediately available by default, but they can be enabled using flags. What the community is requesting is to enable some of these features by default. What we are proposing to do is to take this [issue](https://github.com/prometheus/prometheus/issues/13959) and resolve the problem.

Now, an outline of the various tasks we aim to solve:
1. Understand the project architecture and source code.
2. Set up the environment and run the project/tests.
3. Tackle the problem itself:
    - By default, we want the `no-default-scrape-port` feature to be enabled.
    - Add the possibility to disable it on demand.
    - Update the documentation.

**Relevance**

Prometheus is crucial in DevOps for its ability to monitor (Week 7) and analyze system performance in real-time. It helps teams collect metrics, set alerts, and automate responses, ensuring system reliability and quick incident resolution. This enhances the core DevOps practices of continuous integration, deployment, and collaboration.

Link: https://github.com/prometheus/prometheus/pull/14958

## Done
### Finding the task

We decided to contribute to an open-source project relevant to our DevOps course and chose Prometheus. After reaching out to maintainers through the Cloud Native Computing Foundation Slack, they recommended we start with this issue: https://github.com/prometheus/prometheus/issues/13959, which is detailed in the above section of the file. We reviewed the discussion under the issue, gaining a solid understanding of the problem and proposed solutions. After expressing our interest in tackling the issue and seeking additional guidance, one of the maintainers suggested we look at this abandoned pull request for inspiration: https://github.com/prometheus/prometheus/pull/14160. With that input, we began working on the issue.

### Understanding the project architecture and source code
### Development
### Final issue

After completing all the necessary changes and ensuring our code passed all tests, we submitted a pull request (PR) to Prometheus: https://github.com/prometheus/prometheus/pull/14958. While all tests were successful, we awaited approval from the maintainers. Although this was marked as a first issue, the changes we proposed could have broken the current v3 logic. As a result, the maintainers discussed how to smoothly integrate the new behavior into future versions.

However, after a few days of discussion, an unexpected situation arose. The original author of the previous, abandoned PR (which we had used for reference) suddenly reappeared and submitted changes after four months of inactivity. The maintainers, seemingly unaware of our prior conversations and the rationale behind our PR, questioned why we had submitted it, given its similarity to the older one. Despite the potential for our PR to be merged, they ultimately decided to close it and prioritize the original PR.

We eventually clarified the situation with the maintainers, and they acknowledged the confusion. They recognized that our PR had been submitted in good faith following earlier discussions and the guidance we received.

### Conclusion

Overall, this process has been a valuable experience for us in understanding a large open-source codebase. We learned how to identify important issues and explore how new solutions can be integrated into future versions. Contributing, even in a small way, to such a significant project was highly rewarding. Although the unexpected situation at the end was unfortunate, we successfully identified a good first issue, engaged with the maintainers, studied the project in depth, developed our solution, and opened a PR. The entire experience has been a great learning opportunity.
