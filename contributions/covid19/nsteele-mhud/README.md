### About this project
This project is developed for gathering information regarding COVID-19 to update the users. It is totally non-profit-oriented project which emphasis on novelty and helping the people by providing all related information about COVID-19. Both students and people from the community can support by using this web portal. This web app is integrated with the latest Microsoft cloud platform by using Azure DevOps and Azure WebServices. As a result, this app can ensure low cost and high efficiency.

## Contributors
Helal Uddin (mhud@kth.se/sujon2100@hotmail.com) and Nick Steele (nsteele@kth.se/njws1@outlook.com)
* Final Project Link: https://dev.azure.com/KthProject2020/NewKthCovidProject 
* Live Website link: https://kthcovid19webapp.azurewebsites.net/ (Service might be off due to fee subscription, contact if it is down)

## Table of contents
1. Background
1.1 Used technologies
1.2 An architecture of the app with a component diagram Model
2. The Web Application
3. key metrics about the app (LOC)
4. The test project
5. CI/CD
5.1 CI setup and detailed presentation of the pipelines
5.1.1 CI Setup
5.1.2 Azure Build pipeline
5.1.3 Azure Release pipeline 
5.2 Explanation of the CD setup
5.3 explanation of other DevOps aspects used
5.3.1 Built-in DevOps Technology
5.3.2 Azure DevOps for COVID-19 project
5.3.3 Azure Web Services
6. Functionality/Features of the web app
6.1 COVID-19 Latest Update
6.2 Contribution to Novelty & Helping(Unique & novel)
6.3 Attract Support from other KTH students
6.4 Attract Support from Society: Community Portal
7. Dissemination plan: where did/will you advertise the website?
8. Criteria for this COVID19 project
9. References

## 1. Background
This project is developed for gathering information regarding COVID-19 to update the users. It is totally non-profit-oriented project which emphasis on novelty and helping the people by providing all related information about COVID-19. Both students and people from the community can support by using this web portal. This web app is integrated with the latest Microsoft cloud platform by using Azure DevOps and Azure WebServices. As a result, this app can ensure low cost and high efficiency.

### 1.1 Used technologies
_Frontend:_ HTML, CSS, Boostrap

_Backend:_ C# with.net core

_Development Methodology:_ Model View Control (MVC)

_CI/CD:_ Azure DevOps

### 1.2 An architecture of the app with a component diagram Model
![ComponentArchitecture.jpg](https://github.com/sujon2100/Covid19Source/blob/master/images/ComponentArchitecture.jpg)

## 2. The Web Application
ASP.NET Core MVC web application is created with C#, HTML, CSS, Boostrap to develop a Covid19 social web app. One of the most popular development patterns Model-View-Controler is used to render data from the controller to the view. This helps to develop a standard development structure so that other developer can understand the code structure and can contribute easily in the future if it needed. Link to the source code: https://github.com/sujon2100/Covid19Source/tree/master/NewKthproject
## 3. key metrics about the app (LOC)
Lines of Code(LOC) metric is used to count the total number of codes that are used in this project. TO do that Supercharger is used. The first install is from the Extention and Updates from the Tool options in the VS2017.
![Loc1.JPG](/.attachments/Loc1-239e97c1-6afc-4ac0-8091-7502dbbcf3c7.JPG)

To activate the changes, restart the VS and it will automatically finish the installation.
![Loc2.JPG](/.attachments/Loc2-29137f76-0c7b-4cc8-b40a-5b9ee6eda84d.JPG)![Loc3.JPG](/.attachments/Loc3-cee4fcaf-90c2-4c7e-b77e-b6f958522fdd.JPG)

Now, Open the VS, and Supercharger will be visible after the Tests. Open it and go to REview and Analysis tools and then select Code statistics.
![Loc4.JPG.png](/.attachments/Loc4.JPG-679a72d2-09e0-41db-a8aa-3db8f440023f.png)

A new pop up window would open. Select the Solution and press Analy! 
![Loc5.JPG](/.attachments/Loc5-7fcff301-5af8-482b-b046-26c0cdaec2d0.JPG)

This is the Code line count statistics for the entire solution of this COVID19 project:

	C# comment lines  :         9
	C# empty lines    :        43
	C# pure code lines:       294
	-----------------------------
	Total C# lines    :       346

	Non-C# lines      :    24,014

	=============================
	All lines         :    24,360


## 4. The test project
Inside of the Project Solution, a test project is added to simply right-click in the solution project, go to add, go to a new project and then select xUnit.test project under .Net core.![Test0.JPG](/.attachments/Test0-c4895f8e-2fa3-47be-84a8-0f55e32973ed.JPG)

 To get access to the main web project in the test project, a reference to the main project has been added. Besides, Microsoft.AspNetCore.All library has been installed from the Nuget Package library.
![test1.JPG](/.attachments/test1-42aad2ce-4035-484a-a05b-227ad30fb7d9.JPG)

In the test project, the HomeController of the main project has been tested by checking whether the index of the home controller is empty or not. Once the project is ready, a quick test run has been made and all of the test parameters have been successfully passed.
![test2.JPG](/.attachments/test2-63ae47ba-727b-48c3-8b92-394b327eda97.JPG).

## 5 CI/CD

### 5.1 CI setup and detailed presentation of the pipelines
#### 5.1.1 CI Setup
As it mentioned that this website is created in Visual Studio with Asp.Net MVC Core Application. One of the most interesting features of the VS is that Team Explorer and source control. VS Team Explorar can help to add changed codes to the main branch. To set up CI in VS, First, open the Team Explorer and click "Manage Connection" from the right top of the Team Explorer and select "Connect to Project". It will connect to the DevOps project that is connected with the logged-in user! Once the DevOps project is connected with the team explore, Open "Source Control Explorer" from the View/Other Windows. Now map the local folder with the DevOps project. After that Copy and paste the VS Project to the folder. Next, add files to the source control. ![devops3.JPG](/.attachments/devops3-6944f089-f1f7-4645-a0d9-c8a1241aa357.JPG)![devops4.JPG](/.attachments/devops4-2ea02f86-8997-47a7-a3cb-25ecb75520d0.JPG)

After that go back to the Team Explorer and click the home icon. Select Sync, once the synchronization is done, click the home icon again and click Changes. This will open a new window where all the changes or new code can be check in to the Master or Branch.
![devops5.JPG](/.attachments/devops5-48b8964a-4082-4959-92c8-539839e38ad8.JPG)

It is also possible to add the Task ID with every Check-In by using "Add Work Item by ID". This Task ID can be found in Azure DevOps Boards/Work Items. Moreover, in the "Comment" option, it is possible to add more details of the added task.
![devops14codepushtask2&3.JPG](/.attachments/devops14codepushtask2&3-95572ccf-4665-4850-ac44-9a56271ac5aa.JPG)![devops14task5&7.JPG](/.attachments/devops14task5&7-6ced1056-2362-4023-88c1-b69282d3d609.JPG)![devopstask91.JPG](/.attachments/devopstask91-c9438b34-2899-4d35-a89d-95ffc1be8132.JPG)

Once the changed code is pushed to the Master project in Azure DevOps, a successful message can be shown in the Team Explorer
![devops8.JPG](/.attachments/devops8-c747f92f-b4f9-4199-be33-c99ec07cf299.JPG)

All of the sources and the changesets can be found in the Azure DevOps under Repos.
![devops9.JPG](/.attachments/devops9-4aa0d75f-4ad8-4724-8416-3e8be5f3ea04.JPG)![devops10.JPG](/.attachments/devops10-af0c173c-e619-4215-945f-bbdb483cb2c7.JPG)

#### 5.1.2 Azure Build pipeline
Automated build and release pipeline is used to host Azure web services. To create a build pipeline, click in the Pipeline in Azure DevOps. As this project has used Team Foundation Version Control, TFVC is selected. 
![pipe2.JPG](/.attachments/pipe2-45b7b474-7db1-430e-b9fc-77cbf602ccd8.JPG)

After that ASP.NET Core template is selected to build and test web applications.
![pipe3.JPG](/.attachments/pipe3-97205e3a-b999-4f77-903d-ae7a27edd9d1.JPG)

This opens a new window listed with Restore, Build, Test, Publish, Publish Artifact option for the build pipeline. 
![pipe4.JPG](/.attachments/pipe4-e1ce1e1f-0d90-483b-8258-2953e3de061e.JPG)

At first, Use .Net Core ADK is added just simply click to the plus icon in the Agent Job. Once Use .Net core opens, it is needed to add the version. In this case, 2.1.302 is written.
![pipe5.JPG](/.attachments/pipe5-50f5eecc-de29-45af-bb92-1c344b49186b.JPG)

Change default build pipeline name to "<project name > Build". This can help to find distinguish between the different pipelines.
![pipe6.JPG](/.attachments/pipe6-197e6caa-abc0-409d-8620-b5cb14f7f524.JPG)

Next, enable continuous integration under the Triggers option so that any changes in the pipeline can trigger the build pipeline.
![pipe7.JPG](/.attachments/pipe7-437e6bc2-bd5a-41aa-928c-5b2076c59873.JPG)

Save all configuration and run the pipeline. 
![pipe8.JPG](/.attachments/pipe8-e0408943-2b58-4502-ae43-c39df8bf6197.JPG)

This will automatically run the pipeline. A summary is shown during a pipeline running.
![pipe9.JPG](/.attachments/pipe9-e3975157-a492-42ae-b3d6-085e705ea679.JPG)

More details of each job can be seen by clicking the Agent Job1 icon in the queued jobs. It can show the status of jobs like Build, Test, Publish, Publish Artifact.
![pipe10.JPG](/.attachments/pipe10-c40d8336-a853-4d08-abbc-94f381f0959f.JPG)
It also shows the test results. As in this project, a test project is added, the test is passed 100% as shown in the picture.
![pipe12.JPG](/.attachments/pipe12-585e6818-a2ba-4da7-9a9e-1f9230e60dea.JPG)

Finally, if there is no error happened, the Build pipeline can be successfully created and success status can be shown.
![pipe11.JPG](/.attachments/pipe11-9f48cc28-42c4-48b6-af1e-fa820a42347d.JPG)

#### 5.1.3 Azure Release pipeline 
To create a release pipeline, select Releases under Pipeline in Azure DevOps. This opens a new window where Stage and artifact are configured. Add Azure App Service deployment from the feature list.
![pipe13.JPG](/.attachments/pipe13-c5741d32-db4e-4f69-819d-2ff392fe9f7e.JPG)

Next, Stage requires to add where Stage name can be changed. This stage is used later when the app service plans would be defined.
![pipe14.JPG](/.attachments/pipe14-1ed6e8a3-d077-4cfb-aa1e-0e90b64ee755.JPG)

After that, an artifact is added with the source of the build pipeline which is created in the previous stage.
![pipe15.JPG](/.attachments/pipe15-f91c9795-d7d8-4f44-bb0d-3d9f4f42b2bc.JPG)

Continuous integration is enabled here by pressing the thunder button at this stage located in the artifact section. After enabling CI, a correct checkmark would be visible. 
![pipe16.JPG](/.attachments/pipe16-8eeffeac-eedc-41ef-9516-107c589c75ad.JPG)

In the tasks option, along with stage name, a valid azure subscription, appt type, and app service plan are configured. Note that the App service plan and Azure subscription must be created prior to create a pipeline.
![pipe17.JPG](/.attachments/pipe17-321cf27c-0c9c-4e2a-a792-d4f69c1e8839.JPG)![pipe18.JPG](/.attachments/pipe18-ce6c5719-1b17-4a44-aaf9-03baab64f63b.JPG)

Artifacts source can be configured under the File Transform & Variable Substitution Option. This would allow selecting a.Zip file.
![pipe19.JPG](/.attachments/pipe19-32f6fa75-c713-4316-aa89-ef7a6db5dcdd.JPG)

Now, a deployment method (Web Deploy) is selected with some other additional features like take the app offline, remove additional files at destination, rename locked files.
![pipe20.JPG](/.attachments/pipe20-fd26a7c2-05f0-452f-9c5c-3831a611a504.JPG)

Under Options, release name format can be defined for example adding $(Build.BuildNumber) in front of the release version can be shown the current build number with the release version.
![pipe21.JPG](/.attachments/pipe21-7b38ba2f-c164-469b-a93b-04c1ee6f624a.JPG)

After that, save all of the configurations with appropriate comments like "Initial Release created".
![pipe22.JPG](/.attachments/pipe22-a8b838d0-fb5a-4abf-8fe3-dd056f399364.JPG)

Pressing ok would show the release pipeline Artifact and Sages that have been configured so far.
![pipe23.JPG](/.attachments/pipe23-fed47326-e71a-41d4-aad1-4c90663c1e31.JPG)


Now, click to create a new release and this would show the pipeline and artifact that have been created. Once the create button is pressed, a release would be created.
![pipe24.JPG](/.attachments/pipe24-424a8624-72f2-4881-8695-64c1a4e5bc5b.JPG)![pipe25.JPG](/.attachments/pipe25-053d40ba-0632-4aab-8153-86b413db4c9c.JPG)

Finally, it shows the progress dashboard of the release pipeline and successful notification.
![pipe26.JPG](/.attachments/pipe26-b810ef1e-f4e9-4972-a6f4-fd64c8a241cd.JPG)![pipe27.JPG](/.attachments/pipe27-61409422-96d1-4e88-a3c1-63cde68c72eb.JPG)

The overall project pipelines can be observers from the DevOps Overview pages too.
![projectWIKI.JPG](/.attachments/projectWIKI-6471413d-f4b8-4fa0-b8bc-9d6c779c4ba5.JPG)


### 5.2 Explanation of the CD setup
At first, an organization is created in the Azure DevOps. Under the organization, a project is created.
![Capture.JPG](/.attachments/Capture-47d20fc4-3ab1-42be-b195-8f7c0ba4fa04.JPG)

 Once the project is created, it would show a DevOps portal, where it is possible to add project members, add project information in the wiki, add members' tasks, lookup or manage project repositories, add or delete pipelines as well as test plans and artifacts. This portal makes it possible to control the access of the members, contributors, administrations. It is also possible to add and delete a policy.

In Boards and then Work Items, each of the project tasks is created. It is possible to assign each task to the member, with the state of the task, priority, and many more. 
![Capture1.JPG](/.attachments/Capture1-554480e3-0df6-4cbe-957f-788cbe0157e2.JPG)

Once all of the tasks are created, it can be shown in the list of all tasks.
![Capture2.JPG](/.attachments/Capture2-38bffb4f-3b25-4f08-ab79-0be1faeeafaa.JPG)

Project features are added too and linked with all of the tasks that are related to each feature. In the backlog opting, it can be observed on a hierarchical view of each feature and connected tasks.
![devops12.JPG](/.attachments/devops12-b4636e28-f41c-44c6-b9f5-48797816fd1f.JPG)

On the Boards, each of the project feature statuses can be observed as New or In Progress or Done. This can help to keep track of the program of each work item more efficiently.
![devops13.JPG](/.attachments/devops13-9874f536-fe26-4f91-b744-259adb6f3198.JPG)


### 5.3 explanation of other DevOps aspects used
#### 5.3.1 Built-in DevOps Technology
For continuous delivery, deployment, and code management, Azure DevOps has been used together with Azure web services. This ensures the seamless integration from the beginning/planning phase to the delivery phase.

#### 5.3.2 Azure DevOps for COVID-19 project
Azure DevOps project is created to use Team Foundation Services(TFS) and agile methodology to integrate and manage the development process from the Visual Studio Covid19 project. This could help to support the Covid19 affected community with reliable online coronavirus update.![website2.JPG](/.attachments/website2-0fed3c31-c25e-4ee6-9c5b-ba6e356d9709.JPG)

#### 5.3.3 Azure Web Services
To able to consume web services, the Azure app service plan has been created together with resource groups to run the local project to the cloud. Azure web services can be used configured by using the Azure portal.
![az2.JPG](/.attachments/az2-acd56215-e56a-4fcf-ba67-193a92654b8a.JPG)![az3.JPG](/.attachments/az3-66915a9f-aa69-4358-941d-c4f80d5f73e2.JPG)![az4.JPG](/.attachments/az4-bfb019e8-9125-49fc-b8d9-490e32f2524e.JPG)

## 6. Functionality/Features of the web app
### 6.1 COVID-19 Latest Update
In this website, COVID-19 update regarding confirmed, recovered, and death cases have been shown by using COVID-19 API. Global summary of COVID-19 can be shown in a nice frontend from https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en. Besides, a JSON format of data could be received from this API "https://corona.lmao.ninja/v2/all". It is also possible to find all of the confirmed cases for a particular country like Sweden.
![website.JPG](/.attachments/website-3986fb11-7f42-4790-87c6-ddbb40b49bd7.JPG)![website1.JPG](/.attachments/website1-88db5fa8-c085-4e00-be0c-a62e2a9ace98.JPG)

### 6.2 Contribution to Novelty & Helping(Unique & novel)
The uniqueness of this web app regarding novelty is that it has connected both small Facebook group to collect support for the COVID19 positive patients as well as promoting WHO Donation fund for the covid19 affected people.

Moreover, others helping and supporting the research work or employees have been linked up on the webpage.
![website3.JPG](/.attachments/website3-8db5fbea-f5ff-449c-ad75-92364891503b.JPG)![website7.JPG](/.attachments/website7-b0d428f9-81e6-4cff-b48d-cb9bd06bbfe7.JPG)

### 6.3 Attract Support from other KTH students
Student Portal: In this section, KTH students can be able to get information regarding information and access in the canvas too. Because of the lockdown situation, Zoom has been linked up for the KTH students. For future students, information regarding courses and contact information has been provided in under each program section.
![website4.JPG](/.attachments/website4-6b92c31f-8e50-46e0-af9e-b8db00035884.JPG)![website5.JPG](/.attachments/website5-bde74d2a-196f-41f8-ba1b-9654e9b796b4.JPG)

### 6.4 Attract Support from Society: Community Portal
People from different communities can get help from the Community portal according to their municipality. There is an option for each section. In the first section, people can get their Emergency help by visiting the linked address. For the COVID-19 test kit or any medical assistance, "COVID-19? Support" can be referred to. If someone can learn more in the "COVID-19: Learn more" section about the symptoms of this disease and all related issues. "COVID-19 Update" section can give all current information regarding different cities and communities.
![website4.JPG](/.attachments/website4-6b92c31f-8e50-46e0-af9e-b8db00035884.JPG)![website6.JPG](/.attachments/website6-9d608ae9-034d-4fce-bddb-23bb5f682fe7.JPG)

## 7. Dissemination plan: where did/will you advertise the website?
We can advertise this website on social media like Facebook, Instagram, Linkedin. This would help to let people know more about the Help Fight COVID19 project and encourage people to attract to use and contribute for the society. We can advertise on our COVID19 Facebook page(https://m.facebook.com/groups/815512272277849).

## 8. Criteria for this COVID19 project
This COVID-19 project is fulfilling the following criteria:
-The contribution is related to COVID-19
-The contribution is related to / built with DevOps technology
-The contribution is novel
-The contribution is helpful
-The contribution attracts support from other KTH students

## 9. References
**[1] For correctly formatted final project report, please refer to the wiki link here: https://dev.azure.com/KthProject2020/NewKthCovidProject or https://dev.azure.com/KthProject2020/NewKthCovidProject/_wiki/wikis/NewKthCovidProject.wiki/2/Help-Fight-COVID-19-Web-App**
[2] https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en
[3] https://corona.lmao.ninja/v2/all
[4] https://api.covid19api.com/country/sweden/status/confirmed
[5] https://portal.azure.com/#home
[6] https://visualstudio.microsoft.com/
[7] https://covid19responsefund.org/
[8] https://m.facebook.com/groups/815512272277849
[9] https://www.canada.ca/en/public-health/services/publications/diseases-conditions/covid-19-information-essential-service-workers.html
[10] https://www.canada.ca/en/public-health/services/publications/diseases-conditions/help-reduce-spread-covid-19.html
[11] https://kth.instructure.com/courses/
[12] https://www.kth.se/en/om/kontakt
[13] https://polisen.se/en/the-swedish-police/contacting-the-police/
[14] https://www.vardcentraler.sll.se/
[15] https://www.folkhalsomyndigheten.se/the-public-health-agency-of-sweden/communicable-disease-control/covid-19/about-the-disease/
[16] https://www.google.com/search?rlz=1C1CHBD_svSE814SE814&q=Coronavirus+Stats&stick=H4sIAAAAAAAAAONgFuLVT9c3NMwySk6OL8zJUULlPmL05hZ4-eOesJTTpDUnrzHacHEFZ-SXu-aVZJZUCulxsUFZKlyCUqg6NRik-LlQhXh2MXF7pCbmlGQElySWFC9iFXTOL8rPSyzLLCotVgCLAQCnsUMMkAAAAA&biw=1232&bih=740
[17] https://intra.kth.se/en/campus/sakerhet/kris/corona/information-till-anstallda-med-anledning-av-coronaviruset-1.965906
[18] https://intra.kth.se/en/campus/sakerhet/kris/corona/information-till-studenter-med-anledning-av-coronaviruset-1.965905
[19] https://www.youtube.com/embed/k8vuUJ7hVLY
[20] https://www.youtube.com/embed/JCw-B4Ig3DQ
**[21] Link to a public repo with source code: https://github.com/sujon2100/Covid19Source/tree/master/NewKthproject**
