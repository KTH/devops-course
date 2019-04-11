# Docker Swarm with logging and Monitoring.

* Group members: Jakob Holm (jakobhol@kth.se) & Adibbin Haider (adibbin@kth.se)
## Proposal
We will set up a docker swarm stack with a simple backend with a couple of endpoints that is crashable through curl or postman (this to show that the logging and monitoring works as intended). Furthermore we will add logging with the ELK-stack (elasticsearch, logstash and kibana) and add monitoring with grafana and prometheus to the swarm. This to simulate a possible docker swarm stack that could be usable in the future as a starting point for devops. This will also utilise CI/CD with Jest and Travis.  