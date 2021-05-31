# Tutorial submission: Automated monitoring/analytics with ELK Stack

## Members:

Andreas Kärrby (karrby@kth.se)
Github: [andreaskth](https://github.com/andreaskth)

Henrik Kultala (kultala@kth.se)
Github: [hengque](https://github.com/hengque)

## Proposal/motivation

Original proposal PR is #1251 

## Submission

The Katacoda-scenario can be found at: https://www.katacoda.com/kthandreas

*(Sometimes it seems Katacoda is more responsive when adding `!` as a fragment ID, so you could try using [this link](https://www.katacoda.com/kthandreas/scenarios/elk-analytics/#!) if it is lagging above)*

The repo for the scenario can be found here: https://github.com/hengque/elk-analytics-katacoda-tutorial 


## What we did

- Created a Katacoda scenario utilizing various built in features to ease the user’s interaction with the material.
  - Katacoda-syntax for opening files in the editor automatically
  - Katacoda-syntax to ensure commands are executed in the correct terminal
  - Predefined named Katacoda-tabs to make tabs easier to tell apart
- Extended a [basic Java Spring application](https://github.com/spring-guides/gs-serving-web-content) (forked version [here](https://github.com/andreaskth/gs-serving-web-content)) with logging and provided it in the tutorial to allow the users to interactively create logs. The users can handle the log implementation like a black box, or – should they choose to – they can explore the repo on their own to understand the “Java logging”-part as well.
- Consistently included links to extra material for users interested in learning more (this was usually done in collapsible "aside-like" boxes, to not distract the reader from the main flow of the tutorial)
- Explained the three technologies that make up the acronym ELK (Elasticsearch, Logstash and Kibana): what their purposes are, how they interact, how to use them, and how to set them up.
- Provided a brief motivation for why log management tools like ELK are beneficial (especially in distributed settings such as microservices)
- Showcased a couple of metrics one might want to log and how one might visualize them

## Grading criteria we are aiming for

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) | Yes | No | In the browser 🍯 |
|If local execution, runs on Linux | Yes 🍯 | No | Easy to setup and run |
|The tutorial gives enough background | Yes | No | Comprehensive background 🍯  |
|The tutorial is easy to follow  | Yes | No | Well documented 🍯 |
|The tutorial is original, no such tutorial exists on the web | Yes 🍯 | No | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | Yes 🍯 | No | Subtle and fun |
|The tutorial is successful (attracts comments and success) | Yes | No | Lively discussion |
|The language is correct | Yes | No | Interesting narrative 🍯  |
