# Course Automation: Suggesting legal teammates for projects
 
## Members
- [Carina Wickström](https://github.com/carinawic) (carinawi@kth.se)
- [Justin](https://github.com/Agriad) (arieltan@kth.se)

## Proposal
We would like to use github actions to propose teammates for students.
Students can open an issue to request for teammates.

When the student searching for a legal teammate, a list will be given of students' email addresses, where they have the following criteria:

- The potential teammate has posted < 4 project proposals
- The students and the potential teammate have not worked in the same group more than once before
- The potential teammate has not yet proposed a project in that category.

For example:

Looking for a teammate: 
carinawi@kth.se

Legal teammates:
course-automation: arieltan@kth.se, arieltan2@kth.se, arieltan3@kth.se...
Essay: ...


We aim to fulfill the following criteria:
|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The work is done before April 6, 2021 (in order to be useful for the course) |Yes |	**No** |	n-a|
|The automation task produces a PR status or issue / PR comment	| **Yes**	|No	|Points to a generated page with valuable additional information|
|The automation task is reusable	|**Yes (next year for this course)**|	No	|**In other courses than this one (if they have the smae group formation structure)**|
|The task runs on a standard platform	|**Yes (Github action)**	|No|	Other platforms (e.g. Moodle, Canvas)|
|The task is praised by the other students of this course|	**Yes**|	No|	n-a|
|The code for the task is available	|**Yes (public repo)**|	No	|**Well documented repo**|