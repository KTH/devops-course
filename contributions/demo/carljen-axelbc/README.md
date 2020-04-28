# Demo

## Members 

Carl Jensen (carljen@kth.se) Github username: Callet91

Axel Boldt-Christmas (axelbc@kth.se) Github username: xmas92

## Topic
CI/CD pipeline for embedded devices using PlatformIO and Jenkins

## Outline
Demo of implementing PlatformIO in a CI pipeline with Jenkins for testing scripts intended to run on embedded eval boards. If possible we would like to integrate CD to our pipeline. 

## Motivation
When developing for embedded systems, tests that relate to the actual hardware are often done manually on a dedicated testrigg. This is time consuming and often creates a bottleneck in the workflow since only a small team can work on the testrigg one at a time. Automation of physical tests could hopefully reduce the time spent in the lab and to verify the code under test. 

## Setup
Jenkins server for handling the CI flow.

Using PlatformIO and PIO Remote Agent to run tests on both server and on actual evaluation boards. (Maybe add some electronic test equipment as well, over the serial monitoring that PIO enables)

Using Jenkins and a CD server to push new versions to IoT devices.

## Reference 
platformIO: https://platformio.org/ 

## Screencast link

[https://www.youtube.com/watch?v=ncTp90wV9gM](https://www.youtube.com/watch?v=ncTp90wV9gM)

## Demo Repository

[https://github.com/Callet91/DEMO_Jenkins_PlatformIO](https://github.com/Callet91/DEMO_Jenkins_PlatformIO)
