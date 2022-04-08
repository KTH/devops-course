# Assignment Proposal

## Title

Check that there is a valid link to the slides for all presentations.

## Names and KTH ID
  - Philip Hamelink (ppjha@kth.se)
  - Thomas Srour (srour@kth.se)

## Deadline

Task 1: April 5, 17h Stockholm time

## Category

Course automation

## Description

Create a github action upon each PR labeled **presentation** and **final_submission** will 
check for a link to the slides. To do this we can either 
- check all links in the repo and see if there is a valid link to some slides
- create a presentation README template with a section named *Presentation slides*, 
and every PR will check to see if the format of the README is correct and if there is a valid link under that section.

With our submission, we aim for the following grading criteria. The worflow file that can be used can be found on our forked [repo](https://github.com/phamelink/devops-course/blob/2022/.github/workflows/check-slides.yml). The code and documentation for this action can be found on [here](https://github.com/phamelink/check-valid-slides-action). We also uploaded the action for the course to automatically check for valid slides on [Github market place](https://github.com/marketplace/actions/check-valid-slides)

For this assignment, we worked in a peer-programming method with [Thomas Srour](https://github.com/thomassrour)

|                                             | Yes | No | 
|-------------------------------------------- | ----|----|
|timeliness: the automation is done before the first task deadline (in order to be useful for the course) | **:white_check_mark: YES** | - |
|repo: the code for the task is available in a public repo  | **:white_check_mark: YES**| - | 
|outcome: the automation task produces a PR status or an issue / PR comment | Yes | **No** |
|reuse: the automation task is reusable (next year for this course) | **:white_check_mark: YES** | No | 
|platform: the task runs on a Github action | **:white_check_mark: YES** | No | 
|doc: the repo is documented with a good readme | **:white_check_mark: YES**  | No | 
|figure: the README is illustrated with at least an informative figure (eg a flowchart) | Yes | **No** | 
|availability: The action is available on a market place (Github Marketplace, Azure Marketplace, etc.) | **:white_check_mark: Yes** | No |

The demonstration of how this action works can be found under this [pull request](https://github.com/phamelink/devops-course/pull/14). We simulated a presentation submission without slides, added a 'presentation' label to the PR, and then showed how commit pass or fail the checks depending on whether there are valid slides (a link in the README or a PDF files in the submission)
