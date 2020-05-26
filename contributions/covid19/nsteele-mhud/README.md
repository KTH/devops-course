# Help Fight COVID19 : a social web app

## Link to repo and website
* The source repo is available here: https://github.com/KTH/devops-course/tree/master/contributions/covid19/nsteele-mhud/localfolderfinal
* Website of the COVID19 project: https://kthcovid19webapp.azurewebsites.net/
* Documentation: https://github.com/sujon2100/devops-course/blob/master/contributions/covid19/nsteele-mhud/Covid19_Project_Documentation_Updated.pdf

## Members
* Helal Uddin (mhud@kth.se/sujon2100@hotmail.com), Github id: sujon2100
* Nick Steele (nsteele@kth.se/njws1@outlook.com), Github id: nsteele

## Description
This project is developed for gathering information regarding COVID-19 to update the users. It is totally non-profit-oriented project which emphasis on novelty and helping the people by providing all related information about COVID-19. Both students and people from the community can support by using this web portal. This web app is integrated with the latest Microsoft cloud platform by using Azure DevOps and Azure WebServices. As a result, this app can ensure low cost and high efficiency.
## Motivation
Due to the coronavirus lockdown, many individuals from all different walks of life have been affected. Over the recent months it has been difficult to find reliable information regarding a variety of Coronavirus related topics relevant to society and student life at KTH. 
Our web application is a platform where individuals can be guaranteed reliable and current information. We have achieved this by using a variety of Microsoft DevOps based technology, this means that we are able to deploy new information to our site at high velocity and confidence, an essential requirement of information delivery service operating within a highly uncertain and rapidly changing problem domain. 
The web application includes COVID-19 emergency contact information, advice regarding symptoms a person may have. It includes information about KTH students and their courses. Additionally, this website promotes fundraising for the World Health Organisation or local organisations that are committed to supporting individuals and students in need. 
We have created a Facebook group that supports our website by spreading public awareness of its existence but it also a place where existing users can communicate utilising Facebook technology, the page is moderated by people with educated knowledge on Coronavirus information, to avoid the spread of misinformation. 
Overall, we are confident that the use of our web application is highly relevant and helpful to members of the community, finding credible information amidst a chaotic event can be difficult, but our web application makes this essential obligation of finding reliable information possible. 
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
- In the Azure DevOps Board, project features and related tasks have been added to track and assign project contribution
Refer to documentation for more..
## Test instructions
- It is possible to run the test and web project locally by using Visual Studio 2017 to the latest version
- Reference of the main project must be added in the test project to run locally
- Currently implemented is a test on the HomeController, its purpose is to check whether the index of the home controller is empty. Once the project is ready, a test run has been made and all the test parameters have been satisfied.
Refer to documentation for more..
## Changes based on feedback
Based on the feedback, the following changes have been made:
* Marged the two repositories to keep only one that contains all the
code
* Added the CI and test instructions
* Added the documentation PDF in the github repo
* The current documentation on Azure has been revised to have a clear
structure, fewer screenshots
* Added more metrics about the project: How many tests? What code coverage? How many Locs? How long is a build?
* The CI instructions has been documented. 
* The CI/CD section of the documentation has no screenshot, but instead detail the content of
the configuration files that we have developed and justified this content,  the needs of our application
* We have added contribution on: the novel, helpful, attract support from other KTH students. 
* There is no self-assessment in the readme 
* Added motivation about how our contribution succeeds on these criteria.
