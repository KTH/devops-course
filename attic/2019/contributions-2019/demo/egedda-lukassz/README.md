# Demo: Monitoring and Chaos Engineering

Monitoring: Kubernetes, load balancer, nginx cluster, prometheus, and grafana.
Chaos Engineering: Gremlin

Link to screencast: [https://youtu.be/yAL83Z1VjAI](https://youtu.be/yAL83Z1VjAI)

A kubernetes cluster of 5 nodes was set up. 3 nodes running nginx as a proxy for our flask application, with a load balancer infront of these running in round robin mode.
1 node running httperf to generate HTTP load on the server and the load balancer, and the final node for monitoring with grafana and the timeseries database Prometheus as the backing storage for the metrics.
Gremlin was also installed on a per node-basis to perform simplify the fault injection and resource exhaustion. We also developed our own Python Flask application (served behind nginx) to be able to fault inject straight into the web application aswell.

* Emil Gedda (egedda@kth.se)
* Lukas Szerszen (lukassz@kth.se)
