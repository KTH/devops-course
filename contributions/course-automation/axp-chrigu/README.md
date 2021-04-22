# Course automation: Dashboard for tasks

## Members

Axel Pettersson (axp@kth.se)
GitHub: [Ackuq](https://github.com/Ackuq)

Christopher Gustafson (chrigu@kth.se)
Github: [ChristopherGustafson](https://github.com/ChristopherGustafson)

## Proposal

Create a GitHub action that is triggered when new tasks/proposals are committed to the repository, this will then generate a dashboard of all the contributions made overall, including those submitted in the previous years.

The requirements for the actions are:

-   Automatic triggered at new submissions
-   Include the authors and title of the task
-   Link to the task
-   Classify if completed or not
-   Group by year and category
-   Display the number of submissions per category/year
-   Search for repeated tasks
-   Provide a summary per year: nb of tasks per category, nb of submissions, etc.

## Final Solution

In this folder, you can find the source code of the final solution for the course repo dashboard. It is divided into two separate GitHub actions, one for generating the dashboard and one for commenting on a pull request that the dashboard has been generated. Instructions on how to set up these actions can be found in the README's of the respective folders. A preview of the final solution can also be found in this [fork](https://github.com/Ackuq/devops-course) where the ```dashboard.md``` file is the final result when someone creates a pull request.

During the project, some limitations were found that led us to alter or disregard some of the proposed requirements above. The following requirements were revised:

* Authors and titles of all the tasks were not able to be extracted as there is no common structure that all tasks follow for presenting authors and title. The most common patterns were extracted, but for some tasks, the authors and title will not be identified and displayed as "Authors/Title not found".
* For the same reason, the requirement "Classify if completed or not" was completely disregarded. Since there exists no clear structure for if a task is completed or not, we quickly realized that classifying these was outside the scope of this project.
* The requirement "Search for repeated tasks" was altered to instead search for tasks concerning the same technologies. We realized that two tasks might be the same but have slightly different titles, and it would thus be hard to figure out which tasks were concerning the same problem. We therefore altered the requirement to address a different, but still relevant question.