# Executable-tutorial: Creat multi Jenkins containers in Windows-Sub-Linux based on systemd-nspawn

## Members

Sui Yuehao yuehao@kth.se [@amaothree](https://github.com/amaothree)

## Proposal

Container not always be Docker! Try Systemd-nspawn now!  

"systemd-nspawn may be used to run a command or OS in a light-weight namespace container."

I would like to show a totural about how to creat multi systemd-nspawn containers with Jenkins in WSL2 to implement multiple jenkins projects working simultaneously.

The contents are:

* WSL2 install

* Creat the first systemd-nspawn container in WSL

* How to install Jenkins inside a container

* How to configure the container network so that the host can access it.

* Multiple Jenkins containers running simultaneously

I will try to use katacoda platform firstly, if it can not provide a needed environment. I will write a local totural and post on my blog.
