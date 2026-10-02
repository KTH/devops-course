# Assignment Proposal

## Title

MLOps evaluation and quality gate pipeline with self-labeling simulation and data-poisoning detection

## Names and KTH ID

  - Harry Eriksson (guerikss@kth.se)
  - Villiam Riegler (villiamr@kth.se)

## Deadline

Week 4

## Category

Demo

## Description

We demonstrate a minimal MLOps pipeline that extends a traditional CI/CD workflow with automated evaluation of a machine-learning model. A small web application using a physics-based 3D dice simulator built with [three.js](https://threejs.org/) and the [Rapier](https://rapier.rs/) physics engine generates trusted data (dice rolls). Because the app controls the physics, it knows the true outcome of every roll, so a [Playwright](https://playwright.dev/) script can produce an unlimited labeled image dataset with no manual labelling. Rolls are fully reproducible, due to using a determimistic seed. A small image classifier learns to predict the die's top face from pixels alone, and is evaluated with tests in the CI stage. Crucially, that test set is generated and labeled by the trusted physics oracle, independently of the training data, so it stays a reliable reference. If accuracy on it falls below a defined threshold, or below the currently deployed model, the pipeline fails and blocks deployment, turning the test into an automated quality gate.

In the demo we will:
- Generate a labeled dataset from the app, train the classifier, and show the pipeline passing (accuracy above threshold) and proceeding to deployment / model registration.
- Introduce data poisoning by introducing faulty labels into the training set — emulating malicious or low-quality user feedback. The retrained model scores below threshold on the clean test set, so the gate blocks it.
- Discuss the implications and feasibility of such a quality gate in the pipeline.

**Relevance**

Machine-learning models are increasingly embedded into production software, and many are retrained on data or labels supplied by users, which makes them vulnerable to poisoning: a few incorrect or malicious labels entering the training set can silently degrade behavior for everyone. Shipping retrained models without automated evaluation therefore risks that degradation reaching production. Treating model evaluation as an automated, versioned quality gate in CI/CD extends established DevOps practices — continuous testing, fast feedback, and reliable, gated releases — to ML-powered features. Because the gate is anchored to a trusted, isolated evaluation set that untrusted data cannot influence, it makes an often-invisible failure mode — poisoning from untrusted feedback — observable and testable end to end, which is directly applicable to any pipeline that retrains a model on user-supplied data.
