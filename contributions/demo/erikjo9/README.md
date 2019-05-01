# Dynamic Jenkins build agents using AWS

I intend to demonstrate configuring Jenkins to launch it's own build agents on Amazon Web Services.
Since the configuration is minimal I also intend to show a use case were such a solution will avoid resource
starvation in an environment where there are many developers and many concurrent builds.
This solution saves both time and money since build agents are launched and destroyed on-demand, so it is very relevant
to DevOps.
