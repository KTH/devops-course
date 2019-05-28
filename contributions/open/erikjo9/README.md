# Improving slack notification plugin for Jenkins

The [slack notification plugin](https://github.com/jenkinsci/slack-plugin) is a Jenkins plugin that allows sending
build notifications to slack. It supports traditional "free style" build project as well as pipelines, however the
functionality is very limited when used in pipelines.
When using the plugin in a free style project the notifications may include information like build status (pass/fail/etc),
test results and commits. But when using the "slackSend" step supported in pipelines you are only able to send messages
that you have to format yourself using much knowledge about the slack API.
I intend to create a prototype improvement to the plugin by adding a new pipeline step called "slackNotify" that has support
for build information like the plugin has for free style projects. I do have experience in Jenkins before but I have not
worked much with plugins before. The steps I intend to finish are:

1. Fork the repository and create a feature branch
2. Create the new pipeline step called "slackNotify"
3. At support for build status at least. Optionally also test result and commit info.
4. Add at least one unit test to the new pipeline step
5. Install and test the improved plugin on a local Jenkins instance (also needed for testing)

[Prototype repository](https://github.com/netrounds-erik/slack-plugin/tree/slack-notify)
