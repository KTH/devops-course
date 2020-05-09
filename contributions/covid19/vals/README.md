# COVID-19 - Visualizing daily new cases (USA/Sweden) along with Google Trends

## Link to repo
https://github.com/valsen/covid19

## Author
Victor Josephson (vals@kth.se).
Github username: valsen

## Description
A single-page website that displays a chart overlaying coronavirus related google search trends on top of daily new reported cases of COVID-19. A dropdown selector lets the user choose either the United States or Sweden, meaning the google trends and covid cases are local for that country. A text input field lets the user choose up to 5 comma-separated search terms for the google trends.

Data is fetched from Google Trends, covidtracking.com and covid-api.com.

## Motivation
Many websites offer detailed data and charts on the coronavirus pandemic, but my website adds an interesting visual as it shows a timeline of the search trends of COVID-19 symptoms on top of the reported cases. A spike in the search trends might give an indication of when many people actually got sick, which according to the chart seems to be several weeks before the spikes in reported cases, both in the United States and in Sweden.

## Ties to DevOps
- The website is version controlled and hosted on Github
- The frontend (written in Svelte) and backend (Python Flask) each have their own Dockerfile for containarization
- A docker-compose file is used to create a container swarm in which the frontend and backend can communicate with each other
- Google Cloud Build integration with the Github repo, triggers Google to run a cloudbuild.yaml file that in turn builds the containers with docker-compose
- A terraform config file allows an easy way to spin up a Google Compute Engine instance, which the website could be deployed to (I will not implement the deployment due to lack of time)