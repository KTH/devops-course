# COVID-19 KTH Course Info
A project by Johanna Iivanainen (jii@kth.se) and Tommy Samuelsson (tommysam@kth.se) for the course Automated Software Testing and DevOps DD2482.

## Table of contents
1. [Background](#back)
    
2. [The Application](#app)

    2.1 [Functionality](#func)
    
    2.2 [DevOps Tools](#dev)
    
3. [Criteria for COVID19 Assignment](#crit)
    
[References](#ref)

<a name="back"> </a>

## Background
During the last couple of weeks, we have felt that most of the students at KTH struggle a little bit with the school right now, and feel that they don't really have control over their studies. One of the reasons is that the structure or the examination of the course may have changed due to the pandemic caused by COVID-19. Therefore, we wanted to create an app where KTH students could fill in how the courses have changed, and what type of examination they have now. By doing so, the students help each other stay updated with the course and its examinations.

<a name="app"> </a>

## The Application

The construction of the application COVID19 KTH Course Info is built by React and Firebase. React is a javascript framework created by Facebook, and Firebase is a web and mobile development platform created by Google. The application was developed to work primarily as an mobile app, but you can use it in your computer's web browser as well. Click on the [link](https://dd2482-covid19-course-info.firebaseapp.com) to see the mobile application COVID19 KTH Course Info in the web browser.

<a name="func"> </a>

### Functionality

#### COVID-19 Statistics
If you visit the [URL](https://dd2482-covid19-course-info.firebaseapp.com) for the application, you will enter the ``Home`` screen for the app. At the home screen, you will see the current numbers and statistics for the virus COVID-19, both in Sweden and in the rest of the world. The application fetch the COVID-19 data from the [NovelCOVID](https://github.com/novelcovid/api) API, so the numbers might be a little bit different compared to numbers on the [Public Health Agency of Sweden](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/bekraftade-fall-i-sverige/) web page.

If you want to see the current numbers for another country, you can add the country to the start page by clicking on the ``More`` symbol at the bottom of the screen and then ``Add countries``. In ``Add countries``, you can search for another country and then add their current COVID-19 data to the home screen of the application. 

#### KTH Courses
If you click on the button ``Courses`` at the bottom of the screen, you will get a list of some of the courses at KTH. Each course object contains the course code, the name of the course and how the course will be examined now due to the COVID-19. If you click on one of the courses, you will also get some more information about the picked course. If you want to update the information for the picked course, you can click on the ``three dots`` in the right corner at the top of the screen. 

If you want to submit a new course, click on the ``Submit`` button at the bottom of the screen. We have added some restrictions on how the new course submission should be structured:
* Course code should be 6 characters long and start with two letters
* You need to add some information about how the course is examined
* The course information cannot be longer than 60 characters.

If you don't fulfill these criteria, you will receive an error message with the information you need to add or change to be able to successfully make a submission.

<a name="dev"> </a>

### Devops Tools

#### Jenkins 
One of the intended learning outcomes for the course Automated Software Testing and DevOps DD2482, is that the student should be able to setup and deploy continuous integration. Therefore, we decided to try to create our own Jenkins server and integrate it with our COVID-19 project. 

We are running Jenkins as Docker container from the Blue Ocean Docker image. We have created two different pipelines. One is the main pipeline that are connected to the original GitHub repository for our project. The other one is a pipeline connected to the a forked copy of the original repository, which we use to test changes in the set up of the pipeline, or when we try to build new stages for the original pipeline.

Right now, we only have a Build stage in our main pipeline. Our Build stage install all necessary dependencies and package for our React application. If we continue to work with this project after the course has ended, we also want to create a Test stage and a Deliver stage. We have tried to fix a Deliver stage in the pipeline for our forked repository, but with no further success. If there are someone who has previous knowledge or experience with creating Jenkins' pipelines for a React/NodeJS application, we would like some help with our issue [#528](https://github.com/KTH/devops-course/issues/528).

Today, our Jenkins server is running locally on Johanna's computer. To get access to our Jenkins server, you need to go to [92.34.7.239:8080](92.34.7.239:8080) and log in with these credentials:

Username: test_user  
Password: Test2482

The server might not be up and running all the time, but down below we have a screencast of our Jenkins server in action. If the server is not up and running and you want to test our pipeline, please contact Johanna at jii@kth.se.

Click on the image below to be re-directed to the screencast at Youtube:

[![](/images/jenkins_screencast.png)](https://youtu.be/XFCERzBMqZc) 

The video has been cut at some points to shorten the length of the video and remove parts that does not add any new information to the filmed screencast. 

#### Firebase
Firebase is a serverless computing service, which provides a real-time database for it's users. Firebase provides an API that allows data to be synchronized across all the clients. The application data is stored on Firebase's own cloud.[[1]](https://en.wikipedia.org/wiki/Firebase) Serverless computing is relevant for DevOps, since it shortens the release cycle. By using a serverless architecture, the developers can focus on the functionality of the application and the application's GUI, instead of writing scripts for the server or the database. 
 
<a name="crit"> </a>

### Criteria for COVID19 Assignment

We aim to achieve at least these criteria:

**The contribution is related to COVID-19**
* A mobile and web application that helps KTH students stay updated on changes in examination due to COVID-19.

**The contribution is related to / built with DevOps technology**
* We have created our own Jenkins server, and built a small pipeline that is connected to our private repository for the application. We are also using Firebase in this project, which is a serverless computing service.

**The contribution is novel**
* We haven't found any application that is similar to ours yet. 

**The contribution is helpful**
* If the app uses properly, it is a good way for the KTH students to get an overview on how the courses has changed due to COVID19 and how the examination will take form. The examiners might use different channels to spread the information, and as a student it might be difficult to find that information because of that. By using this application, we can gather all information at one place and update the application as soon as something has changed. 
There a lot of courses at KTH, and some of them might have found a good solution to examine a course that usually has an exam that takes place in school. This application could also be used for examinars to see how other courses are handling the situation at get some inspiration.

**The contribution attracts support from other KTH students**
* Right now, our repository is private (because we have an API key in we don't want to make public if not necessary) but we could make it public or ask other students to contribute to the project. Either by submit a new course, update a existing one or help us develop and improve the application.

<a name="ref"> </a> 

### References

[1] https://en.wikipedia.org/wiki/Firebase




