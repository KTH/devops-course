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

## How to read the totural

~~I will try to use katacoda platform firstly, if it can not provide a needed environment. I will write a local totural and post on my blog.~~

I write a document and an executable script. The best way to learn this tutorial is to combine the two. My blog posts are comprehensive and detailed. And the script is concise and comes with 6 quizzes.

The script is divided into four sections, corresponding to the four chapters of the body of the article.

### The totural link

* [My Blog](https://amao.run/en/posts/systemd-nspwan/)
* [The Github](https://github.com/amaothree/amaothree.github.io/blob/master/content/en/posts/Systemd-nspwan.md)
* [The Executable Script](https://gist.github.com/amaothree/d8bac64e5225b15db84aaf8e3aa6e08d#file-totural-sh)

### How to download and run the script.

1. Open a new terminal tab. If you using WSL, open a wsl tab in Windows terminal.
2. Copy and Execute:
    ```bash
    curl -o totural.sh https://gist.githubusercontent.com/amaothree/d8bac64e5225b15db84aaf8e3aa6e08d/raw/fdff92ffddac8626584ad823a3b01ce0795c9f4a/totural.sh
    chmod +x ./totural.sh
    ./totural.sh
    ```


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