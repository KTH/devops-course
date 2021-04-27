# Executable-tutorial: Creat multi Jenkins containers in WSL2 based on systemd-nspawn

## Members

Sui Yuehao yuehao@kth.se [@amaothree](https://github.com/amaothree)

## Proposal

Container not always be Docker! Try Systemd-nspawn now!  

"systemd-nspawn may be used to run a command or OS in a light-weight namespace container."

I would like to show a totural about how to creat multi systemd-nspawn containers with Jenkins in WSL2 to implement multiple jenkins projects working simultaneously.

## The contents are:

* WSL2 install

* Creat the first systemd-nspawn container in WSL

* How to install Jenkins inside a container

* How to configure the container network so that the host can access it.

* Multiple Jenkins containers running simultaneously

~~I will try to use katacoda platform firstly, if it can not provide a needed environment.~~ I will write a local totural and post on my blog.

## The totural link
* [My Blog](https://amao.run/en/posts/systemd-nspwan/)
* [The Github](https://github.com/amaothree/amaothree.github.io/blob/master/content/en/posts/Systemd-nspwan.md)


## My goals
|                                             | Yes | No | Remarkable |
|-------------------------------------------- | ----|----|-------------|
|The TA can successful execute all the commands of the tutorial (mandatory) |  | No |  |
|If local execution, runs on Linux | Yes |  | Easy to setup and run  |
|The tutorial gives enough background | Yes |  | Comprehensive background |
|The tutorial is easy to follow  | Yes |  | Well documented |
|The tutorial is original, no such tutorial exists on the web | Yes |  | The teaching team never heard about it |
|The tutorial contains [easter eggs](https://github.com/OrkoHunter/python-easter-eggs) | Yes |  | Subtle and fun |
|The tutorial is successful (attracts comments and success) |  |  |  |
|The language is correct | Yes |  | Interesting narrative  |