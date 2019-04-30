# Taking Down Production

## A cautionary tale about the need for testing

My proposal is to create a short animated website that is a mockup of a dashboard where you can see the status of microservices or perhaps servers, and a log showing git pull requests in to the production branch. Before too long a bad commit is merged and you can witness the destruction of the production environment.

If there is time, this will follow by another version where each commit is run against tests before being accepted in to the production branch - a "what you should be doing" version.

## Members

- Louis Nathan, lcjna@kth.se
