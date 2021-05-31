# Demo Submission After feedback: Automatically generate Python unittest results in HTML reports with Jenkins

## Members

Name: Sihan Chen,  Yuehao Sui

Mail: sihanc@kth.se, yuehao@kth.se

Github: Spycsh, amaothree

## Link

[Video](https://www.youtube.com/watch?v=VDmBfglO6YQ)

[GitHub repo related to the Video](https://github.com/Spycsh/python-unittest-htmlTestRunner-jenkins-demo)

[Another Take-home repo](https://github.com/Spycsh/python-unittest-htmlTestRunner-GitHub-Action-demo)


## Description
The demo will show how to automatically generate and visualize Python unittest results in HTML reports with Jenkins. The essential component to elegantly show the testing results in HTML reports is [HTMLTestRunner](https://github.com/SeldomQA/HTMLTestRunner), which is a non-trivial project itself and yield elegant HTML testing results for testers. The video will provide a simple example to show how it can be intergrated into Jenkins in a CI testing flow.

## Motivation
This is quite relevant to DevOps because jenkins is widely used for CI but there is no native support to generate HTML testing report for Python unittest. We hope this video demo will clearly show the whole flow.

## Criterias that we are aiming for

* The demonstration is clearly motivated
    - yes, as explained in the Motivation above

* The demonstration is difficult to do
    - yes & remarkable, because it is not easy to do from scratch and it depends on non-trivial infrastructure [HTMLTestRunner](https://github.com/SeldomQA/HTMLTestRunner) which is co-contributed by us. This infrastructure offers elegant HTML templates and also the mail support and the functionality to render testing results on the HTML. It is difficult to build it from scratch and there are no native support of such HTML template on Jenkins.

* The demonstration is original
    - yes & remarkable, although there are some videos on publishing HTML on jenkins, most of them are based on JUnit rather than python unittest. We also write our own [GitHub](https://github.com/Spycsh/python-unittest-htmlTestRunner-jenkins-demo) to show the whole flow and we promise that is original and non-duplicated.

* The video is sublime (eg. visually appealing)
    - yes, and HTML report is internally visually appealing than console output:)

* The video contains an easter egg
    - No

* There is a code repo to run the demo
    - yes & remarkable, see [GitHub](https://github.com/Spycsh/python-unittest-htmlTestRunner-jenkins-demo), the code repo is with a solid readme

* The video must contain subtitles which are clear and in proper English, and clear voice
    - yes & remarkable

* The video includes a take-home message
    - yes & remarkable, because you can deploy the whole flow on your own jenkins with the steps we wrote in README Of our [GitHub](https://github.com/Spycsh/python-unittest-htmlTestRunner-jenkins-demo), and there is also a take-home project you can try it out about how to use GitHub Action rather than jenkins to do the same things 
[Another Take-home repo](https://github.com/Spycsh/python-unittest-htmlTestRunner-GitHub-Action-demo).

