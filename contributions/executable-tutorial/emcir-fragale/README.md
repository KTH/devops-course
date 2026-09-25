# Assignment Proposal

## Title

Deploying a Pre-trained Semantic Search Model as an API with BentoML

## Names and KTH ID

- Ettore Mugisha Cirillo (emcir@kth.se)
- Riccardo Fragale (fragale@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

This executable tutorial uses Google Colab to demonstrate how BentoML turns an existing machine learning model into a service accessible through an HTTP API. It focuses on serving and operating a pre-trained sentence embedding model available on Hugging Face.

The service proposed as example supports a customer support application by finding the FAQ entry most relevant to a user's question. The model converts the question and FAQ entries into embeddings, which the application compares to identify and return the closest match. This scenario provides a concrete use case for sending inference requests to the service.

The tutorial covers defining a BentoML service, calling its API, inspecting the automatically generated API documentation, and building a versioned Bento that packages the service and specifies its dependencies. It also includes checks for correct service responses, readiness, and request metrics.

The tutorial concludes with an explanation of how the packaged Bento could subsequently be deployed in a container environment. This deployment is discussed conceptually; all executable steps take place in Colab without requiring any cloud credentials.

By the end of the tutorial the user should be able to:

- Explain how an existing machine learning model becomes an API service.
- Define and call a BentoML endpoint.
- Package the service as a versioned Bento.
- Perform basic checks of service correctness, readiness, and request metrics.

**Relevance**

Model serving is an important stage of an MLOps workflow. An existing model must be packaged with its code and dependencies, exposed through a stable interface, tested, and monitored. BentoML supports these activities, connecting model serving with DevOps practices such as reproducible packaging, service verification, and observability.

Semantic FAQ search provides a concrete example through which these practices can be explored, while distinguishing the tutorial environment from the requirements of a production deployment.