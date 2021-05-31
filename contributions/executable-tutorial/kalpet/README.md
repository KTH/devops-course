# (Repeat)Executable tutorial: CI workflow for C++ project using Travis CI and CxxTest for automated building and testing

## Members
Kalle Pettersson (kalpet@kth.se) Github: [kallepettersson](https://github.com/kallepettersson)


## Proposal
I will create a [Katacoda](https://www.katacoda.com/) executable tutorial including:
* Creating a simple C++ project
* Writing unit tests using the CxxTest framework 
* Creating a Travis CI server 
* Creating a CI pipeline that automatically builds and tests the project on every push

## Katacoda link 
The old tutorial can be found here: [link](https://www.katacoda.com/kalpet/scenarios/executable-tutorial-dd2482)

The new tutorial can be found here: [link](https://www.katacoda.com/kalpet/scenarios/repeat-executable-tutorial)

## GitHub links

- [GitHub - Katacoda branch](https://github.com/KallePettersson/katacoda-scenarios)
- [GitHub - Tutorial project](https://github.com/KallePettersson/devops-executable-tutorial/tree/tutorial-start)
- [GitHub - Complete Tutorial project](https://github.com/KallePettersson/devops-executable-tutorial/tree/tutorial-complete)
- [GitHub - Extended Tutorial project](https://github.com/KallePettersson/devops-executable-tutorial/tree/main)


# Tutorial outline
1. Before you start
2. Creating a simple C++ project
3. What is CxxTest?
4. Writing CxxTests
5. Running CxxTests
6. What is Travis CI?
7. Continuous Integration with Travis CI


## Grading - I strive to meet the following grading criteria
|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) | X |  |  |
|If local execution, runs on Linux |  |  |   |
|The tutorial gives enough background | X |  | X |
|The tutorial is easy to follow  | X |  |  |
|The tutorial is original, no such tutorial exists on the web |  |  |  |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | X |  |  |
|The tutorial is successful (attracts comments and success) | |  |  |
|The language is correct | X |  | |

-----

## Repeat feedback and changes:
### Criteria that can potentially be met(From feedback):
* background - though the code has been explained in detail, more information about CxxTest and Travis CI is necessary for this task
    * Added two background sections in the tutorial explaining more about what CxxTest and Travis CI is and how they work.   
* easy to follow - the tutorial can be made more modular, and can be presented in a more engaging way, involving more Katacoda features (file navigator, cloning a fork from the terminal, all within Katacoda)
    * Made the tutorial more modular, from 3 big steps to 9 smaller ones.
    * Removed the use of vim and instead used the file navigator feature.
    * Used more KataCoda features such as `Copy to editor` code and executable commands.   
    * Changed so that a user has to fork the repo to follow along to the tutorial

### Other improvements(From feedback)
* Strengthen the link to DevOps.
    * Added a paragraph in the intro page to streangthen the link to devops
*  Break the tutorial down into smaller steps, instead of three very big steps.
    * Made the tutorial more modular, from 3 big steps to 9 smaller ones.
*  Use the interactive features of Katacoda. For example, it would be better to ask the user to clone a fork of the sample application within Katacoda, then use Katacoda’s file navigator to explain the code.
    * Used more Katacoda features

### My extra improvements 
* Added an Easteregg to the tutorial
