# KTH DevOps Course 2026 Edition

This repository contains the material and content of the DevOps course at KTH Royal Institute of Technology [DD2482](https://www.kth.se/social/course/DD2482/).

```
$ git clone ssh://github.com/KTH/devops-course/ --branch 2026 --single-branch
```


## Schedule

The schedule is at <https://www.kth.se/social/course/DD2482/calendar/>

*If you can't see any schedule events on the HTML page*  
*Change course rounds/groups in [My settings](https://www.kth.se/social/course/DD2482/subscription/) or change the time period above so that it conforms to the course round.*

## Program

### Week 1 (26/8 13h-15h): Introduction (mandatory)
* Preparatory reading: [DevOps principles](https://www.atlassian.com/devops/what-is-devops) and [demo](https://youtu.be/qcm0rG8EKXI)
* Course introduction by Larissa Schmid (Teaching philosophy, interactive classroom, Expectations, Team, Agenda, Grading, Communication, Infrastructure, Master's theses and Research)
* Goals: watch the repo, register one first task as a pull request on this repo.
* Seminar on 28/8 (09h-12h), 03/09 (09h-12h): Open schedule - discuss your goals for the course, your planned tasks, and any other questions you may have. 

### Week 2 (2/9 13h-15h): [Testing automation](https://github.com/KTH/devops-course/issues/9), [Continuous Integration](https://github.com/KTH/devops-course/issues/3), [Feature flags](https://github.com/KTH/devops-course/issues/21)
* Preparatory material [Testing at scale](https://increment.com/testing/testing-at-scale/), [Harvesting Production GraphQL Queries to Detect Schema Faults](https://arxiv.org/pdf/2112.08267), [The Rituals of Iterations and Tests](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9238653)
* Seminar on 10/09 (15h-18h): scientific paper, demonstrations

### Week 3 (9/9 13h-15h): [Continuous Deployment / Delivery](https://github.com/KTH/devops-course/issues/12)
* Preparatory material [An Introduction to Continuous Integration, Delivery, and Deployment](https://www.digitalocean.com/community/tutorials/an-introduction-to-continuous-integration-delivery-and-deployment), [The Top 10 Adages in Continuous Deployment](https://zlmonroe.com/CSE566/Readings/5.The_Top_10_Adages_In_Continuous_Deployment.pdf)
* Seminar on 18/09 (15h-18h): scientific paper, demonstrations

### Week 4 (16/9 10h-12h): [MLOps/AIOps/LLMOps](https://github.com/KTH/devops-course/issues/1016)
* Preparatory material: [Short intro to MLOps](https://www.databricks.com/glossary/mlops), [Building Machine Learning Models Like Open Source Software](https://cacm.acm.org/magazines/2023/2/268952-building-machine-learning-models-like-open-source-software/fulltext)
* Seminar on 25/09 (15h-18h): scientific paper, demonstrations


### Week 5 (23/9 13h-15h): [Infrastructure as Code](https://github.com/KTH/devops-course/issues/2)
* Preparatory material: [Best practices for container compliance](https://increment.com/containers/container-compliance/), [Building on-demand staging environments](https://increment.com/containers/on-demand-staging-environments-kubernetes/), [Gang of eight: a defect taxonomy for infrastructure as code scripts](http://www.chrisparnin.me/pdf/GangOfEight.pdf)
* Seminar on 30/09 (09h-12h): scientific paper, demonstrations


### Week 6 (29/9 13h-15h): [Dependency Management](https://github.com/KTH/devops-course/issues/24) & [DevSecOps](https://github.com/KTH/devops-course/issues/18)
* Preparatory material: [A 'Worst Nightmare' Cyberattack: The Untold Story Of The SolarWinds Hack](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack), [The supply chain of software](https://increment.com/apis/apis-supply-chain-software/), [Successes, challenges, and wombat behind npm](https://increment.com/development/interview-with-isaac-z-schlueter-ceo-of-npm/), [A comprehensive study of bloated dependencies in the Maven ecosystem ](https://arxiv.org/pdf/2001.07808)
* Seminar on 08/10 (09h-12h): scientific paper, demonstrations


### Week 7 (7/10 13h-15h): Other topics
* incl. [Monitoring and Observability](https://github.com/KTH/devops-course/issues/8), [cultural aspects](https://github.com/KTH/devops-course/issues/7) and [legal aspects](https://github.com/KTH/devops-course/issues/1557), [Software bots](https://github.com/KTH/devops-course/issues/310), , [Misc DevOps topics](https://github.com/KTH/devops-course/issues/13)
* Preparatory material [Chaos Engineering](https://ieeexplore.ieee.org/iel7/52/5204063/07436642.pdf) [A Chaos Engineering System for Live Analysis and Falsification of Exception-handling in the JVM](http://arxiv.org/pdf/1805.05246) 
* Seminar on 12/10 (13h-16h), 14/10 (13h-16h): scientific paper, demonstrations


## Rules


To pass the course, the student has to complete and pass between 3 and 5 tasks:
* The tasks are in category: "[demo (mandatory)](https://github.com/KTH/devops-course/blob/2026/grading-criteria.md#demos)", "[scientific paper](https://github.com/KTH/devops-course/blob/2026/grading-criteria.md#scientific-papers)", "[executable tutorial](https://github.com/KTH/devops-course/blob/2026/grading-criteria.md#executable-tutorials)", "[contribution to open-source](https://github.com/KTH/devops-course/blob/2026/grading-criteria.md#open-source-contributions)", "[feedback](https://github.com/KTH/devops-course/blob/2026/grading-criteria.md#feedback)",  "[project](https://github.com/KTH/devops-course/blob/2026/grading-criteria.md#project)" (project and demo are mandatory, at most one in the same category, it is not necessary to cover everything).
* The [grading criteria page](grading-criteria.md) is the unique reference which explains how to pass each task category.
* The student proposes a category and a topic, which is discussed and accepted by the TA. The proposal is made as a [structured pull-request](https://github.com/KTH/devops-course/blob/2026/.github/pull_request_template.md) on this repository. The 3-5 graded contributions must have little overlap.
* The same student cannot choose the same topic for two different tasks. The 3-5 tasks should cover different aspects of DevOps.
* Deadlines:
  * Deadline for demos and paper presentations: the day and time they are given in person
  * Deadline for tutorial and opensource: Sep 24, 23h59 Stockholm time
  * Deadline for project: Oct 10, 23h59 Stockholm time
  * Deadline for repeated tasks (all): Oct 27 2026, 17h Stockholm time.
  * Deadline for feedback on tasks: 2 business days after the "go" from the authors
  * Hand-in your async tasks via a new PR that updates your proposal document with a link to the artifact/contribution/feedback
  * The deadlines are strict and cannot be extended. Not meeting a deadline means failing the task / the repetition.
* Final grading scheme
  * E: 3 completed tasks (excluding feedback)
  * C: 3 completed tasks + feedback
  * B: 5 completed tasks
  * A: 5 completed tasks + active participation in all but one seminars
* Active participation: attendance to all but one seminars between 10/09 and 14/10, a traceable record of questions asked during seminars (through GitHub issues) and the answers you received to them.
* Group work is mandatory (max 2 persons) but you cannot be with the same person for more than 2 individual tasks. You are not allowed to work alone. When you send a pull request for registration, please follow the name convention of using email addresses of two members to create the folder: email-email.
* A failed task requires to pass it again at the end of the course (repeat), based on the feedback from the failure. A task can only be repeated once.
* If the whole course is failed, no grades are kept if the student registers again to the course the year after. 
* After a proposal has been merged, the topic of that proposal cannot be changed.


## Communication

* All communication for the course DD2482 should be sent to <dd2482@eecs.kth.se>.
* you create issues here if you think the question is good to be discussed publicly, the rules of [netiquette](https://en.wikipedia.org/wiki/Etiquette_in_technology) fully apply.

## Participation

**Lectures** The lectures are held on campus (no hybrid / no video link). The lecture locations are given on KTH Social <https://www.kth.se/social/course/DD2482/calendar/>. The first lecture is mandatory, the other ones are strongly encouraged.

**Seminar sessions**

* Seminar slots are used to present and discuss the "demo" and "scientific paper" tasks. They are given in person and correspond to the weekly topics as outlined in the schedule. 
* Seminar slots are not mandatory, but you have to be present to present the tasks you proposed. 
* Active participation (and therefore attendance) in all but one seminars between 10/09 and 14/10, covering the topics of weeks 2 to 7, is required if you are aiming for an A. 

**Examinations**: Some tasks require physical presence (demo, scientific paper), others do not (project, open-source, feedback).

## Team

* [Dr Larissa Schmid](https://www.kth.se/profile/lgschmid?l=sv) (Teacher)
* [Dr Carmine Cesarano](https://www.kth.se/profile/cesarano) (TA)
* [Frank Reyes](https://www.kth.se/profile/frankrg) (TA)
* [Eric Cornelissen](https://www.kth.se/profile/ericco) (TA)
* [Aman Sharma](https://www.kth.se/profile/amansha) (TA)
* [Prof. Martin Monperrus](http://www.monperrus.net/martin/) (Examiner)


## Prerequisites

* A software engineering course (eg [DD2480](https://www.kth.se/student/kurser/kurs/DD2480))
* A networking course (eg [IK2218](https://www.kth.se/student/kurser/kurs/IK2218?l=en))

## See also

* KTH Social URL: <https://www.kth.se/social/course/DD2482/>
* Kopps URL: <https://www.kth.se/student/kurser/kurs/DD2482?l=en>
* Past editions:
  * [KTH DevOps Course 2019](https://github.com/KTH/devops-course/blob/2019/)
  * [KTH DevOps Course 2020](https://github.com/KTH/devops-course/blob/2020/)
  * [KTH DevOps Course 2021](https://github.com/KTH/devops-course/blob/2021/)
  * [KTH DevOps Course 2022](https://github.com/KTH/devops-course/blob/2022/)
  * [KTH DevOps Course 2023](https://github.com/KTH/devops-course/blob/2023/)
  * [KTH DevOps Course 2024](https://github.com/KTH/devops-course/blob/2024/)
  * [KTH DevOps Course 2025](https://github.com/KTH/devops-course/blob/2025/)



