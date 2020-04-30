# Demo #

CI/CD pipeline for iOS application using micresoft Azure and Appcenter

### Members ###
* Muhammad Jahangir Zafar (mjza@kth.se), 
* Gibson Chikafa (chikafa@kth.se)
* Nagasudeep Vemula (vemula@kth.se)


### Details ###
We will implement a CI/CD pipeline using Microsoft Azure and AppCenter. In this demo we'll develop small iOS application for movies search using tvmaze api's. Pipeline will use azure repo actions to set up an environment, build, test on real devices provided by microsoft app center and if all tests will succeed then send build to specified group of testers.

### Motivation ###
Distribution of iOS application for test flight beta testers is very time consuming. We have to add tester device in apple developer account and then add these devices in provisioning profiles then tester can install application on his device. Microsoft Azure has solved this problem for the testers. It'll automatically add device in apple developer account and install provisioning profile automatically on the tester device. Another motivation to use Microsoft Azure is that it provides real devices for testing. You don't have to buy all iOS devices, you just need to select devices on which you want to test the application. 


### What we cover ###

* CI/CD Pipeline Configuration
* Testing on Real Devices
* Adding Distribution Group and iPhone devices
* Send Build to defined beta tester group

