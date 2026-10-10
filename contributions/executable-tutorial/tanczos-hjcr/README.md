# Assignment Proposal

## Title

Feature Flags with OpenFeature and flagd

## Names and KTH ID

  - Barnabas Tanczos (tanczos@kth.se)
  - Henrique Ramalho (hjcr@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

We propose an executable tutorial about feature flags using OpenFeature and flagd. It will run on Killercoda in a standard Ubuntu environment.

The learner will start with a small Python web app that contains a new feature that has been deployed but is not yet visible. The app reads flags through the OpenFeature SDK and flagd runs as the flag provider using a configuration file. Using the terminal and browser, the learner will complete these steps:
1. Start the app and observe that the feature is switched off.
2. Turn the feature on by editing the flags without redeploying.
3. Add a targeting rule so that only internal users (identified by an attribute in the evaluation context) see the feature.
4. Add a variant-based flag with a percentage-based rollout for A/B testing.

The tutorial starts with a problem statement. Each step will include an explanation and justification, including visuals where appropriate. Lastly, there is a reflection section on when feature flags are useful, who should use them, and how they fit into continuous delivery alongside other strategies.

**Relevance**

Feature flags are an important technique in continuous integration and deployment, as they allow features to be activated and deactivated without redeploying. They are also useful for quickly recovering from failure and for experimentation with real users. The executable tutorial will cover the advantages and disadvantages of this technique, and contrast it with other methods like canary deployment.
