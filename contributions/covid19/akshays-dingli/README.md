
# COVID19 True Infected Estimator
## Authors
Akshay Sinha (akshays@kth.se)

Dingli Mao (dingli@kth.se)

## Description and Motivation
This is a collection of microservices which use the [coronavirus api](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest) (formerly scraped worldometer) for the cases and deaths of all affected countries. Then it calculates the Case Fatality Rate (CFR) of the source countries and uses that to estimate the number of true cases in your country (estimate country). It also calculates the true infected according to an average of the Infection Fatality Rate (IFR) taken from [bloomberg](https://www.bloomberg.com/opinion/articles/2020-04-24/is-coronavirus-worse-than-the-flu-blood-studies-say-yes-by-far). This is helpful because most countries test the deceased for COVID19 so that metric is accurate. But, in countries like Sweden, mild cases of COVID19 are never tested. Using real data from countries that perform blanket testing such as South Korea, Iceland, and Germany we can get a better picture of the number of true cases. Also, the IFR, which is based on randomized surveys, is our current best guess at the number of true cases in a country. The number of true infected are shown for the past 10 days. Currently, there is no tool to estimate cases in this way. ~~NOTE: there will only be a backend for this project; it will return the estimation as a JSON object.~~ We have now created a limited frontend. 

## Relation to DevOps
We will use the following tools and techniques in relation to DevOps:

- Version Control (github)
- Microservices architecture
- Serverless (containers on cloud run)
- Docker 
- CI/CD pipeline (Cloudbuild) which builds from repo and deploys automatically

## Link to Repos
There are two microservices we have created:

- covid-scraper
	- [https://github.com/zen93/covid-scraper](https://github.com/zen93/covid-scraper)
	- This service is not publicly accessible. It is called by the Cloud Scheduler every 30 mins. It reads data from the coronavirus api and stores it to our database.
- covid-stats 
	- [https://github.com/zen93/covid-stats](https://github.com/zen93/covid-stats)
	- This service is accessible at [https://covid-5pocszgd4q-lz.a.run.app/](https://covid-5pocszgd4q-lz.a.run.app/)
	- This service calculates the CFR of the source countries and applies the calculated CFR to the estimate country. It also calculates cases of the estimate country with an average IFR stored in the database. It accepts two query parameters `source` and `estimate`. Example: [https://covid-5pocszgd4q-lz.a.run.app/?estimate=sweden&source=korea-south,germany](https://covid-5pocszgd4q-lz.a.run.app/?estimate=sweden&source=korea-south) 
	- To try new countries use the endpoint: [https://api.covid19api.com/countries](https://api.covid19api.com/countries) The Slug property is to be used with our service.
	- This service also serves the frontend.
