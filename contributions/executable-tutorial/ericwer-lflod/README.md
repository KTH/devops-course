# Assignment Proposal

## Title

Tutorial submission: MLOps: Sentiment analysis API using Hugging Face models wrapped with BentoML

## Names and KTH ID

- Eric Wernström (ericwer@kth.se)
- Ludwig Flod (lflod@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

We want to make a tutorial which goes through the steps of taking a pre-trained model for sentiment analysis and turning it into a deployable service using BentoML. Sentiment analysis refers to finding out the sentiment behind a written piece of text, I.E "positive", "negtive" or neutral. The focus of the tutorial is the process of deploying the model, since any model could be used. The tutorial will be carried out in Google Collab, where you will learn to load the model, wrap it in a BentoML to turn it into a REST API. We then expose the API using pyngrok and show the API being called on a demo website with simple UI generated with Gradio.

**Relevance**
Turning a trained model into a BentoML service and exposining it as a REST API teaches the user how to structure their ML code in order for it to be reproducible and for it to provide a consistent interface for other applications to interact with. The Bento service is reproducible and version-controlled, and automates the process of starting the API, serving the model and exposing the endpoints needed to interact with it.

**Submission link below**
https://colab.research.google.com/drive/1sKIBppnJNOEm22vm0GG0N1VaoSqMKjyL?usp=sharing

**Our ngrok authkey encrypted with course key**
-----BEGIN PGP MESSAGE-----

hF4D0KiDfE6sIscSAQdAwDc4nA9Zh9jCkpCH0aNzApJ97NC12A5+poWV7q0HlXgw
YGj9e7wyOczAWhOuffioULYIQXSyS/lxFxokf9CtwzvqUTsVNTiDlElaIFdtSZMQ
1KwBCQIQflvavLyUSTkTTnPlur/kVtLxHbZYwLjr9K+bcr/Vb6Cmek6k0B+ukucx
qBzoaA3QphHM3TJoEFRYcn4B6K7ggAo18iNY0iWCERuLYbkGmOI6qdkQYLA13JB8
OUtxJiCC006RlMz6Fg/8RivLzQgMI+kLzlY/BZLAJbyz4ByTeD6XLVkuJLKh4IT4
cqNOViWh5Qvak6CTZ0i/sB3YPGu/ohLbDRMvDBJ6
=nLru
-----END PGP MESSAGE-----

