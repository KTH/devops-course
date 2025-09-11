# Assignment Proposal

## Title

CD Using Elixir/Erland Hot Code Swapping and Github self-hosted Runner

## Names and KTH ID

  - Edwin Ahlstrand (edwinahl@kth.se)
  - Emil Kanerva (ekanerva@kth.se)

## Deadline
- Week 3

## Category
- Demo

## Description
This demo implements an automated deployment workflow for Elixir using a GitHub self-hosted runner which monitors pushes to the main branch. When new commits are pushed, the runner triggers a workflow that:
- Pulls the latest code changes from the repository.
- Builds the new version of the Elixir app.
- Uses Erlang's hot code swapping to upgrade the app to the new version while still running.

This will be demonstrated through an application which is actively communicating with a server in an uninterrupted manner while it is being updated, showcasing that the changes made to the server immediately become apparent on the client.

**Relevance**
The project is connected to Week 3 Continuous Deployment/Delivery since it embodiedes core features of DevOps in that topic, mainly automation and continuous integration/deployment. This showcases an alternative to for example Blue/Green deployment where the same speed of deployment can be achieved, but without requiring any extra hardware or systems. 
