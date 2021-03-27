# Course automation proposal: Verify PR submitted have Github id's and KTH ids matching students registered to the course 

 ## Members
-----
Kalle Pettersson (kalpet@kth.se)
GitHub: [KallePettersson](https://github.com/KallePettersson)

Anders Nillson (andnil5@kth.se)
GitHub: [andnil5](https://github.com/andnil5)

-----

 ## Proposal
We want to solve the issue described by baudry in #916.
"Check that all PR submitted for the course come from a Github id that corresponds to one KTH id of a student who registered for the course"

 ## Proposed solution:

* Create a GitHub javascript action to be run on each PR.
* Extract the GitHub id of the PR author.
* Create a list of valid kth ids (from students registered to course).
* If GitHub id matches kth id, set a status check flag to success.
* Otherwise, check that the Member mail address in the README match, and set the status check flag to success.
* If both of the above fails, set the status check flag to failure.
* Utilize Status checks API to visualize the result for the TA:s.


## Solution

ncc build index.js -o ../dist

### Requierments for solution to run
This solution is written with two assumptions in mind. First there needs to be a textfile called **kth-ids.txt** with the email addresses of students registered to the course. The file needs to have the following format:

````
...
Username1@kth.se
Username2@kth.se
...
````

Secondly each README file for a given PullRequest needs to placed in the correct folder, as follows: 
````
devops-course/contributions/<Category>/<StudentName(s)>/README.md"
````
And the Members section of the README file needs to be written with the following syntax:
````
## Members
-----
<Student1Name> (<Username1>@kth)
Github: [<GithubID1>](<linkToGithubProfile1>)

<Student2Name> (<Username2>@kth)
Github: [<GithubID2>](<linkToGithubProfile2>)
-----
````