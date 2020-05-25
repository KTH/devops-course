# Help Fight COVID19 : a social web app

## Link to repo and website
* The source repo is available here: https://github.com/sujon2100/devops-course/nsteele-mhud/localfolderfinal
* Website of the COVID19 project: https://kthcovid19webapp.azurewebsites.net/

## Members
* Helal Uddin (mhud@kth.se/sujon2100@hotmail.com), Github id: sujon2100
* Nick Steele (nsteele@kth.se/njws1@outlook.com), Github id: nsteele

## Description
This project is developed for gathering information regarding COVID-19 to update the users. It is totally non-profit-oriented project which emphasis on novelty and helping the people by providing all related information about COVID-19. Both students and people from the community can support by using this web portal. This web app is integrated with the latest Microsoft cloud platform by using Azure DevOps and Azure WebServices. As a result, this app can ensure low cost and high efficiency.
## Motivation
Due to the coronavirus lockdown, everyone is affected whether a normal person or a KTH student/employee. It is important to keep updated with COVID19 situation from time to time. Moreover, if a person is confirmed with COVID19 positive, or has COVID19 symptom, he/she needs emergency contacts with the local healthcare. Besides, a student/employee needs an update about the courses or the instruction during the lockdown situation. All of these current facts have motivated us to create a web portal where it can serve the latest information regarding Covid19 update, emergency contact information based on the local community, KTH students support about the curses or admission. This website could promote fundraising for the WHO as well as locally which would be spent to help and support COVID19 affected people or students.
## Ties to DevOps
This COVID119 project would be integrated with the following DevOps technologies:
1. Azure DevOps to create an initial project in the cloud.
2. Connecting local .Net MVC Core web project to the Azure DevOps
3. Creating build-pipeline in Azure DevOps
4. Creating deployment-pipeline in Azure DevOps

## CI/CD instructions
As mentioned, this website is created in Visual Studio (VS) utilising Asp.Net MVC Core Application. One of the most interesting features of VS is the Team Explorer and Source Control. Visual Studio Team Explorer has helped us add and integrate code changes to the main branch. We set up CI in VS through using Team Explorer and connected it to our main project. This allowed for the DevOps project to connect with the logged in user. Once this was achieved, we used “Source Control Explorer” from the View/Other Windows and mapped the local folder with the DevOps project. After this we copied and pasted the VS project to the folder and added the files to our Source Control and synchronised them together. It is then possible to view these changes in a new window where all the changes or new code can be check in to the Master or Branch. It is also possible to add the Task ID with every Check-In by using ”Add Work Item by ID”. This Task ID can be found in Azure DevOps Boards/Work Items. Moreover, in the” Comment” option, it is possible to add more details of the added task. Once the changed code is pushed to the Master project in Azure DevOps, a successful message can be shown in the Team Explorer. All the sources and the changesets can be found in the Azure DevOps under Repositories. Refer to the project document for complete instruction for Build & Release Pipeline.

Firstly, we created an organization in Azure DevOps.  Under the organiza-tion, a project is created.  Once the project is created, it shows the DevOpsportal, where it is possible to add project members, add project informationin the wiki, add members’ tasks, lookup or manage project repositories, addor  delete  pipelines  as  well  as  test  plans  and  artifacts.   This  portal  makesit possible to control the access of the members, contributors, administra-tions.  It is also possible to add and delete a policy.  In Azure Boards andWork  Items,  each  of  the  project  tasks  is  created.   It  is  possible  to  assigneach  task  to  the  member,  with  the  options  such  as  the  state  of  the  taskand  the  priority.   When  all  tasks  are  created,  it  can  be  shown  in  the  listof  all  tasks.   Project  features  are  added  and  linked  with  other  tasks  thatare related to each feature.  In the backlog opting, it can be observed on ahierarchical view of each feature and connected tasks.  On the Boards, eachof  the  project  feature  statuses  can  be  observed  as  New  or  In  Progress  orDone.  This can help to keep track of the program of each work item moreefficiently.

## Test instructions
Inside of the Project Solution, a test project is added which would be expanded on in the future. A reference to the main project is added and all libraries have been installed from the NuGet Package Manager. Currently implemented is a test on the HomeController, its purpose is to check whether the index of the home controller is empty. Once the project is ready, a test run has been made and all the test parameters have been satisfied.

## Chnages have been made
Based on the feedback, the following changes have been made:
* Marged the two repositories to keep only one that contains all the
code
* Added the CI and test instructions
* Added the documentation PDF
* The current documentation on Azure has been revised to have a clear
structure, fewer screenshots
* Added more metrics about the project: How many tests? What code coverage? How many Locs? How long is a build?
* The CI instructions has been documented. 
* The CI/CD section of the documentation has no screenshot, but instead detail the content of
the configuration files that we have developed and justified this content,  the needs of your application
* We have added contribution on: the novel, helpful, attract support from other KTH students. 
* There is no self-assessment from the readme 
* Added motivation about how our contribution succeeds on these criteria.
