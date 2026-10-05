# Assignment Proposal

## Title

Zero-Downtime Changes with Terraform Lifecycle Management

## Names and KTH ID

- Pavlos Spanoudakis ([pavloss@kth.se](mailto:pavloss@kth.se))
- Dimitrios Bakalis ([bakalis@kth.se](mailto:bakalis@kth.se))

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This executable tutorial demonstrates how to replace infrastructure without causing downtime, using Terraform lifecycle rules. It runs on Killercoda in the browser and requires no cloud credentials.

By default, when Terraform must replace a resource, it destroys the old one and then creates the new one. For a service behind a load balancer, the gap between the two actions is an outage, even though `terraform apply` reports success. The tutorial first **measures** this outage and then removes it step by step.

The tutorial is a single repository containing one Killercoda scenario. The environment consists of:

- **An nginx load balancer** in front of the application containers.
- **A stateless application container** (built locally, with a simulated slow start) that is upgraded repeatedly. It keeps no data itself; from step 6 it reads and writes values in the data store.
- **A stateful data store (Redis) with a volume**, added in step 6.
- **A traffic generator** outside Terraform that sends about 10 requests per second and counts failed requests, so every change is checked against "real" traffic.

The learner works through the following steps. Steps 2 to 5 each end with a measurement on a scoreboard:

1. **Baseline:** deploy the stack with Terraform and start the measurement.
2. **Observe the outage:** upgrade the image version with the default destroy-then-create behaviour and read the plan that predicts the outage.
3. **`create_before_destroy`:** fix the replacement order, run into a resulting name collision, and solve it with a unique name per release.
4. **Health checks:** add a health check and `wait = true`, so the old container is only removed once the new one is actually ready.
5. **`replace_triggered_by`:** handle a config file change that Terraform cannot see on its own.
6. **`prevent_destroy`:** store a value through the application, lose it in a simulated accident, then protect the data volume and repeat the accident. This shows why the overlap approach used for the application must not be used for stateful resources.
7. **Reflection:** compare the results on the scoreboard and discuss potential use cases, limits and alternatives, using questions with collapsible model answers.

Steps 1 to 6 have automated checks (the Check button), so the tutorial can be executed from start to finish in the browser. Diagrams show the architecture and the timeline of each replacement strategy, and each step explains what a command does and why it is needed.

**Relevance**

Deploying changes without interrupting users is a core DevOps concern. Many teams use Terraform to manage infrastructure, but its default replacement behaviour is not safe for live services, and this is often only discovered in production.

The tutorial shows that infrastructure as code needs more than just declaring the needed resources: the order of changes, readiness, hidden dependencies and protection of stateful data all have to be managed explicitly. Because the effect of each lifecycle rule is measured with real traffic, the learner sees what each rule solves and which new constraint it introduces, instead of taking "zero downtime" on trust.

The tutorial also discusses the limits of the approach. Terraform controls ordering but not connection draining or gradual traffic shifting, so it only gives near-zero downtime for simple topologies. It compares lifecycle rules with dedicated mechanisms such as Kubernetes rolling updates and blue/green deployments, and explains for which teams and situations each is appropriate.

Because every change in the tutorial is a change to a file, it also shows infrastructure as code as a record: when the files are kept in version control, each deployment is documented by the code and by its history.

The tutorial therefore combines **infrastructure as code, safe deployment practices, observability of changes, and protection of stateful resources** in one reproducible workflow.