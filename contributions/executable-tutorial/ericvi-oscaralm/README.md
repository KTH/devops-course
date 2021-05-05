# Exectuable tutorial: MLOps - Automation of Model Evaluation

# Members

Eric Vickström (ericvi@kth.se)

Github: vickstrom

Oscar Almqvist (oscaralm@kth.se)

Github: oscaralmqvist

# Proposal
Before pushing changes to the model, it is important to evaluate the model against certain datasets. For a given pull-request, we aim to compare the current version performance versus the version on the master branch. Hopefully, commenting the results on the pull-request itself with relevant statistics (classification rate etc.). 

Our executable tutorial will contain the following:
1. Github Webhooks - Check if an pull-request has been made.
2. DIY Server - Create an environment that evaluates the model with the proposed changes given in the pull-request.
3. Use the Github API  to make a comment on the pull request with the established classification rate.

# Submission

Here is the tutorial in written form as stated in the contract. 

[Tutorial (Github)](https://github.com/vickstrom/automation-of-model-evaluation)

We decided to extend our submission, by making the written tutorial interactive, to make it easier for TAs to grade and the possiblity of getting distinction.  

[Tutorial (Katacoda)](https://www.katacoda.com/vickstrom/scenarios/automation-of-model-evaluation) 