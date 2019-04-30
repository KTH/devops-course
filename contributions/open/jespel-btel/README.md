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

## Side goal
We were happy with our devops practices. Our project focused very much on the visual and artistic side of the product resulting in us forgoing unit tests, but we are proud over our automatic deployment. Our repos can be found at [https://gitlab.com/flaky_kth_devops](https://gitlab.com/flaky_kth_devops).

Unfortunately we did not have time to implement our crazy idea. However, we did implement an alternative mode where the animation will continously flatline if some CI fails in a specified repo.

