
# Executable Tutorial: CI Notification 

## Members
Name: Eric Vickström 

Mail: ericvi@kth.se 

Github: vickstrom

Name: Oscar Almqvist 

Mail: oscaralm@kth.se 

Github: oscaralmqvist 

## Proposal:

CI Server that notifies developers about pull-request via an application such as Slack.

## Proposed Solution

Github repo explaining the following process in detail:

1. Show how to create a webhook that listens on pull request in Github.
2. Create a simple Web server that recieves the PUSH event from the webhook
3. Connect to Slack API and output an message to a specific channel  
  
Possible extensions could be tailored messages depending the metadata in the pull-request. For example, examining the labels at categorising them into different channels, such as #developer, #webdesign.

