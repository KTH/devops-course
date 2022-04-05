# Assignment Proposal

## Title

How to encapsulate microcontroller applications upon RIOT-OS inside Femto-Containers. 

## Names and KTH ID
  - Johan Edman (jedma@kth.se)
  - Fabian Segatz (segatz@kth.se)

## Deadline

Task 3

## Category

Executable tutorial

## Description

Embedded software life cycle management resembles still more PC system software workflow from the 90s than todays common software practices. Methods to apply DevOps like containerization and virtualization are not very common. 

Projects such as [Micropython](https://micropython.org/), which aims to bring a full-blown Python 3 interpreter to microcontrollers, are steadily gaining popularity. However, it seems that everything done in this area, is currently only used for rapid prototyping purposes and never actually deployed on any product. There are two reasons behind this:

1. Interpreters introduce a large size overhead. I. e. the micropython interpreter, compiled for the Nordic nrf52840dk microcontroller, needs 101kB ROM and 8.2kB RAM. With microcontrollers memory sizes of 256kB ROM and 64kB RAM are not uncommon. 
2. Compared to native code, script interpreters execute code approx. 600 times slower.

Just in last years november (2021), Koen Zandberg release a paper with the title: ["Femto-Containers: DevOps on Microcontrollers with Lightweight Virtualization & Isolation for IoT Software Modules"](https://arxiv.org/abs/2106.12553), introducing a promising outlook on containerization, effectivly takeling the above problems.

We would like to create a Katacoda tutorial how to encapsulate application code inside a femto-container to show the benefits of such techniques on microcontrollers.
