# Monitoring availability using Cloudprobe and Prometheus

## Members

Martijn Atema, atema@kth.se, GitHub: Atema
Simon Persson, siper@kth.se, GitHub: altaired

## Proposal

After building software that users depend on every day it becomes clear that uptime and response times are very important measures to always keep track of. We need to be able to respond quickly when something goes wrong, and want to know when an endpoint doesn't work; preferably before the user even notices. There are some paid, closed-source tools that achieve this, but there's very few self-hosted, open-source alternatives.

[Cloudprober](https://cloudprober.org) is a good option; it is an open-source monitoring tool that makes it easy to monitor availability and performance of applications. In this demo we will show how to setup Cloudprober to monitor an API and then display the data in [Prometheus](https://prometheus.io).


## Submission
We've now completed the demo, it consists of a 3:00 minute youtube video that can be found [here](https://www.youtube.com/watch?v=o1ITz06dd2A) and an accompanying github repository [here](https://github.com/Atema/Cloudprober-Demo) that includes written instructions as well as all the configuration files used in the demo. With it we aim to fulfill the following criterias:

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The demonstration is clearly motivated (why it matters for Devops?) | 🔥 Yes | No | Relates to a hard problem |
|The demonstration is difficult to do | 🔥 Yes | No | Relies on a non trivial infrastructure |
|The demonstration is original | Yes | No | 🔥 The are less than 10 demos on the topic on Internet |
|The video is sublime (eg visually appealing) | 🔥 Yes | No | Excellent narrative |
|The video contains an [easter egg](https://github.com/OrkoHunter/python-easter-eggs) | Yes | No | 🔥 Related to the demo |
|There is a code repo to run the demo  | Yes | No | 🔥 Code repo with a solid readme |
|The video must contain subtitles which are clear and in proper English | Yes | No | 🔥 Clearly understandable voice over |
|The video includes a take-home message | Yes | No | 🔥 Actionable takeaway |

## Feedback

From the feedback given as part of the demo day we've improved the following:

* Rephrased a part of the introduction to make it more clear what the demo is about

* We’ve added a proper title and description for the video, hopefully making it clearer what the video is about.

* We’ve done our best to slow down the introduction part, as some of you thought it was a bit rushed.

* We’ve clarified in the description why we have 4 probes (The DNS probe is simply there to demonstrate how to use a DNS probe too) and also that there are other ways than using docker images to use cloudprober and Prometheus.

* We’ve clarified in the video that there is an accompanying GitHub repository, with more details and all code.

* We’ve unfortunately not been able to fix a better microphone, we used the best mic we have available. We’ve tried to improve it when editing and hope it’s a little bit better.


