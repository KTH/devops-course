# Covid-19 Cases by Counties

## Link to repo
The repo is available here: https://github.com/perfah/covid-19-in-my-region

## Members
Per Fahlander (perfah@kth.se)
Joar Ekelund (joarek@kth.se)

## Description
Write a webserver in Python that fetches and presents [official CSV-data from DGG (Myndigheten för digital förvaltning)](https://www.dataportal.se/sv/datasets/525_1424/antal-fall-av-covid-19-i-sverige-per-dag-och-region) on the number of COVID-19 cases per Swedish region/county. This data would be presented on a website with a graph plotting the development of newly confirmed cases in any region (with available statistics).

## Motivation
The official website from Folkhälsomyndigheten does not show newly confirmed cases per region/county in graph-form. It would be a nice addition to be able to see a plot on the development in specific regions since it is hard to see trends from data sheets.

## Ties to DevOps
We will use the following DevOps technologies in the development of the script:
- GitHub for version control.
- Travis CI + PyTest (or similar) for unit and integration testing (including end-to-end http request testing)
