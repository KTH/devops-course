# Grading Criteria of the KTH Devops Course

- We are all aware that assessment may be subjective in nature. In case of disagreement, the informed judgment of the professor is the final decision.
- Project and demo are mandatory tasks to pass the course.
- In case of a task failure, the students receive feedback and instructions for repetition through Canvas 

## Project 

In this project, you will design and implement a software system that demonstrates core DevOps practices in an integrated workflow. You are expected to justify your technical choices, demonstrate how the different components interact, and reflect on the strengths and limitations of your solution.


The goal is not to build a large system, but to implement a coherent, working DevOps pipeline that you understand and can explain. You can choose freely which domain the project should be in and which tools you would like to use for implementing it.

To pass, the project must demonstrate:
* Automated build and testing (CI pipeline)
* Automated deployment or delivery (CD pipeline)
* Infrastructure configuration (Infrastructure as Code)
* Use of a modern development platform (e.g., GitHub/GitLab)
* At least one quality or security automation (e.g., static analysis, dependency bots, secret scanning)
* Documented use (or critical discussion) of AI-assisted tools (e.g., AI code review)

The different parts need to be coherently integrated and function together as a system.

Deliverables:
1. Project repository: A fully functional implementation including all configuration, code, and documentation needed to run the system.
2. Short report (2-3 pages) that should:
    1. Explain the system architecture wrt to the features that must be demonstrated.
    2. Justify key design decisions (structure, tools)
    3. Describe how the components interact
    4. Reflect on limitations and trade-offs
3. Optional presentation: Selected projects may be invited to present their system and demonstrate key aspects of the workflow.

## Demos


The concept: Students prepare a demonstration involving DevOps technology, to be performed during the lecture. For example, a demo typically involves multiple virtual machines, likely deployed in the cloud. A demonstration is scripted, prepared and lasts 6:30-7:30 minutes.

| Category | Criterion | Description | Requirement |
|----------|----------|-------------|-------------|
| Technical Implementation | Technical Depth | Students demonstrate a non-trivial DevOps workflow involving multiple interacting components, integrations, or automation steps. | Yes/No |
| Technical Implementation | Liveness | Students demonstrate that they can interact and experiment live with their tooling (e.g., modifying, debugging, or extending it). | Yes/No |
| Conceptual Understanding | System Reasoning | Students explain the system architecture and how components interact. | Yes/No |
| Conceptual Understanding | Relevance | Students argue how their demo reflects DevOps concepts and practices. | Yes/No |
| Critical Thinking | Design Decisions | Students justify their choice of tools, architecture, and configuration based on DevOps principles. | Yes/No |
| Critical Thinking | Reflection | Students judge when the demo is useful, when it is not, and identify its limitations. | Yes/No |
| Communication | Narrative | The demo follows a clear structure: problem → solution → implications. | Yes/No |
| Communication | Speech | Speech is clear, understandable, and well-paced. | Yes/No |
| Communication | Timing | Demo duration is between 6:30–7:30 minutes (hard limit). | Mandatory |


## Scientific Papers


The concept: The students prepare a 7 minute presentation on one scientific paper related to DevOps. Papers must be published in the main proceedings of [software engineering](https://scholar.google.com/citations?view_op=top_venues&hl=en&vq=eng_softwaresystems) or [computer security](https://scholar.google.com/citations?view_op=top_venues&hl=en&vq=eng_computersecuritycryptography) venues. 

| Category | Criterion | Description | Requirement |
|----------|----------|-------------|-------------|
| Conceptual Understanding | Relevance | Students relate the paper to DevOps concepts and practices. | Yes/No |
| Conceptual Understanding | Conceptual Explanation | Students explain the main idea, problem, and contribution of the paper clearly. | Yes/No |
| Conceptual Understanding | Technical analysis | Students analyze and explain a key technical component (e.g., algorithm, system design) in detail | Yes/No |
| Critical Thinking | Critical | Students critique the paper by identifying limitations, assumptions, or threats to validity. | Yes/No |
| Critical Thinking | Related Work | Students differentiate and relate the paper to alternative approaches (min. 2 related papers not in the bibliography). | Yes/No |
| Critical Thinking | Reflection | Students judge in which cases the presented approach is useful, when it is not, and for whom. | Yes/No |
| Communication | Narrative and Slides | The presentation follows a clear structure from problem → approach → results → implications, with slides supporting understanding by using appropriate visualization, clarifying structure, and limited amount of text. | Yes/No |
| Communication | Speech | Speech is clear, understandable, and well-paced. | Yes/No |
| Communication | Timing | Presentation duration is between 6:30–7:30 minutes (hard limit). | Mandatory | 

## Executable Tutorial 


The concept: you create an executable tutorial about a specific technology related to Devops. You deliver your tutorial on an online platform supporting execution, such as [KillerKoda](https://killercoda.com/), [mybinder.org](https://mybinder.org/), [collab](https://colab.research.google.com/) or equivalent.

| Category | Criterion | Description | Requirement |
|----------|----------|-------------|-------------|
| Technical Implementation | No Account | The tutorial does not require to open complex or paying accounts for the grader. Secrets can be shared with the course GPG key. | Mandatory |
| Technical Implementation | Executability | The tutorial can be executed mostly automatically from beginning to end in the browser. | Mandatory |
| Technical Implementation | Technical Depth | The tutorial implements a non-trivial DevOps workflow involving multiple interacting components, integrations, or automation steps. | Yes/No |
| Conceptual Understanding | Relevance | The tutorial explains how it reflects DevOps concepts and practices. | Yes/No |
| Conceptual Understanding | System Reasoning | The tutorial explains the system architecture and how different components interact. | Yes/No |
| Critical Thinking | Design Decisions | The tutorial justifies the choice of tools, architecture, and configuration based on DevOps principles. | Yes/No |
| Critical Thinking | Reflection | The tutorial argues in which cases the presented approach is useful, when it is not, and for whom. | Yes/No |
| Communication | Narrative/Structure | The tutorial follows a clear structure from motivation/problem → setup → steps → outcome → reflection, and each step is accompanied by an explanation of what it does and why it is needed. | Yes/No |
| Communication | Visuals | The tutorial uses figures to support understanding (e.g., flowchart, architecture diagram). | Yes/No |
| Communication | Language | The language used is clear, correct, and appropriate. | Yes/No |
| Communication | ILO | The tutorial states the intended learning outcomes in the beginning. | Mandatory |


## Open-Source Contribution 

The concept: you contribute to one open-source project related to DevOps. Yout get at least one merged pull-request.
Criteria for the selection of the open-source project: 1) The project is related to DevOps 2) The project has more than 100 Commits 3) The project has an active community on GitHub.

| Category | Criterion | Description | Requirement |
|----------|----------|-------------|-------------|
| Technical Implementation | Technical Depth | The student implements a non-trivial contribution (bug fix, feature, improvement) that integrates correctly into the project. | Mandatory |
| Technical Implementation | Code Quality & Testing | The contribution follows project standards and includes appropriate tests and documentation. | Yes/No |
| Technical Implementation | Merge | The contribution is merged in the main branch of the target project. | Yes/No |
| Conceptual Understanding | System Reasoning | The student demonstrates understanding of the project’s architecture and how their contribution fits into it. | Yes/No |
| Critical Thinking | Design Decisions | The student justifies their implementation choices based on project constraints, existing architecture, and DevOps practices. | Yes/No |
| Critical Thinking | Relevance | The student argues how the contribution adds value to the project and fits its goals or roadmap. | Yes/No |
| Critical Thinking | Reflection | The student reflects on challenges faced, feedback received, and what they would improve. | Yes/No |
| Communication & Collaboration | Engagement with maintainers | The student engages in conversation with the project maintainers, responding to feedback in a timely manner and making necessary changes. | Yes/No |
| Communication & Collaboration | Process | The student follows the project’s contribution workflow (e.g., issues, Prs, reviews) appropriately. | Yes/No | 


## Feedback



The concept: you provide constructive and timely feedback about any task except "feedback".
The feedback is provided in a written manner as a well-structured comment on the PR of the task.
The feedback is given before the actual delivery of the task (before the presentation, before the deadline).

| Category | Criterion | Description | Requirement |
|----------|----------|-------------|-------------|
| Conceptual Understanding | Understanding | The feedback demonstrates a correct understanding of the work, its goals, and its main components. | Yes/No |
| Critical Evaluation | Criterion-based evaluation | The feedback evaluates the work using and referencing the relevant criteria, not just general impressions. | Yes/No |
| Critical Evaluation | Identification of Strengths and Weaknesses | The feedback points to clear high-level strengths and weaknesses about the work. | Yes/No |
| Critical Evaluation | Constructive | All feedback points are constructive and clearly actionable. | Yes/No |
| Critical Evaluation | Depth of Insight | The feedback explains why something is considered a strength or weakness and why it matters, and relate it to system behavior, design decisions, or DevOps principles. | Yes/No |
| Communication | Professional Tone | The feedback is respectful and appropriately phrased for a professional setting. | Yes/No |
| Process Requirements | Substance | The feedback is substantiated (at least 500 words) | Mandatory |
| Process Requirements | Generative AI | The feedback contains "I/We certify that generative AI, incl. ChatGPT, has not been used to write this feedback. Using generative AI without permission is considered academic misconduct." | Mandatory |
| Process Requirements | Timeliness | The feedback is provided 2 business days after the "go" from the authors. | Yes/No |






