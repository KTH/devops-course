# open-source: Bug fixing for the open-source project act, submission on proposal #1172

## Members

Alexander Kruger: Email: alekru@kth.se Github: [alekru](http://github.com/thestar19)

Anders Renström: Email: renstr@kth.se Github: [renstr](http://github.com/Renstrom)

## Contribution

Course [PR](https://github.com/KTH/devops-course/pull/1423) 

Fixing bug issues for GitHub repository [act](https://github.com/nektos/act) 


Issue [#598](https://github.com/nektos/act/issues/598) Hard bug

Target [PR](https://github.com/nektos/act/pull/628)


Issue [#597](https://github.com/nektos/act/issues/597) Easy bug

Target [PR](https://github.com/nektos/act/pull/637) 

## Self-assessment based on the courses guidelines:

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The contribution fixes bugs | Yes | | hard bug |
|The contribution improves documentation |  | No | |
|The contribution adds new features |  | No  |  |
|The contribution is much appreciated by the community | Yes, requested by community |  | |

## Motivation for self-assessment

Issue 598 had an issue with the yaml decoder of the string format which removed the quotes when converting to string. First solution was to find a way to avoid this by using some yaml flag, but this didn't seem to work. Secondly, we created a temporary file in order to fix this solution without touching the main file, but upon criticism of creating a temporary file, this solution had to be changed. The new solution instead changed the interface of the if type to yaml.node and uses regexp to fit the correct format given in the yaml.node. 
This is why we think this is a hard bug

Issue 597 had a wrongful order of operations which caused the fields to be evaluated in the wrong order. This was easily fixed since issue 598 was worked on before 597, which made it easy to know what we were looking for. 
