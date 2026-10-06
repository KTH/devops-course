# Assignment Proposal

## Title

Detection as Code: Testing and Deploying Falco Runtime Security Rules in Kubernetes

## Names and KTH ID

- Vilhelm Prytz (vprytz@kth.se)
- Samouil Mosios (samouil@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We will create an executable [Killercoda](https://killercoda.com) tutorial that shows how runtime security fits into the DevOps workflow. Attacks on a running Kubernetes workload are detected with [Falco](https://falco.org/) and routed with [Falcosidekick](https://github.com/falcosecurity/falcosidekick). The detection rules are managed like application code: versioned in Git, tested automatically and rolled out by a pipeline. The alerts are then used to fix the application itself.

The tutorial runs on Killercoda's two-node Kubernetes playground and needs no local installation or paid account. A background setup script installs pinned versions of Falco, Falcosidekick and the Falcosidekick web UI with Helm, deploys a small, deliberately vulnerable web application, creates a local Git repository for the detection rules, and waits until Falco is running on every node. A Git hook in that repository runs the pipeline, standing in for a hosted CI service so that no GitHub account is needed. We have already verified that Falco 0.45.0 runs in this environment with its default modern eBPF driver.

The learner will:

- Exploit the application (for example, through a command injection) and see Falco's default rules flag each action together with the affected pod and namespace, and the alerts reach the web UI and a webhook receiver through Falcosidekick.
- Follow how an event travels from a system call, through Falco's kernel driver and rule engine, to Falcosidekick and its outputs.
- Write a custom rule for the application together with a test case for it, and push it. The pipeline validates the rule, deploys it with `helm upgrade`, and uses Falco's [event-generator](https://github.com/falcosecurity/event-generator) to perform the suspicious actions and check that Falco raised the expected alerts. If the tests fail, the pipeline rolls the rules back.
- Push a broken rule and a rule that no longer fires, and see the pipeline stop both. Then tune a false positive by adding an exception for a legitimate process, through the same pipeline.
- Close the loop: use the alert details to find the vulnerability, fix the application, redeploy it, and run the attack again to confirm that it fails and no alert is raised.

The tutorial will state its intended learning outcomes at the start and include an architecture diagram of the components (application, Falco DaemonSet, kernel driver, Falcosidekick and its outputs, rules repository and pipeline). It will discuss design decisions such as the choice of driver, running Falco as a privileged DaemonSet, testing rules before and after deployment, and how the local pipeline maps to a hosted CI service such as GitHub Actions. It will also discuss limitations: Falco only sees events once it is running, tests only cover the attacks someone thought of, rules need tuning to avoid alert fatigue, Falco needs access to the host kernel (so it cannot run on platforms such as AWS Fargate), and it detects attacks rather than preventing them.

**Relevance**

Build-time checks such as image scanning and admission policies catch known problems before deployment, but they cannot see what a container actually does once it runs, for example when an attacker exploits an unknown vulnerability. Runtime security monitoring closes this gap and is a core part of DevSecOps. The tutorial applies core DevOps practices to it. Detection rules are kept as code and go through the same automated test and deploy pipeline as the rest of the system, so a broken rule, or one that silently stops firing, is caught before anyone relies on it. The team that owns the application also owns its rules, instead of handing security to a separate team. Finally, alerts from production feed back into development, which is the monitoring-to-code feedback loop at the centre of DevOps.
