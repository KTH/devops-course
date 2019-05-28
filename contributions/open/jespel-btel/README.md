# Flaky Test

![ecg](https://i.imgur.com/PJBc6GD.png)

An animation that symbolises flaky tests.

## The main idea

We would like to create an art project representing flaky tests as our open project.

Our idea is to create an animation of an ECG that works most of the time, but sometimes for no reason weirds out (like flatlines for a short while or take a double beat) before it returns to normal.

Our idea is to create a small webpage to hold this animation.

We created the image above as small exploatory project to understand the techniques to create the ECG effect.

## Side goals

Developing this website we would like to practice some of the DevOps techniques that are taught in the course. We beleive that especially CI and CD would fit the project.

Further we got a crazy idea that it might be cool to be able to visualize the progress of project, i.e. being able to see every commit of the project.

# Result
## Main project
[https://flaky.jesperlarsson.me](https://flaky.jesperlarsson.me) holds the final animation.

## Meaning

## Implementation

## Repo structure
Other than the main frontend-only animation that was the focus of the project we created a small backend that the frontend may communicate with. The purpose of the backend is to listen for webhooks signaling the status of a repo. (The backend only support GitLab for the moment, but is designed so that it is easy to add support for other platforms.) The frontend may also function just as an artpiece without a backend if desired.

### Flaky
The frontend is contained within the repository Flaky. It is simply a static webapp and could be deployed as such to any webserver. We hosted ours on a server that ran the docker manager dokku. For a custom deployment where one would like to integrate it with our developed backend, one would have to update the url to that backend though. This can easily be done on [line 318](https://gitlab.com/flaky_kth_devops/flaky/blob/master/public_html/index.js#L318) of index.js. (It might have been more friendly to extract that value to a constant at the top of the file though.)

### flaky_back_end
We choose to seperate the backend to its own repository (flaky_backend) so that the frontend would deploy as a simple static website. The backend listens to status webhooks from GitLab and stores it. The frontend may then query that status through the route `/status`. The backend may only monitor one repo at a time, so one backend need to be deployed per repo to monitor. The backend is otherwise a flask application and may be deployed as such. Before deploying, one need to configure CORS to allow the frontend to talk to the backend. This can easily be done on [line 8](https://gitlab.com/flaky_kth_devops/flaky_back_end/blob/master/controller.py#L8) in controller.py. We also hosted this using dokku.

### flaky_test
The repo flaky_test was used as a dummy repo that our backend could monitor. We purposefully made it pass or fail tests to ensure that our backend integrated with GitLab as desired.

## Side goal
We were happy with our devops practices. Our project focused very much on the visual and artistic side of the product resulting in us forgoing unit tests, but we are proud over our automatic deployment. Our repos can be found at [https://gitlab.com/flaky_kth_devops](https://gitlab.com/flaky_kth_devops).

Unfortunately we did not have time to implement our crazy idea. However, we did implement an alternative mode where the animation will continously flatline if some CI fails in a specified repo.

