# Tutorial: Continuous benchmarking using Github Actions
<img src="https://www.maxi-muth.de/wordpress/wp-content/uploads/2014/09/Professortocat_v2.png" height = 100 width = 100 align ="right" />

## Authors ##
* Johan Hammarstedt (johhamm@kth.se), Github: [jhammarstedt](https://github.com/jhammarstedt)
* Carl Leijonberg (carllei@kth.se), Github : [carllei](https://github.com/carllei)

## Relevant links
📚 Katacoda tutorial is found [here](https://www.katacoda.com/jhamm/scenarios/ghactiondemo)

🗝 Project repository is found [here](https://github.com/jhammarstedt/Benchmarking-DevOps) 

📣 First PR [#1158](https://github.com/KTH/devops-course/pull/1158) 

📝 Feedback is found in this PR [#1358](https://github.com/KTH/devops-course/pull/1358) and modifications are found in the `Feedback_adjustments.md`


## Task
This project was aimed to teach others how to set up a Github Action to create continuous benchmarking with pytest. We also added a simple visualization with Github Pages that we walk through briefly in the tutorial. 

This will help developers easily compare benchmark results and alert on worse performance when making new commits. The statistics from the latest run are found in `output.json` and the historical comparison table is visualized in the generated page available [here](https://jhammarstedt.github.io/Benchmarking-DevOps/). 

<img src="https://www.katacoda.com/images/logo-head.png" align="right" />

## Katacoda tutorial
We have created a katacoda tutorial that runs a bash terminal and a VS code environment in the browser. It walks through every step to build and set up this repo yourself. 

You will learn how to: 
* Create simple Github Action that will let you test and compare python scripts on pushes to your GitHub repository
    * With a few modifications, you can also implement them for other tasks to enable CI/CD in your other projects!
    * You can also use this action with similar performance tools for other programming languages.
* Create your first Github Page that will display the results from your testing

<img src="https://github.com/jhammarstedt/katacoda-scenarios/blob/main/ghactionDemo/images/Summary_tutorial.PNG?raw=true" />

## Aiming for --> 💥  Distinction  (Extra header for DevOps course)

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) |💥  Yes | No |💥  In the browser  |
|If local execution, runs on Linux | Yes | No | Easy to setup and run  |
|The tutorial gives enough background |💥  Yes | No | 💥 Comprehensive background |
|The tutorial is easy to follow  |💥  Yes | No | 💥 Well documented |
|The tutorial is original, no such tutorial exists on the web |💥 Yes | No | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) |💥 Yes |  No |💥 Subtle and fun |
|The tutorial is successful (attracts comments and success) |💥  Yes | No | Lively discussion |
|The language is correct | 💥 Yes | No | 💥 Interesting narrative  |


## Easter egg hint for tutorial

<details> 
  <summary>Click me for hint</summary>
  Did you collect the 🥚 from scripts?
  <details>
  <summary> Fun fact regarding easter egg (open after finding it) </summary>
    The author of the action did not support memes by repo owners, which would be a problem for our purpose. So I raised that
   <a href="https://clipart.world/wp-content/uploads/2020/09/Colorful-Easter-Egg-clipart-transparent.png" target="_top">issue</a> and got a new feature merged for this tutorial 🤙
    
  </details>
</details>


## Future work
* Add support for more languages
