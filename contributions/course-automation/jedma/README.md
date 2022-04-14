# Assignment Proposal

## Title

_Automatic schedule import to GitHub_

## Names and KTH ID
  - Johan Edman (jedma@kth.se)

## Deadline

Task 1

## Category

Course automation

## Description

As the GitHub repository acts as the central meeting place for the course with  
most of the course-related information already available here, it would be  
convenient to continue to gather and display as much of the course information  
from external services here.

Currently, the schedule section of the `README.md` refers students to KTH Social  
for calendar events. This requires students to navigate away from GitHub to see  
the events there (or to check e.g. TimeEdit).

I'd like to contribute with a GitHub action that automatically fetches calendar  
events from [KTH TimeEdit](https://cloud.timeedit.net/kth/web/public01/ri155XQ7093Z5YQv580508Z6yQY440480YX1Y5gQ9025787.html) and exports them to a convenient format for display  
(e.g. markdown). All the calendar events for the course offering could be displayed  
in the `README.md` schedule section or on a separate Wiki page, and automatically  
updated as events are updated. Thus, students could see the schedule information  
directly in the `README.md` or on a related wiki page, and not have to navigate away  
from GitHub to see the information.

<hr>

**FINAL SUBMISSION**

| Link                                                                                                                  |       Description      |
| ----------------------------------------------------------------------------------------------------------------------| ---------------------- |
| [Repository](https://github.com/EdmanJohan/schedule-update-action)                                                    | Repo for Github Action |
| [Marketplace](https://github.com/marketplace/actions/update-timeedit-schedule-events)                                 | Github Marketplace     |
| [Test environment](https://github.com/EdmanJohan/devops-course-demo)                                                  | Fork of repo for demo  |
