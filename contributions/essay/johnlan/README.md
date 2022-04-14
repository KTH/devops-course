# Assignment Proposal

## Title

The blasphemy of YAML and other configuration "languages"

## Names and KTH ID
  - John Landeholt (johnlan@kth.se)

## Deadline

Deadline to complete task 1: April 5, 17h Stockholm time (tomorrow)

## Category

Essay

## Description

    Note for the TA: I've forgotten to make a pull request. I've written roughly 60% of the first draft already. Please have overseight.

A evergrowing problem that new software engineers encounters firstly when they actually enter the industry is the **lack of standards**. No interface is alike. Sure, there exists some flavour that are similar or even supersets of eachother, but the environment is still vastly scattered. We all have probably seen repositories filled to the brim with weird files such as  `*.toml`, `.*rc`, `*.yaml`, `*.json`, `*.hcl`, `*.txt`, `*.config` and `Dockerfile`.

Why is this? And does there exist a long-term solution to combat this?

This essay will research this particular area of devops because it is relevant to establish a standard for configuration, preferably as code with a ecosystem built around it by the community. Much like what libraries such as React has done for the web development community.

Configuration files are extremly error prone. Especially as they are usually written manually and doesn't have any additional syntax capabilities for specific configurations (github actions, terraform, netlify, kubernetes, Docker).

Sure, you can constrain an IDE to validate keys in the case of github actions (yaml), but it doesn't constrain the actual value that is appended to the key, and thusly creates a window of uncertainty.

This level of uncertainty can be daunting, especially when it is applied to production configurations. But surely you can build something **custom** that evaluates that the config is valid, but then we are coming full circle. THERE EXISTS NO STANDARD!
