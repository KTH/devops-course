# Course automation: Essay bibliography check & summary
## Members
Amar Hodzic (amarh@kth.se)

Natan Teferi Asegehegn (ntas@kth.se)

## Proposal #1008 
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
* The automation task is reusable (possibly in other courses that use Github)
* The task runs on a standard platform (Github Action)
* The code for the task is available and well documented

## Final solution
The action was created with Docker and Python making it easy to integrate with a repository. The action is well documented, both with a good README as well as docstrings in the code. Pair-programming was used for the whole development.

We tested the action on all the PDF files from last years Essay category (`attic/2020/contributions-2020/essay/`) and 31 out of 34 PDF files were parsed and summarized correctly.
Out of the 4 that could not be parsed, one was a copy of a medium article without references, one only had URLs as bullet points in reference list, one did not have a reference list, and one used Harvard reference system. Meaning that the system in reality only failed with the Harvard system which could be questionable to use as a computer scientist and in this course.
A PR comment summary example can be found in our [test PR](https://github.com/amarhod/devops-course/pull/1#issuecomment-812869936).

We chose not to do multiple verbosity levels for stripping down references. The problem is that PDF is a document format designed to be printed, not to be parsed. Inside a PDF document, the text is not necessarily in a particular order. Meaning that it would be hard to make a generalisation for picking out parts of a reference when the parser does not detect the same attributes (e.g. URL) between references all the time. We felt that it was out of the scope given the effort we already had put in. However, this could be attempted in future works (i.e. as a task for next year).

The trigger we have chosen in the workflow is to run the job on PR that has the label `essay`. If the student commits an updated or new PDF in the same PR, the label needs to be removed and added again to trigger the action to run again. However, you may change the triggering as your prefer.

The public repository for the action can be found [here](https://github.com/amarhod/pdf-bibliography-action).

