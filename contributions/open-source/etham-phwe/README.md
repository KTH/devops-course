# Open-Source Proposal

## Members
1. Emelie Tham (etham@kth.se)
2. Philip Wester (phwe@kth.se)

## Proposal
Creating a [SaltStack]{https://github.com/saltstack/salt} Slack bot. 

## Description
SaltStack supports a SecOp orchestration of the DevOps toolchain by acting as a configuration manager as well as allow for remote execution. 

We want to create a Slack bot that will notify the user of the result of SaltStack's state runs. If time permits, perhaps allow sending commands from Slack as well. As of now, SaltStack has an API that allows for Slack integration, however, there seems to be no bots that make use of it. A slack bot would be preferable instead of directly calling the SaltStack API. This is because of two main reasons:
1. It is easier to communicate with a bot than with the API.
2. We can configure the presenting format from the bot to suit the user needs. (ie. include extra/less information, highlight important parts).

This implementation will be written in Python with the API of the open-source community Salt software.
