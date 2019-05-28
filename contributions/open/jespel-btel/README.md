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

### The heartbeat function
The heartbeat was implemented from scratch by using some simple built
in mathematical functions. The function attempts to describe the
different interval, segments and waves of a high detailed ECG. First
is the P-wave, which is described by a simple sine function. After
this comes the very characteristic spike of an ECG, known as the QRS
segment. The function describes this by gluing together 4 different
linear functions with different derivatives, to give the
characteristicly sharp look that drops before and after the
highpoint. The QRS segment is followed by the T-wave, also described
by a simple sine function. After this is the seldom seen U-wave, a
wave with very small magnitude compared to the other parts of the ECG,
and this is often missed if the ECG has a low resolution. The U-wave
is also described by a sine function.

The heartbeat function returns an object with information that the
display uses. The attributes are height (`y`), colour and sound, which
tells the display to send sound or not.

### The display

To display all this, a html canvas was used to continously draw the
points provided by the hearbeat function, and a nice thematic
background was added using a colour gradient effect.

To display this, points were fetched from the heartbeat function by
supplying it with a parameter t, which determined how far into the
heartbeat the display is. 

A tone was also played depending on the return value of the hearbeat
function, much like a normal ECG (with a continous sound being played
during a flatline).

### The backend

The backend was written in Python using the Flask framework to create
an API to control the front-end. A few different routes were used to
controle the mode of the front end (is it an art-work or build health
monitor?), change the build status and provide the current build
status. 

* `/status` displays the current status of the build 

* `/mode` the current mode of the canvas

* `/flip-mode` switch the current mode of the canvas

* `/hook` endpoint to communicate with gitlab

## Repo structure

## Side goal
We were happy with our devops practices. Our project focused very much on the visual and artistic side of the product resulting in us forgoing unit tests, but we are proud over our automatic deployment. Our repos can be found at [https://gitlab.com/flaky_kth_devops](https://gitlab.com/flaky_kth_devops).

Unfortunately we did not have time to implement our crazy idea. However, we did implement an alternative mode where the animation will continously flatline if some CI fails in a specified repo.

