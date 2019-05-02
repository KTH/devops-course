const data = [{
                id: 0,
                text: "It's the start of a new week. You arrive at work on time monday morning and settle in for the day. What is the first thing you do to settle in?",
                responses: [
                    {
                        text: "Sit down at your work station and get started for the day. You have lots of work to do.",
                        type: "end",
                        goto: 0
                    },
                    {
                        text: "COFFEE!!!",
                        type: "continue",
                        goto: 1
                    }
                ]
            },
            {
                id: 1,
                text: "Now that you're all energised from the coffee you sit down at your workstation and get to work. You notice lots of complaints about a bug found in production. You quickly learn what and who caused said bug. What do you do with the culprit?",
                responses: [
                    {
                        text: "Ask him how the bug got into production.",
                        type: "continue",
                        goto: 2
                    },
                    {
                        text: "Tell him to fix it",
                        type: "moreInfo",
                        moreInfoText: 0,
                        goto: 2
                    }
                ]
            },
            {
                id: 2,
                text: "The co-worker tells you he forgot to run a test prior to him pushing it to production. How do you respond to his mistake?",
                responses: [
                    {
                        text: "Gather a team meeting to discuss the issue further to ensure this doesn't happen again.",
                        type: "continue",
                        goto: 3
                    },
                    {
                        text: "Remind him how important testing is before pushing code to production.",
                        type: "continue",
                        goto: 13
                    }
                ]
            },
            {
                id: 3,
                text: "During the meeting, a fellow co-worker mentions that the team could implement automatic testing to avoid the scenario in the future. Do you agree with your co-corker?",
                responses: [
                    {
                        text: "No, the testing we do at the moment is fine. As long as the developers actually run the tests.",
                        type: "continue",
                        goto: 4
                    },
                    {
                        text: "Yes, you task the team to begin implementation immediately.",
                        type: "continue",
                        goto: 4
                    }
                ]
            },
            {
                id: 4,
                text: "The team meeting comes to an end and you go back to your workstation. Soon after you've settled into work again you receive a message from a co-worker stating that a product is not working on their machine. How do you respond to this complaint?",
                responses: [
                    {
                        text: "You say it's probably nothing and advice them to reboot.",
                        type: "moreInfo",
                        moreInfoText: 1,
                        goto: 6
                    },
                    {
                        text: "You proceed to check that the software works from your machine.",
                        type: "continue",
                        goto: 6
                    }
                ]
            },
            {
                id: 5,
                text: "You find the software is broken on your machine too. You track down who was the cause of the breakage. What do you do next?",
                responses: [
                    {
                        text: "Gather another team meeting to discuss the issue further.",
                        type: "continue",
                        goto: 3
                    },
                    {
                        text: "Remind them how important testing is before pushing code to production.",
                        type: "continue",
                        goto: 13
                    }
                ]
            },
            {
                id: 6,
                text: "As the team implemented automated testing, the software works as expected on your machine. You and your co-worker open config files to find the cause of the issue. You find that a Python version is out of date when compared to your machine. Do you update this old version?",
                responses: [
                    {
                        text: "Yes, update the software on the co-worker's local workstation.",
                        type: "continue",
                        goto: 7
                    },
                    {
                        text: "No, don't update it. He'll find a way to fix the code locally.",
                        type: "continue",
                        goto: 7
                    }
                ]
            },
            {
                id: 7,
                text: "You have to attend a meeting now for another project and leave your desk for an hour. When you return, you find three more complaints about software not working as expected on their local workstations. How do you go about this issue?",
                responses: [
                    {
                        text: "Assume it's the same issue as before and tell those co-workers to adapt their code or update the Python version themselves.",
                        type: "continue",
                        goto: 8
                    },
                    {
                        text: "Get the team together and explain the issues that have been raised.",
                        type: "continue",
                        goto: 9
                    }
                ]
            },
            {
                id: 8,
                text: "This update fixes the local environments for two out of the three co-workers who had raised the issues. The final co-worker however, is still having issues with is code. Do you explore config files again?",
                responses: [
                    {
                        text: "Yes, compare his config files to yours again.",
                        type: "continue",
                        goto: 11
                    },
                    {
                        text: "No, there must be a solution to avoid this issue.",
                        type: "continue",
                        goto: 12
                    }
                ]
            },
            {
                id: 9,
                text: "Throughout the discussion many solutions are raised and advice is given. Along with the following two. Which one should you choose?",
                responses: [
                    {
                        text: "Simply not install newly updated versions of software.",
                        type: "continue",
                        goto: 10
                    },
                    {
                        text: "Standardise software versions across the project.",
                        type: "end",
                        goto: 5
                    }
                ]
            },
            {
                id: 10,
                text: "You tell the team to not update to newer versions of their current software in the future. What are your final instructions before getting back to your work?",
                responses: [
                    {
                        text: '"Everyone get their workstations working locally."',
                        type: "end",
                        goto: 4
                    },
                    {
                        text: '"I\'ll come around and update all the workstations that are not working so you can continue your work."',
                        type: "end",
                        goto: 3
                    }
                ]
            },
            {
                id: 11,
                text: "You dive into the config files but don't see anything more you can do. What do you want to try next?",
                responses: [
                    {
                        text: "You must not be looking hard enough, compare his configs to yours again.",
                        type: "continue",
                        goto: 11
                    },
                    {
                        text: "No, there must be a solution to avoid this issue.",
                        type: "continue",
                        goto: 12
                    }
                ]
            },
            {
                id: 12,
                text: "You discuss the issues with a supervisor of the project and he suggests using containerisation. You know of this concept but have never used it in practice before. How do you respond to his suggestion?",
                responses: [
                    {
                        text: '"We have some other ideas that could work. Thanks anyway."',
                        type: "end",
                        goto: 1
                    },
                    {
                        text: '"That sounds great. I\'ll bring it up with the team."',
                        type: "end",
                        goto: 2
                    }
                ]
            },
            {
                id: 13,
                text: "He gets the message and says it won't happen again. </br></br>You get back to your work. Soon after you've settled into it again you receive a message from a co-worker stating that a product is not working on their machine. How do you respond?",
                responses: [
                    {
                        text: "Check that the software works from your local machine.",
                        type: "continue",
                        goto: 5
                    },
                    {
                        text: "You say it's probably nothing and advice them to reboot.",
                        type: "moreInfo",
                        moreInfoText: 1,
                        goto: 5
                    }
                ]
            }];


const endCases = [{
                    id: 0,
                    text: "Don't try to get through the day without coffee. You're a developer, you need your coffee.",
                    successfulPath: false,
                },
                {
                    id: 1,
                    text: "You never figure out the problem, disaster. You waste valuable time on the issue.",
                    successfulPath: false,
                },
                {
                    id: 2,
                    text: "You bring up the idea of containerisation with your team and they love it. </br> It's getting to the end of the working day but you make a work item to begin plans on containerising the project right away. </br>Great Work. You had a successful work day.",
                    successfulPath: true,
                },
                {
                    id: 3,
                    text: "That's great that you're fixing everyone's workstations but this method is just a bandaid. You're going to have to update versions at some point in the future.",
                    successfulPath: false,
                },
                {
                    id: 4,
                    text: "This might involve individuals updating their software on their own but they may also adapt the code on their local workstation to work on their version which when pushed onto the server, may break on other worker's workstations. Not a great solution in the long run.",
                    successfulPath: false,
                },
                {
                    id: 5,
                    text: "You bring up the idea to standardise software versions throughout the project with your team and they love it. </br> It's getting to the end of the working day but you make a work item to begin plans on standardising software within the project right away. </br>Great Work. You had a successful work day.",
                    successfulPath: true,
                }];

const moreInfo = ["Using the information you gave him, he realises what he did and comes back and tells you what he did.",
                  "The co-worker reboots and comes back to you. He says it still is not working so you test the broken software on your local machine."];