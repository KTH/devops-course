# Assignment Proposal
## Title
Send an automatic weekly mail to students to give plan for next week and a summary of taks to do

## Names and KTH ID
- Pauline Vaillant (paulinev@kth.se)

## Deadline
Task 2
## Category
Course Automation
## Description

I would create a github action that send a weekly mail that would send a mail with 
- plan for the next week (arcticles to read according to the readme), when and where are the lectures
- task done, and next task deadline (for example if the student has done 0 task, it would be the deadline for task 1, if it has aldready done 1 task, it would be the date for deadline 2)

To create my mail I have :
- analayze the readme to find the task deadline and the articles to read
- analysze the calendar ics found there "https://www.kth.se/social/course/DD2482/calendar/ical/?lang=en"
- use the issue statistics  ( #1607 (Statistics of Student Registrations) for this year for example) to have the number of task done by a student. FOr studennt with no task yet I will try to use canvas API (if I can have acces to it) 


== Final submission
- ![GitHup Repo](https://github.com/paulinev-kth/weekly_recap_mail)
- ![Marketplace](https://github.com/marketplace/actions/dd2482-weekly-mail)
