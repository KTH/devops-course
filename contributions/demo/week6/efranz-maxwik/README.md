# Assignment Proposal

## Title

Blazing fast feature flags and A/B testing with Vercel edge functions and edge config

## Names and KTH ID

  - Emil Franzell (efranz@kth.se)
  - Max Wiktorsson (maxwik@kth.se)

## Deadline

Week 6

## Category

Demo

## Description

In this demo, we show how you can easily deploy feature flags and A/B tests to your Vercel application using edge functions and edge config. We do this by creating a simple Next.js application with authenticated routes using middleware and server-side rendering. We then deploy the application to Vercel and make use of edge config to show how feature flags can be deployed. Finally, we want to show how fast this solution is for feature flags.

**Relevance**

This demo shows one way to implement feature flags, which is a concept that cloesely aligns with devops principles. Feature flags facilitate faster release cycles and by decoupling feature releases from code deployment, they enable incremental rollouts and provide a way to roll back in case of bugs or other issues. It is a novel way to accomplish this, since edge config is a new feature on Vercel. The reason why this way to do it is interesting is because it can speed up page loads by hundreds of milliseconds by putting feature flags on the edge instead of in some remote database.