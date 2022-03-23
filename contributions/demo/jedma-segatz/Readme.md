# Assignment Proposal

## Title

Automated testing and delivery for FreeRTOS using AWS

## Names and KTH ID
  - Johan Edman (jedma@kth.se)
  - Fabian Segatz (segatz@kth.se)

## Deadline

Deadline task 1

## Category

Testing & Continuous Integration 

## Description

In IoT there are often many devices that should receive updates, even when they are already embedded in field.

It is crucial to validate the correctness of any update, before it is published. At the same time security updates should be supplied fast, to close eventual weaknesses. Automated testing can be used to reduce the time-to-delivery.

However, software developement for embedded systems is not as advanced by the means of using CI-pipelines and need some further exploring.

We plan to give a demonstration on how to use, Jenkins and AWS to automatically deploy firmware which is built upon FreeRTOS. The firmware-under-test runs some schedulability test, which sends back metrics to Jenkins.

The deployment is supposed to be performed using over-the-air (OTA) updating to an ESP32 evaluation board connected to the same network as the build server.

## Comment 
There was a similar project in 2020 (https://github.com/KTH/devops-course/tree/2022/attic/2020/contributions-2020/demo/carljen-axelbc), where a demonstration of a CI pipline for embedded devices was given.

Our proposal divers in three ways:
  1. We don't use the remote testing suite of plattform io, and instead use AWS.
  2. Deployment with OTA updates, which simulates a better use-case for in-field testing
  3. Unit testing without using an extra probe device, expoiting the capabilities of RTOS.


