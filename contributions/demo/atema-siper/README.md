# Monitoring availability using Cloudprobe and Prometheus

## Members

Martijn Atema, atema@kth.se, GitHub: Atema
Simon Persson, siper@kth.se, GitHub: altaired

## Proposal

After building software that users depend on every day it becomes clear that uptime and response times are very important measures to always keep track of. We need to be able to respond quickly when something goes wrong, and want to know when an endpoint doesn't work; preferably before the user even notices. There are some paid, closed-source tools that achieve this, but there's very few self-hosted, open-source alternatives.

[Cloudprober](https://cloudprober.org) is a good option; it is an open-source monitoring tool that makes it easy to monitor availability and performance of applications. In this demo we will show how to setup Cloudprober to monitor an API and then display the data in [Prometheus](https://prometheus.io).
