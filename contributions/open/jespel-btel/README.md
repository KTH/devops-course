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

## Artistic meaning
The final product contains two different animations:
 1. normal heartbeats, and
 2. flatline.

We did not animate arrythmia manifesting as a double heartbeat since we deemed that it was not neccessary to deliver our artistic vision.

Our vision was to create an animation that could convey the feeling of flaky tests. The normal heartbeats represents that tests passing as they should, and the site is dominated by a calming green to ensure the viewer that everything is fine. But then, suddenly, it all changes to an alarming red with a constant monotonic noise when the ECG flatlines and turns red. This represents the heartstopping fear one might feel when their normally green chekckmark suddenly turns into a red cross due to a flaky test. But just as suddenly as it flatlined, it goes back to the calming green, and momentarily calms you, but you feel that your trust has slightly diminished.

## Implementation
The frontend was implemented as static site, with plain HTML, CSS and JS. The following sections will describe how we generated datapoints for the heartbeat and displayed them.

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

* `/hook` endpoint to communicate with gitlab about the build status

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

