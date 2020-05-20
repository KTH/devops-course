# Finished Demo: GitLab CI/CD pipeline (Building, Testing, Deployment to Heroku)

Link to the Youtube screencast: https://youtu.be/0YTg6ryIxOE

The accompanying GitLab repository: https://gitlab.com/christinasunnegardh/devops-gitlab-demo

The improvements that have been made after the feedback on the Demo Day are the following:
- Added a description to the README at the accompanying GitLab repository
- Fixed minor issues with the subtitles
- Removed the "prerequisites" part in the screencase and updated the description with this information instead
- Removed the unnessecary action in the screencast where ruby is installed altought we are already on a Ruby Docker image.
- Added information about that you can specify a specific version of the image in docker
- Changed the easter egg completely
- Major changes to the end/take-away part in the screencast
    - Relate to DevOps again, what happens when the pipeline fails etc.
    - Hint about where to fid the easter egg
- Made updates to the description on Youtube.

*Old youtube link, before feedback: https://youtube.com/watch?v=5IkDrgFSFw4*
# Demo proposal

## Members
Christina Sunnegårdh (sunneg@kth.se)

## Topic
I have come across that GitLab offers their own CI/CD for projects, as opposed to the traditional way where you would have to integrate an external CI/CD. I would like to create a demo on how to integrate this in an example project. In the demo, we will create a pipeline for the application that carries out some tests, and if theese are ok, deploys the application to Heroku.

The application will be a simple Node JS application and the tests will most probably be using the Jest testing framework (I will not put alot of emphasis on how the tests are written, they will be simple and using Jest is just an example).

## Outline

- Background
    - What is GitLab?
    - What is CI/CD?
- Demo
    - How to integrate GitLab's CI/CD in a GitLab repo (GitLab Runner)
    - Setting up the pipeline to test and deploy to Heroku
- Wrap-up
    - Reflect quickly on demo
    - Final thoughts



I aim to fulfill the criterias in bold:

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The demonstration screencast is clearly motivated (why it matters for Devops?) | **Yes** | No | **Remarkable** |
|The demonstration screencast is difficult to do | Yes | No | Remarkable |
|The demonstration screencast is original | **Yes** | No | Remarkable |
|The demonstration screencast is sublime (eg visually appealing) | **Yes** | No | **Remarkable** |
|The demonstration screencast contains an easter egg | **Yes** | No | Remarkable |
|An accompanying Github repository has been made (optional) | **Yes** | No | **Remarkable** |