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

## Solution:

* Create a GitHub javascript action to be run on each PR.
* Reads a list of valid kth ids (from students registered to course).
* Parse `README.md` file and extract student kth-ids.
* Check that the students kth-ids match the list of valid ids.
* If the kth-ids are valid, set a status check flag to success.
* If one or more kth-ids are invalid, set the status check flag to failure.

### Requierments for solution to run
This solution is written with two assumptions in mind. First there needs to be a textfile called **kth-ids.txt** with the email addresses of students registered to the course. The path for this file could be configured in **src/config/config.js**. The file needs to have the following format:

````
...
Username1@kth.se
Username2@kth.se
...
````
Note: The kth email addresses must be separated by one or many of the following characters:
* A space character
* A tab character
* A carriage return character
* A new line character
* A vertical tab character
* A form feed character
* A comma 
* A semicolon


Secondly each `README.md` file for a given PullRequest needs to placed in the correct folder, as follows: 
````
devops-course/contributions/<Category>/<StudentName(s)>/README.md"
````
And the Members section of the `README.md` file needs to be written with the following syntax:
````
## Members
-----
<Student1Name> (<Username1>@kth)
Github: [<GithubID1>](<linkToGithubProfile1>)

<Student2Name> (<Username2>@kth)
Github: [<GithubID2>](<linkToGithubProfile2>)

-----
````
Note: It is important that student email addresses are encapsulated with parenthesis and that the
opening and closing tags `-----` are present.

## Contribution


### Installation
1. Clone this repo (https://github.com/KallePettersson/devops-course.git) 
2. Download and install Node.js 12.x, which includes npm.(https://nodejs.org/en/download/current/)
3. Cd into `devops-course/contributions/course-automation/kalpet-andnil5/src` and run `npm install`
4. Install `vercel/ncc` by running this command in your terminal: `npm i -g @vercel/ncc`
5. Now all tools needed are installed and setup.


### Compilation
All changes to the github action needs to be compiled into the `/dist/index.js` file in order to run. This can be done with the following command executed from the src folder.
```
ncc build index.js -o ../dist
```