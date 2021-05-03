# Executable-tutorial: Creat multi Jenkins containers in Linux based on systemd-nspawn

## Members

Sui Yuehao yuehao@kth.se [@amaothree](https://github.com/amaothree)

## Proposal

Container not always be Docker! Try Systemd-nspawn now!  

"systemd-nspawn may be used to run a command or OS in a light-weight namespace container."

I would like to show a totural about how to creat multi systemd-nspawn containers with Jenkins in Linux to implement multiple jenkins projects working simultaneously.

## The contents are

* The background of this tutorial

* The preparation to creating Systemd-nspawn container.

* How to create a systemd-nspawn container

* How to install Jenkins inside a container

* How to configure the container network so that the host can access it.

* Multiple Jenkins containers running simultaneously

* How to pack containers

## How to run the tutorial

Open the katacoda link below and enjoy the tutorial follow the steps.

If you are want to try this tutorial on your PC instead katacoda. Please read the post in my blog > https://amao.run/en/posts/systemd-nspwan/

### The tutorial link

* [The Executable Script](https://www.katacoda.com/amaothree/scenarios/nspwan)
* [The Github](https://github.com/amaothree/katacoda-scenarios/tree/main/nspwan)
* [My Blog](https://amao.run/en/posts/systemd-nspwan/)

## My goals

|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) | Yes | |  |
|The tutorial gives enough background | Yes |  | Comprehensive background |
|The tutorial is easy to follow  | Yes |  | Well documented |
|The tutorial is original, no such tutorial exists on the web | Yes |  | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | Yes |  | Subtle and fun |
|The tutorial is successful (attracts comments and success) |  |  |  |
|The language is correct | Yes |  | Interesting narrative  |