
# Feedback on #1371
Members:
Alexander Kruger @thestar19 alekru@kth.se

[Feedback proposal #1225](https://github.com/KTH/devops-course/pull/1225)
[Essay submission](https://github.com/KTH/devops-course/pull/1371)
## Summary:
From an overall standpoint, the tutorial was interesting and well done. The only major problem was being forced to enter a creditcard number without context. In a world where scammers constantly try and steal your cookies, this part would be better with some reassurance from the tutorial. 
The readme from the folder seems underutilized. Information that was hard to include in the tutorial or a small easter egg could be placed there. Links to helpful pages or further information for those that want it could be placed here.
### Step 1
When opening the tutorial, the first part of the tutorial is really interesting and well written. The way the tutorial is structured makes it seem like an adventure and really contributes to the way it spins a tutorial into something more fun. If we are to really nitpick, it would be a good addition to mention what GCP stands for; assuming that the user knows at least something about GCP is reasonable but is the only complicated technology not mentioned.
### Step 2
Step 2 starts out with a problem. When registering an account for GCP, a credit card is required. For any previous Android user or Google Play developer, this step should not be a challenge but still represents a problem. Entering your credit card details, regardless of the reassuring logo of Google, still makes my internal alarms go off. The link presented in the tutorial with little to no background makes the alarms worse, especially because the website could be made to look like Google. Here it could be helpful to include more information about why google requires the credit card, how they are going to use it and ways to corroborate that the user is in fact going to right website. This verification could be in the way of recommending the user on what to google to get more information about the project or simply linking a guide about how to understand the SSL certificate.
### Step 3
Step 3 continues with presenting the adventure theme where the user moves through the tutorial like  a hero in a story. The tutorial assume familiarity with basic terminal tools such as simple file editors such as nano. The styling is excellent and provides a professional look. Unfortunately, the editing of files quickly becomes messy and complicated. An example of this can be seen when you need to change some parts of the variable.tf file. The instructions tell you to change the gcp_credentials which “is the directory of the file storage”. This could better explained by including a clear reference to the key obj created previously. The line “Change them to match your project, credentials, and service accounts.” makes this confusion worse by adding more unclear information to the mix. If it refers to other parts of the tutorial, a simple pointer such as mentioned above or simply asking the user to take note in a third party program such as Notepad++ of the paths needed later for example would go a long way to make this section more clear.
With that in mind, seeing your cluster running was fascinating at the very end. Including these kinds of pulls back to reality is great for making the user take a step back from the file system and recognize progress, even if it might seem like a minor step.
### Step 4
Moving from the complicated mess of editing the config files, step 4 is straightforward and interesting. A potential addition would be to explain the files deployment.yaml etc further by briefly walking through their structure and effect. Nothing in this world was as tempting as writing “kubectl apply -f your-specific-file”  when it said that I shouldn’t.
### Step 5
This part was interesting and the configuration file included great comments about it’s structure and effect. I also got stuck here for quite a while with the error 400 googleapi until the problem seemingly fixed itself. The small paragraph at the end was confusing: What does it mean to set the container to public? The google page included many warning and therefore made it harder to understand what the correct steps where. 
### Step 6
Having most of complicated stuff behind you, step 6 was really great moment. I really wish that some pictures were included, perhaps in a separate picture folder in the starting directory if images are hard to add to the left side tutorial part.  The ending on step 6 “If you copy that IP address you will be able to your counter application running” was a letdown as I did not at all understand what I was supposed to do.
### Step 7/8
Step 7 & 8 finished up a really interesting tutorial. I wish that the tutorial ended with potential other tutorials to follow or recommendations about where to go next. A link to an appropiate next step at https://www.katacoda.com/courses/kubernetes would be great or kubernetes own tutorial https://kubernetes.io/docs/tutorials/kubernetes-basics/. 

