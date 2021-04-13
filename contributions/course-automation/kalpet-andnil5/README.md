# Course automation: Verify PR submitted have GitHub ids and KTH ids matching students registered to the course

## Members
-----
Kalle Pettersson (kalpet@kth.se)  
GitHub: [KallePettersson](https://github.com/KallePettersson)

Anders Nillson (andnil5@kth.se)  
GitHub: [andnil5](https://github.com/andnil5)

-----

## Proposal
We want to solve the issue described by Baudry in [#916](https://github.com/KTH/devops-course/issues/916): "Check that all PR submitted for the course come from a Github id that corresponds to one KTH id of a student who registered for the course".

## Solution:

* Create a GitHub JavaScript action to be run on each PR.
* Reads a list of valid kth ids (from students registered to course).
* Parse the contributions `README.md` file and extract student kth-ids.
* Check that the students' kth-ids match the list of valid ids.
* If the kth-ids are valid, set a status check flag to success.
* If one or more kth-ids are invalid, set the status check flag to failure.

### Requirements for solution to run
This solution is written with two assumptions in mind. First, there needs to be a text file called **kth-ids.txt**, including course registered students' email addresses. The path for this file could be configured in **src/config/config.js**. The file needs to have the following format:

````
...
Username1@kth.se
Username2@kth.se
...
````
Note: The students' email addresses must be separated by one or many of the following characters:
* A space character
* A tab character
* A carriage return character
* A new line character
* A vertical tab character
* A form feed character
* A comma 
* A semicolon

Secondly, each `README.md` file for a given PullRequest needs to placed in the correct folder, as follows:
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
Note: It is crucial to encapsulate the email address with parenthesis and that the opening and closing tags `-----` are present.

## TA-NOTE

For the GitHub action to work, one must move the file `./contributions/course-automation/kalpet-andnil5/.github/workflows/kthID-validator.yml` to the root of the repo `.github/workflows/kthID-validator.yml`.

## Contribution

### Installation
1. Clone this repo (https://github.com/KallePettersson/devops-course.git)  
2. Checkout course-automation branch
3. Download and install [Node.js 12.x](https://nodejs.org/en/download/current/), which includes npm.
4. Cd into `devops-course/contributions/course-automation/kalpet-andnil5/src` and run `npm install`
5. Install `vercel/ncc` by running this command in your terminal: `npm i -g @vercel/ncc`
6. Now, all tools needed are installed and set up.

### Compilation
The GitHub action files must be compiled into the file `/dist/index.js` to put your changes into action. This can be performed by executing the following command from the `src` folder.
```
ncc build index.js -o ../dist
```