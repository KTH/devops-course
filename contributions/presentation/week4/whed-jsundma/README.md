# Assignment Proposal

## Title

Data Set Anomaly Detection using the k-NN Algorithm

## Names and KTH ID

  - William Hedenskog (whed@kth.se)
  - Joakim Sundman (jsundma@kth.se)

## Deadline

- Week 4

## Category

- Presentation

## Description

We plan on presenting a method for detecting anomalies or outliers in a data set, before the data is used to train AI models. It will be based on the [*k*-NN algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) and the purpose is to find data points that could be malformed or or otherwise unsuitable for its intended purpose. The algorithm could be based on previous known good data, making it part of an iterative life cycle. 

The test should/could trigger each time new data or tuning data is added to the database as part of a CI pipeline.

**Relevance**

This topic is relevant seeing as the data set has a big impact on model performance. If anomaly detection is implemented early in the process as part of AIOps, data outliers can be removed from the data set before it has a chance to affect model training. It should be easier to avoid merging data than to remove it, after a model has already been introduced to it, leading to more effective and automated data validation. 
