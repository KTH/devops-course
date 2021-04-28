# Course automation: Essay bibliography check & summary
## Members
Amar Hodzic (amarh@kth.se)

Natan Teferi Assegehegn (ntas@kth.se)
## Proposal
We would like to create a Github Action that produces a PR comment with the number of references used as well as an excerpt from the reference list. This would simplify the TAs job in getting an overview without having to open the file and scroll down.
We are aware of another proposal that summarises essays but it has no mention of references.

What the Action should do:
* When a PR uses a specific label (e.g. essay), create a comment on that PR
* The comment should have a reference count
* The comment should include the reference list
* The reference list should be stripped down based on verbosity level set in the code (e.g. remove "accessed date", URL etc)

Criterias it should fulfill:
* Done before April 6
* The task produces a PR comment
* The task runs on a standard platform (Github Action)
* The task is praised by the other students of this course
* The code for the task is available and well documented