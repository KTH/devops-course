# Tutorial: Continuous integration with Jenkins and Blue Ocean 

 - Keivan Matinzadeh keivanm@kth.se @keivanm
 - Alexander Volminger alevol@kth.se @Volminger
 
 ## Description
We will show how to setup a pipeline using Jenkins with Blue Ocean for a Java project. We will first show how to setup and install Jenkins with Blue Ocean. We will after that show how to setup a pipeline  that is triggered each time a user commits to the connected github repository containing the Java application. We will then show how to add a testing stage to the pipeline. The pipeline will either fail or succeed if the code passes the tests. The tutorial will go through both scenarios, because the build will fail from the start so the user needs to fix the Java code to be able to make the build succeed.

We aim to do this tutorial using https://www.katacoda.com
