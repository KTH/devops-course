# Tutorial: Continuous benchmarking using Github Actions

## Members ##
* Johan Hammarstedt (johhamm@kth.se), Github: [jhammarstedt](https://github.com/jhammarstedt)
* Carl Leijonberg (carllei@kth.se), Github : [carllei](https://github.com/carllei)

## Task
This project was aimed to teach others how to setup a github action with continuous benchmarking using pytest and visualizing it with github pages. 

This will help developers easily compare benchmark results and alert on worse performance when making a new commits. The statistics from the latest run is found in `output.json` and the historical comparission table is visualized in the generated page available [here](https://jhammarstedt.github.io/Benchmarking-DevOps/). 

## Relevant links
* Katacoda tutorial is found [here](https://www.katacoda.com/jhamm/scenarios/ghactiondemo)
* Project repository is found [here](https://github.com/jhammarstedt/Benchmarking-DevOps)
* First PR is found [here](https://github.com/KTH/devops-course/pull/1158)


## Description and usage (when not running the tutorial)
To try this project out (if not running the tutorial) simply fork this repository and create a commit. 

Ideally you would change the [benchmarking.py script](https://github.com/jhammarstedt/Benchmarking-DevOps/blob/master/src/benchmarking.py) since that will give different performance results. We have 2 test functions, a slower `turtle` and faster `cheetah` which are just used to test the benchmarking. So try to change:

line 22: `benchmark(turtle)` --> `benchmark(cheetah)`

Commit this, get some results, and then change back and commit again to see the difference. 

* The workflow file is found in [`.github/workflows/python.yml`](https://github.com/jhammarstedt/Benchmarking-DevOps/tree/master/.github/workflows)
* The configurations for the webpage is found in [docs](https://github.com/jhammarstedt/Benchmarking-DevOps/tree/master/docs)
* All python scrips are found in [`src`](https://github.com/jhammarstedt/Benchmarking-DevOps/tree/master/src)


### Clean the html table

If you want to reset the table simply run
```./scripts/clear_table.sh```

## Easter egg hint for Katacoda tutorial

<details> 
  <summary>Click me for hint</summary>
  Did you collect the 🥚 from scripts?
</details>

## Grading table

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) | Yes | No | 👍In the browser |
|If local execution, runs on Linux | Yes | No | Easy to setup and run  |
|The tutorial gives enough background | Yes | No |👍 Comprehensive background |
|The tutorial is easy to follow  | Yes | No |👍 Well documented |
|The tutorial is original, no such tutorial exists on the web | Yes | No | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | Yes | No |👍 Subtle and fun |
|The tutorial is successful (attracts comments and success) | Yes | No | Lively discussion |
|The language is correct |👍 Yes | No | Interesting narrative  |



## Future work
* Add support for more languages



