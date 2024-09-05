# KTH DevOps Course

This repository contains the material and content of the DevOps course at KTH Royal Institute of Technology [DD2482](https://www.kth.se/social/course/DD2482/).

## Schedule

The schedule is at <https://www.kth.se/social/course/DD2482/calendar/>

*If you can't see any schedule events on the HTML page*  
*Change course rounds/groups in [My settings](https://www.kth.se/social/course/DD2482/subscription/) or change the time period above so that it conforms to the course round.*

## Program

### Week 1: Introduction (mandatory)
* Preparatory reading: [DevOps principles](https://www.atlassian.com/devops/what-is-devops) and [demo](https://youtu.be/qcm0rG8EKXI)
* Course introduction [Martin Monperrus](https://www.monperrus.net/martin/) (Teaching philosophy, [flipped classroom](https://en.wikipedia.org/wiki/Flipped_classroom), Expectations, Team, Agenda, Grading, Communication, Infrastructure, Master's theses and Research)
* Goals: watch the repo, register one first task as a pull request on this repo.

### Week 2: [Testing automation](https://github.com/KTH/devops-course/issues/9), [Continuous Integration](https://github.com/KTH/devops-course/issues/3), [Feature flags](https://github.com/KTH/devops-course/issues/21)
* Preparatory material [Testing at scale](https://increment.com/testing/testing-at-scale/), [Harvesting Production GraphQL Queries to Detect Schema Faults](https://arxiv.org/pdf/2112.08267), [The Rituals of Iterations and Tests](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9238653)
* Student presentations, demonstrations

### Week 3: [Continuous Deployment / Delivery](https://github.com/KTH/devops-course/issues/12)
* Preparatory material [An Introduction to Continuous Integration, Delivery, and Deployment](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment), [The Top 10 Adages in Continuous Deployment](https://zlmonroe.com/CSE566/Readings/5.The_Top_10_Adages_In_Continuous_Deployment.pdf)
* Student presentations, demonstrations

### Week 4: [MLOps/AIOps/LLMOps](https://github.com/KTH/devops-course/issues/1016)
* Preparatory material: [Short intro to MLOps](https://www.databricks.com/glossary/mlops), [Building Machine Learning Models Like Open Source Software](https://cacm.acm.org/magazines/2023/2/268952-building-machine-learning-models-like-open-source-software/fulltext), [What is A/B testing?](https://medium.com/is-that-product-management/what-is-a-b-testing-bc964ecd99b4)
* Student presentations, demonstrations


### Week 5: [Infrastructure as Code](https://github.com/KTH/devops-course/issues/2)
* Preparatory material: [Best practices for container compliance](https://increment.com/containers/container-compliance/), [Building on-demand staging environments](https://increment.com/containers/on-demand-staging-environments-kubernetes/), [Gang of eight: a defect taxonomy for infrastructure as code scripts](http://www.chrisparnin.me/pdf/GangOfEight.pdf)
* Student presentations, demonstrations


### Week 6: [Dependency Management](https://github.com/KTH/devops-course/issues/24) & [DevSecOps](https://github.com/KTH/devops-course/issues/18)
* Preparatory material: [A 'Worst Nightmare' Cyberattack: The Untold Story Of The SolarWinds Hack](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack), [The supply chain of software](https://increment.com/apis/apis-supply-chain-software/), [Successes, challenges, and wombat behind npm](https://increment.com/development/interview-with-isaac-z-schlueter-ceo-of-npm/), [A comprehensive study of bloated dependencies in the Maven ecosystem ](https://arxiv.org/pdf/2001.07808)
* Student presentations, demonstrations


### Week 7: Other topics
* incl. [Monitoring and Observability](https://github.com/KTH/devops-course/issues/8), [cultural aspects](https://github.com/KTH/devops-course/issues/7) and [legal aspects](https://github.com/KTH/devops-course/issues/1557), [Software bots](https://github.com/KTH/devops-course/issues/310), , [Misc DevOps topics](https://github.com/KTH/devops-course/issues/13)
* Preparatory material [Chaos Engineering](https://ieeexplore.ieee.org/iel7/52/5204063/07436642.pdf) [A Chaos Engineering System for Live Analysis and Falsification of Exception-handling in the JVM](http://arxiv.org/pdf/1805.05246) 
* Student presentations, demonstrations


## Rules


To pass the course, the student has to complete and pass between 3 and 5 tasks:
* The tasks are in category: "[presentation (mandatory)](https://github.com/KTH/devops-course/blob/2024/grading-criteria.md#presentations)", "[demo (mandatory)](https://github.com/KTH/devops-course/blob/2024/grading-criteria.md#demos)", "[scientific paper](https://github.com/KTH/devops-course/blob/2024/grading-criteria.paper)", "[executable tutorial](https://github.com/KTH/devops-course/blob/2024/grading-criteria.md#executable-tutorials)", "[contribution to open-source](https://github.com/KTH/devops-course/blob/2024/grading-criteria.md#open-source-contributions)", "[feedback](https://github.com/KTH/devops-course/blob/2024/grading-criteria.md#feedback)" (presentation and demos are mandatory, at most one in the same category, it is not necessary to cover everything).
* The [grading criteria page](grading-criteria.md) is the unique reference which explains how to pass each task category.
* The student proposes a category and a topic, which is discussed and accepted by the TA. The proposal is made as a [structured pull-request](https://github.com/KTH/devops-course/blob/2024/.github/pull_request_template.md) on this repository. The 3-5 graded contributions must have little overlap.
* The same student cannot choose the same topic for two different tasks. The 3-5 tasks should cover different aspects of DevOps.
* Deadlines:
  * Deadline for presentations, demos, paper: the day and time they are given in person
  * Deadline 1 for async tasks: Oct 1 2024, 17h Stockholm time
  * Deadline 2 for async tasks: Oct 8 2024, 17h Stockholm time
  * Deadline 3 for async tasks: Oct 15 2024, 17h Stockholm time
  * Deadline for feedback on async tasks: 48 hours after delivery for a given deadline
  * Deadline for repeated tasks (all): **Nov 5 2024, 17h Stockholm time**.
  * The deadlines are strict and cannot be extended. Not meeting a deadline means failing the task / the repetition.
* Final grading scheme
  * E: 3 completed tasks (excluding feedback)
  * C: 4 completed tasks 
  * B: 5 completed tasks 
  * A: 5 completed tasks + active participation in all but one lectures
* Active participation: attendance to all but one lectures, a traceable record of questions asked during lectures (through GitHub issues) and the answers you received to them.
* Group work is encouraged (max 2 persons) but you cannot be with the same person for more than 2 individual tasks. As a general rule, you are not allowed to work alone.
* A failed task requires to pass it again at the end of the course (repeat), based on the feedback from the failure. A task can only be repeated once.
* If the whole course is failed, no grades are kept if the student registers again to the course the year after. 
* After a proposal has been merged, the topic of that proposal cannot be changed.

Group Rules
* When you send a pull request for registration, please follow the name convention of using email addresses of two members to create the folder: email-email.
* We recommend 2 students. Three is also possible for ambitious demos or contribution to open-source.

## Communication

* All communication for the course DD2482 should be sent to <dd2482@eecs.kth.se>.
* you create issues here if you think the question is good to be discussed publicly, the rules of [netiquette](https://en.wikipedia.org/wiki/Etiquette_in_technology) fully apply.

## Participation

**Lectures** The lectures are held on campus (no hybrid / no video link). The lecture locations are given on KTH Social <https://www.kth.se/social/course/DD2482/calendar/>. The first lecture is mandatory, the other ones are strongly encouraged.

**Lab sessions**

* Lab slots are not mandatory. They are given in person (preferably) or videoconf.
* During the planned lab time slot, please use this [Queue](https://queue.csc.kth.se/Queue/DD2482) for booking online meetings
* Specify your zoom meeting link when you register the queue

**Examinations**: Some tasks require physical presence (presentation, demo, scientific paper), others do not (open-source, feedback).

## Team

* [Prof. Martin Monperrus](http://www.monperrus.net/martin/) (Examiner)
* [Javier Ron](https://www.kth.se/profile/javierro?l=en) (TA)
* [Deepika Tiwari](https://www.kth.se/profile/deepikat) (TA)
* [Sofia Bobadilla](https://www.kth.se/profile/sofbob) (TA)
* [Aman Sharma](https://www.kth.se/profile/amansha) (TA)


## Prerequisites

* A software engineering course (eg [DD2480](https://www.kth.se/student/kurser/kurs/DD2480))
* A networking course (eg [IK2218](https://www.kth.se/student/kurser/kurs/IK2218?l=en))

## See also

* KTH Social URL: <https://www.kth.se/social/course/DD2482/>
* Kopps URL: <https://www.kth.se/student/kurser/kurs/DD2482?l=en>
* Past editions:
  * [KTH DevOps Course 2019](https://github.com/KTH/devops-course/blob/master/attic/2019/)
  * [KTH DevOps Course 2020](https://github.com/KTH/devops-course/blob/master/attic/2020/)
  * [KTH DevOps Course 2021](https://github.com/KTH/devops-course/blob/master/attic/2021/)
  * [KTH DevOps Course 2022](https://github.com/KTH/devops-course/blob/master/attic/2022/)
  * [KTH DevOps Course 2023](https://github.com/KTH/devops-course/blob/master/attic/2023/)



