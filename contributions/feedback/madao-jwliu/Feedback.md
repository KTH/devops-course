# Feedback

Feedback for the Essay "How host-based intrusion detection systems can improve the security of CI/CD pipelines" by Löfberg and Xiong.
https://github.com/KTH/devops-course/tree/2023/contributions/essay/nilslof-taox

Feedback by Allan and Jun, @allandao and @Letuvertia respectively

I/We certify that generative AI, incl. ChatGPT, has not been used to write this feedback. Using generative AI without permission is considered academic misconduct.

Number of words: ~540

---

## Overview

We were interested in exploring and providing feedback on this particular essay in order to learn more about the specifics of the notion of host-based intrusion detection systems (HIDS), which is introduced in the essay. The issue at hand is highly relevant to DevOps and is a modern and again, relevant issue to pipelines across a diverse range of projects, teams, and organizations. With this in mind, the feedback presented will feature an exploration of the different sections of the paper, with thoughts on how it all comes together to introduce and promote technology that may be impactful to one's day-to-day work, but perhaps not something that a rather inexperienced developer knows of, emphasizing the essay's significance.

### High Level Feedback
Areas of Strengths:
- Interesting and relevant topic
- Well structured, with the introduction to CI/CD pipelines offering the baseline knowledge needed as well as definitions for key terms
- Example tool provided (actionable)
- Overall, a strong foundation

Areas of Improvement:
- Increased integration of diagrams and/or listings could be beneficial
- Slight expansion of available examples of instrusion and vulnerabilities
- Links to particular subsection references would be helpful
- More resources always appreciated

### Additional Materials
Some interesting resources that complement the information found in the paper.
- A deeper dive into OSSEC https://www.sans.org/white-papers/39565/
- More information about intrusion https://www.sans.org/white-papers/343/

### Conclusion
The essay is well written to be self-contained and informative, and again, on an interesting and relevant topics. Key ideas related to improvement are generally more particular quality of life additions, such as more visuals to offer a better idea of what the suggested tools do and look like. On this previous point, we see a key aspect of the paper: actionable steps through two different pieces of software and a recognition that the software is only complementary to other security tooling, given the analysis from the challenges and limitations mentioned. As for the course rubric, it holds to many of the required points, although the essay could be more direct in terms of the language used to express points such as how recent (sota or state of the art) the issue and discussed software is. Overall, a fun and quite a comprehensive read!

---

## A Deeper Dive
Examining each section.

### 1 Introduction
Self-contained and brief introductory statement, with clear statements on what we will examine.

We might to change "most significant companies" to "most significant projects," given how prevalent CI/CD pipelines are.

May be helpful to specify outside malicious actors

### 2 CI/CD Pipelines
Great section to self-containerize the essay. Re-emphasizing DevOps here may be helpful.

Offering more information about why untested code can lead to issues can be helpful.

### 3 Overview
Effective introduction to HIDS, but it would be helpful to re-emphasize the distinction between the two different forms of HIDS that have been in development and usage.

### 4 Benefits
Offering an example of why a HIDS make require significant ongoing work would be helpful.

"The third argument, outlined in subsection 2.2.3 entailed the fast-paced environ-
ment in which CI/CD pipelines live."

Relates to the detail of adding links that was mentioned in the overview.

### 5 Limitations and Challenges
A fair section that promotes issues both related to team culture (towards the end) and technical issues.

### 6 Conclusion
"However, they [HIDS] are not an all-encompassing solution
and should be used in conjunction with other security measures to create a
multi-layered security to the CI/CD pipeline."

It could be helpful to offer examples of other security measures to clearly indicate what HIDS is lacking. For example, if static analysis tools would be complementary.