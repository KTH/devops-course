# Assignment Proposal

## Title

Collecting user crash reports in GameMaker

## Names and KTH ID
- Linus Below Blomkvist (libl@kth.se)
- Fredrik Svanholm (svanhol@kth.se)

## Deadline

Task 4

## Category

Demo

## Description

[GameMaker](https://gamemaker.io/) is a game engine that has been used to create games such as Shovel Knight, Hyper Light Drifter and Katana Zero.

GameMaker has a default crash report handler that shows basic information about the crash to the user before exiting the game.

We have created a library for GameMaker called "CrashR" that allows developers to override and create their own crash handler that generates a crash report containing information about the uncaught exception along with additional platform and user data that is then formatted and sent to a webhosted database (Firebase in our demo). This library allows the game developer (us) to automatically collect crash reports from all users playing the game, which makes it possible to analyse game crashes on a much larger scale than if automation woudln't have been used.

Repository: https://github.com/JustFredrik/CrashR
