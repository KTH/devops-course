# COVID19 True Infected Estimator
## Description and Motivation
This is a collection of microservices which scrape the website [https://www.worldometers.info/coronavirus/](https://www.worldometers.info/coronavirus/) for the cases and deaths of all affected countries. Then it calculates the Case Fatality Rate (CFR) of the country and uses that to estimate the number of true infected in your country. This is helpful because most countries test the deceased for COVID19 so that metric is accurate. While, in countries like Sweden, mild cases of COVID19 are never tested. Using real data from countries that perform blanket testing such as South Korea, Germany and the cruise ship Diamond Princess we can get a picture of the number of true cases. Currently, there is no tool to estimate cases in this way. NOTE: there will only be a backend for this project; it will return the estimation as a JSON object.

## Relation to DevOps
We will use the following tools and techniques in relation to DevOps:

- Version Control (github)
- Microservices architecture
- Serverless (containers on cloud run)
- Docker 
- (if time permits) CI/CD pipeline which builds from repo and deploys automatically  
