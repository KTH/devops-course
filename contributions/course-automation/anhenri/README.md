# Course automation: Check length of youtube video

## Members

Andreas Henriksson (anhenri@kth.se)
GitHub: [heeenkie](https://github.com/heeenkie)

## Proposal

I would like to check the length of the demo video so that it fulfills the requested length.


For this, I will do a Github action on pushes that concernes the demo folder.
Extract the url to the youtube video
Check the length of the video and if it is between 3 and 5 minutes
Update PR status

## Result
The developed Github Action can be found [here](https://github.com/marketplace/actions/youtube-checker).
All requirments and full setup is described on the frontpage of the provided link above.

Demos can be found [here](https://github.com/heeenkie/youtube-link-checker-action/pulls).
The repo have copied the path from KTH/devops-course github repository 
and a pull with a readme file including a youtube link have been requested.

The action runs on pull requests inside the demo folder. It checks all youtube links provided in the readme file. 
If a youtube link with a video with a duration outside the time range is found it updates the pull requests status to fail. 
Otherwise it succeeds.


|||
|-|-|
|The work is done before April 6, 2021 (in order to be useful for the course) | Yes |
|The automation task produces a PR status or issue / PR comment | Yes |
|The automation task is reusable | Yes (next year for this course) |
|The task runs on a standard platform | Yes (Github action) |
|The code for the task is available | Yes (public repo) |


