# Video demo proposal: Monitoring Docker Containers by Visualization 

## Members

Eric Vickström (ericvi@kth.se)
GitHub: [Eric](https://github.com/vickstrom)

Måns Andersson (manande@kth.se)
GitHub: [Måns](https://github.com/mansand1)

## Proposal
Demoing how to make a simple visualization tool for Docker containers memory usage.

## Prerequisites
The user has Docker installed and there is one or more containers to visualize.

## Solution
1. Create python script that runs the shell command `docker stats`

The following information will be retrieved:
```
CONTAINER ID        NAME                                    CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
b95a83497c91        awesome_brattain                        0.28%               5.629MiB / 1.952GiB   0.28%               916B / 0B           147kB / 0B          9
67b2525d8ad1        foobar                                  0.00%               1.727MiB / 1.952GiB   0.09% 
```

2. Store the stats in a log with a timestamp
3. Visualize the memory usage in a web app using flask and chart.js

The video will show the process of creating the app and show a short demo.