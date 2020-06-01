# Help Fight COVID19 : a social web app

## Changes based on feedback
Based on the feedback, the following changes have been made:
* Marged the two repositories to keep only one that contains all the code: https://github.com/sujon2100/devops-course/tree/master/contributions/covid19/nsteele-mhud/localfolderfinal/NewKthproject <br/><br/>
* Added the CI and test instructions: see below in the readme file https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/README.md <br/><br/>
* Added the documentation PDF in the github repo: https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf <br/><br/>
* The current documentation on Azure has been revised to have a clear structure, fewer screenshots but we have decided to use PDF for the documentation: https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf <br/><br/>
* Added more metrics about the project: https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf <br/>
How many tests? : see on the documentation PDF section 3.<br/>
How many Locs? : see on the documentation PDF section 4.<br/>
What code coverage? : see on the documentation PDF section 5.<br/>
How long is a build? : see on the documentation PDF section 6. <br/><br/>
* The CI instructions has been documented: see below in the readme as well as section 7 in the documentation https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf <br/><br/>
* The CI/CD section of the documentation has no screenshot, but instead detail the content of
the configuration files that we have developed and justified this content,  the needs of our application: on the documentation PDF section 7 to 8 https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf. <br/><br/>
* We have added contribution on: the novel, helpful, attract support from other KTH students: on the documentation PDF section 6 https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf. <br/> <br/>
* There is no self-assessment in the readme. <br/><br/>
* Added motivation about how our contribution succeeds on these criteria: see motivation description below in the readme https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/README.md. <br/><br/>

## Link to repo and website
* The source repo is available here: https://github.com/sujon2100/devops-course/tree/master/contributions/covid19/nsteele-mhud/localfolderfinal/NewKthproject
* Website of the COVID19 project: https://kthcovid19webapp.azurewebsites.net/ (due to free subscription is ended in Azure portal, please run source code locally by using visual studio)
* Documentation: https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_FinalVersion.pdf
## Link to Azure DevOps
* Link to the Azure DevOps for features and tasks dashboard: https://dev.azure.com/KthProject2020/NewKthCovidProject/_boards/board/t/NewKthCovidProject%20Team/Features
* Link to the Build pipelines: https://dev.azure.com/KthProject2020/NewKthCovidProject/_build
* Link to the Release pipeline: https://dev.azure.com/KthProject2020/NewKthCovidProject/_releaseProgress?_a=release-pipeline-progress&releaseId=1

## Members
* Helal Uddin (mhud@kth.se/sujon2100@hotmail.com), Github id: sujon2100
* Nick Steele (nsteele@kth.se/njws1@outlook.com), Github id: Nick-Steele

## Description
This project is developed for gathering information regarding COVID-19 to update the users. It is totally non-profit-oriented project which emphasis on novelty and helping the people by providing all related information about COVID-19. Both students and people from the community can support by using this web portal. This web app is integrated with the latest Microsoft cloud platform by using Azure DevOps and Azure WebServices. As a result, this app can ensure low cost and high efficiency.
## Motivation
Due to the coronavirus lockdown, many individuals from all different walks of life have been adversely affected. Over recent months it has been difficult to find reliable information regarding a variety of Coronavirus related topics relevant to society and student life at KTH.</br></br>
Our web application is a platform where individuals are guaranteed relevant and reliable information regarding selected COVID topics. We have achieved this information delivery service utilising a variety of Microsoft DevOps based technology. This technology has allowed us to deploy new information to our web app at high velocity and with confidence using an automated CI/CD pipeline. New information can be deployed to our website as COVID changes unfold.</br></br>
The web application includes COVID-19 emergency contact information, advice regarding symptoms a person may have. It includes information about KTH students and their courses. Additionally, this website promotes fundraising for the World Health Organisation and local organisations that are committed to supporting individuals and students in need.</br></br>
We have created a Facebook group that supports our website by spreading public awareness of its existence but it also a place where existing users can communicate utilising Facebook technology, the page is moderated by people with an educated knowledge on Coronavirus, to avoid the spread of misinformation.</br></br>
Overall, we are confident that the use of our web application is highly relevant and helpful to members of the community. Due to the DevOps technologies implemented, our web application can keep up with the ever-changing problem domain of COVID by allowing users to find quality information amidst the information overload of COVID-19.
## Ties to DevOps
This COVID119 project would be integrated with the following DevOps technologies:
1. Azure DevOps to create an initial project in the cloud.
2. Connecting local .Net MVC Core web project to the Azure DevOps
3. Creating build-pipeline in Azure DevOps
4. Creating deployment-pipeline in Azure DevOps

## CI/CD instructions
- Visual Studio Team Explorer and Source Control has been used for CI
- Azure DevOps Repo for the source code shows all of the updates regarding local code changes
- Task ID from the Azure DevOps Dashboard was specified from each local code commit
- In the Azure DevOps Board, project features and related tasks have been added to track and assign project contribution. Refer to documentation for more..
## Test instructions
- It is possible to run the test and web project locally by using Visual Studio 2017 to the latest version
- Reference of the main project must be added in the test project to run locally
- Currently implemented is one test on the HomeController in the test project, its purpose is to check whether the index of the home controller is empty. Once the project is ready, a test run has been made and all the test parameters have been satisfied. Refer to documentation for more..
