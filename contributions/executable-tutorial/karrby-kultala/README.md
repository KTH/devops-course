# Executable tutorial: Automated monitoring/analytics with ELK Stack or Splunk

## Members

Andreas Kärrby (karrby@kth.se)  
Github: [andreaskth](https://github.com/andreaskth)

Henrik Kultala (kultala@kth.se)  
Github: [hengque](https://github.com/hengque)

## Proposal

We would like to create an executable tutorial on Katacoda that will showcase how to add support for monitoring/analytics in an application by using either the ELK stack (Elasticsearch, Logstash, Kibana) or Splunk. We will either create our own very basic application and extend it with monitoring/analytics, or if we can find a suitable existing "example application" we will use that instead and extend it (for example, [this](https://github.com/spring-projects/spring-petclinic) looks to be a promising project).

As for the actual analytics to focus on, it remains to be determined when we've learned more about the capabilities of the analytics tool we choose. Most likely we want to focus on generating and displaying data on how users interact with the application (which views are most frequently visited and – if simple enough to implement – how much time is spent in each view).

The implementation itself will either be "old school" in the sense that we run the applications "as is", or – if time and skill permits – we will dockerize the application and the analytics tool to make them easier to run together (in that case, probably using Docker Compose).

The relationship to DevOps is that monitoring is a big part of "Ops" and a lot can be gained by automating this as much as possible. Also [this](https://www.atlassian.com/devops/devops-tools/devops-monitoring?) reference contains good motivations for why this is related to DevOps.
