# Course automation proposal: check word count for essays


## Members
John Landeholt (johnlan@kth.se) 
github: landeholt

## Group rules in this course regarding groups with 3 student.
"We recommend 2 students. Three is also possible for ambitious essays, demos or contribution to open-source."

## Proposal

One of the proposed tasks that could we found in issue #916

Check that essays are 2000 words +/- 5%. This can be done with pdftotext.

_Originally posted by @monperrus in https://github.com/KTH/devops-course/issues/916#issuecomment-801790377_

## Submission
This GitHub action looks at pull requests and analyzes the newly changed pdf files. Creates a PR comment and commit status as feedback on if it passes the required length (2000 words)

### Link to action repo
https://github.com/landeholt/course-automation-essay

## Validation
No validation has been check. Only that the resources (50 word file) is correct. Can be easily reproduced by generating a file with 2000 words.
