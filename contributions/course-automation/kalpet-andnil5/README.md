# Course automation: Verify PR submitted have GitHub ids and KTH ids matching students registered to the course

## Members
-----
Kalle Pettersson (kalpet@kth.se)  
GitHub: [KallePettersson](https://github.com/KallePettersson)

Anders Nilsson (andnil5@kth.se)  
GitHub: [andnil5](https://github.com/andnil5)

-----

## Proposal
We want to solve the issue described by Baudry in [#916](https://github.com/KTH/devops-course/issues/916): "Check that all PR submitted for the course come from a GitHub id that corresponds to one KTH-id of a student who registered for the course".

## Grading - We strive to meet the following grading criteria

| | Yes | No | Remarkable |
|---|:-:|:-:|:-:|
| The work is done before April 6, 2021 (in order to be useful for the course) | X | | |
| The automation task produces a PR status or issue / PR comment | X | | X |
| The automation task is reusable | X | | |
| The task runs on a standard platform | X | | |
| The task is praised by the other students of this course | X? |  |  |
| The code for the task is available | X | | X |
----

## Solution:
* Creates a GitHub JavaScript Action to be run on each PR.
* Reads a file including valid kth ids (from students registered to course).
* Parses the contribution's `README.md` file and extract the students' kth ids.
* Checks that the students' kth ids match the list of valid ids.
* If the kth ids are valid, set a status check flag to success.
* If one or more kth ids are invalid, set the status check flag to failure.

## Test the solution
The GitHub Action is set to be triggered on each Pull Request. We have set up a test branch to ease testing of the workflow. This is done by performing the following steps:
1. Go to the [Pull requests](https://github.com/KallePettersson/devops-course/pulls) page in the forked repository and click `New pull request`.
2. Select from repository `KallePettersson/devops-course` and branch [course-automation](https://github.com/KallePettersson/devops-course/tree/course-automation) to repository `KallePettersson/devops-course` and branch [course-automation-test](https://github.com/KallePettersson/devops-course/tree/course-automation-test).
3. Click on `Create pull request`, and on the next page, click `Create pull request` again. This will trigger the action.

## Source code location
The actual source code of the implementation can be found in the [course-automation branch](https://github.com/KallePettersson/devops-course/tree/course-automation/contributions/course-automation/kalpet-andnil5). The GitHub action workflow file is located in the [`.github/workflow`](https://github.com/KallePettersson/devops-course/tree/course-automation/.github/workflows) folder. The remaining source code is located in the [`course-automation/contributions/course-automation/kalpet-andnil5`](https://github.com/KallePettersson/devops-course/tree/course-automation/contributions/course-automation/kalpet-andnil5) folder.

## Requirements for solution to run
This solution is written with three assumptions in mind. 

*First*, there needs to be a text file including course registered students' usernames. This implementation is currently using the file `Registered_KTH_IDs.txt`, which is located in the root of the repository. The path for this file could be configured in `contributions/course-automation/kalpet-andnil5/src/config/config.js`. 

**Note**: The usernames in **Registered_KTH_IDs.txt** must be separated by one or more of the following characters:
* A space character
* A tab character
* A carriage return character
* A new line character
* A vertical tab character
* A form feed character
* A comma 
* A semicolon

### Example format for `Registered_KTH_IDs.txt`
````
...
kthid1
kthid2 kthid3     
...
````

*Secondly*, the `README.md` file for a given PullRequest needs to placed in the correct folder, as follows:
````
devops-course/contributions/<Category>/<StudentName(s)>/README.md"
````
And the Members section of the `README.md` file needs to abide by the following format:
````
## Members
-----
<Student1Name> (<Username1>@kth)
Github: [<GithubID1>](<linkToGithubProfile1>)

<Student2Name> (<Username2>@kth)
Github: [<GithubID2>](<linkToGithubProfile2>)

-----
````
Note: It is crucial to encapsulate the email addresses with parentheses and that the opening and closing tags `-----` are present.

*Finally*, it's assumed that the PullRequest made by a student only includes modifications of files located in the directory of the contribution, according to the course convention. For instance, if kalpet makes a PullRequest for an essay task, it's assumed that all modifications are included in the `devops-course/contributions/essay/kalpet/` folder.

## How to update and modify the implementation

To change the implementation one has to perform four steps:
1. Install all necessary dependencies as explained below.
2. Make your changes.
3. Compile the files.
4. Push the changes to GitHub.

### Installation
1. Clone the repository (https://github.com/KallePettersson/devops-course.git)  
2. Checkout to the course-automation branch
3. Download and install [Node.js 12.x](https://nodejs.org/en/download/current/), which includes npm.
4. cd into `devops-course/contributions/course-automation/kalpet-andnil5/src` and run `npm install`
5. Install `vercel/ncc` globally by running this command in your terminal: `npm i -g @vercel/ncc`
6. Now, all tools needed are installed and set up. Make sure to compile and push the files after the changes have been made.

### Compilation
The GitHub Action files must be compiled into the file `/dist/index.js` to put your changes into action. This can be done by executing the following command from the `devops-course/contributions/course-automation/kalpet-andnil5/src` folder.
```
ncc build index.js -o ../dist
```
