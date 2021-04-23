# Course automation proposal: Verify PR submitted have Github id's and KTH ids matching students registered to the course 

 ## Members

 Kalle Pettersson (kalpet@kth.se)
 GitHub: [KallePettersson](https://github.com/KallePettersson)

 Anders Nillson (andnil5@kth.se)
 GitHub: [andnil5](https://github.com/andnil5)

 ## Proposal
We want to solve the issue described by baudry in #916.
"Check that all PR submitted for the course come from a Github id that corresponds to one KTH id of a student who registered for the course"

 ## Proposed solution:

* Create a GitHub javascript action to be run on each PR.
* Extract the GitHub id of the PR author.
* Create a list of valid kth ids (from students registered to course).
* If GitHub id matches kth id, approve PR.
* Otherwise, check that the Member mail address in the README match.
* Utilize Status checks API to visualize the result.