# Feedback on #1393

## Members
André Brogärd (brogard@kth.se)
Github: [andrebrogard](https://github.com/andrebrogard)


## Related PRs
Tutorial Proposal PR [#1169](https://github.com/KTH/devops-course/pull/1169)
Tutorial Submission PR [#1393](https://github.com/KTH/devops-course/pull/1393)
Feedback Proposal PR [#1198](https://github.com/KTH/devops-course/pull/1198)

PR where I responded to feedback and documented changes (with a referenced commit) [#1330](https://github.com/KTH/devops-course/pull/1330)

## Feedback


### Overall

I can see that you are passionate about the tutorial, I can really see the effort you have put in offering a fun experience executing the tutorial (for example, with the quiz). But for someone who is unfamiliar with the 'what' and 'why' of these technologies. It is very difficult to follow along.

I will go over what I think can be improved to really teach a reader like me the usefulness and relevance of this tutorial and allow me to complete it!

### Getting started

I am not very familiar with Linux distros or "WSL" so it was very difficult to get started. It took me quite a while to figure out where I should run the tutorial (On windows, on Linux? Do I have to use a specific Linux?). 
* Where to run the tutorial needs to be more clear.

Prepare the reader for the heavy preparation and what it means to the local computer. If necassary, include a clean up section at the end and let the reader know this.

I interpreted it as. 'Choose windows or Arch Linux, but any linux works with some changes'. So I attempted to use Ubuntu. But it failed. In the introducton you say that the preparations step can be skipped on any Linux distro that uses systemd. Which is what I did on Ubuntu, I do now know what Systemd is... so I assumed a typical Linux distro like ubuntu supports it. However, the instructions after Preparations are related to genie, wsl and Arch Linux. Therefore using Ubuntu failed for me, it looks like I need WSL or genie. 

It's hard for me to tell, because I know nothing of these technologies. Furthermore, I was reluctant to install WSL2 on my Windows machine, as I would have wanted to install this in a virtual environment instead of making system changes on my main PC. 

I advise to:
* Maybe, generalize the tutorial to be titled 'CREATE MULTI JENKINS CONTAINERS BASED ON SYSTEMD-NSPAWN'. Then in the prep section you can include the WSL2 install for windows users. You could then have a description of WSL2 and how good it is. 
* Or, keep as is. Readers like me can choose to skip the WSL step if we run on linux, but you have to be super clear about this. This is achieved by making the user understand the technologies used. It is important to then generalize the rest of the tutorial to not depend on WSL. You need to limit the amount of supported distros.

###  Introduction
Good summary of what this tutorial is and what will happen. But you introduce alot of technologies here that I do not understand.
* I think you need to add sections/paragraphs describing 'WSL2', 'Systemd', 'Systemd-nspwan container technology' and 'Jenkins'. What are they, how are they used and why do we use them? You could of course describe 'Jenkins' later when it is actually isntalled and first mentioned in section 3. But importantly, I do not know what any of these technologies are, before I use them I should know them. 

About the tutorial script. I like the quiz! But I think that tutorial script should not be introduced here, maybe it is best to not have it at all. It is also confusing to run this script while following the rest of the tutorial, even if it is organized into the sections. My advise is to:
* Keep the quiz! It adds a personal touch to the tutorial which I like. But add it as transitions into new sections of the tutorial. Such as after 0x02 and before 0x03. Then you could have answers to the quiz at the bottom, for example.
* Add the information/trivia that is in the tutorial script to the tutorial itself and to the different sections instead of having a seperate script. This help me learn what is happening. 

### Preparations
You explain why we use Genie, however in this context, you explain Genie with the assumption that the reader knows why we use WSL or what systemd is. It is therfore difficult to get an understanding. 
* More information on WSL, the what, how and why. (Some you already cover slightly)
* Same for Systemd
* Same for Genie

If you explain the above, the install instructions will make more sense to me.

You say that I can choose any WSL2 distribution, like Ubuntu, Debian, Alpine or Arch Linux. You choose Arch Linux.
* The instructions in the tutorial assumes Arch Linux. It is not possible to run:
    ```
    sudo pacman -S arch-install-scripts
    ```
    on an Ubuntu. That package is also not available, I suspect, on other distros through their package manager.
    I think you need to do the tutorial more self-contained. Do not tell the reader to find the tutorial for themselves. (Or, as advised in the bottom, do not support other distros)
* The user needs more guidance if you wanna support all distros.

### Create our first Systemd-nspwan container

* Missing an explaination of what 'Systemd-nspawn container' is
* It is nice that you explain 'Systemd-nspwan' in section 2, but with more context I think I could understand this. What is namespace virtualization, what is the chroot command. Please give examples and provide more in depth, in detail descriptions. 
* Please explain why we do 2.5 Boot container, change root password

#### Jenkins 

Nice step 4!

* Missing explaination of Jenkins in step 3. What does it do, how will we use it in this tutorial. I am not sure if this information is covered later, but as a reader it helps to learn if I know about it before I install or use it. 

### Second Container and Packing containers

Good to remind the reader of some key insights in the beginning of Second Container!
I think this stage is rather clear and straight forward. Good job!

* It would be nice to maybe reflect on the purpose of multiple Containers, why and when would we use this? Isn't one file system enough?

Maybe you could end the tutorial with the above pointer, that you could reflect on how these techniques may enable ... somehthing? If there is relevance to DevOps a.s.o. How can we use Jenkins now, unlike before. As a reader, that is unfamiliar with these things, I cannot do those deductions on my own.


### General advise

My strong **STRONG** advise is to create a step by step tutorial on Katacoda. However this is a transition completely to a ubuntu environemnt. If you are unsure of what is possible or struggle with syntax in the configuration. You can check out my executable tutorial (git: [Github](https://github.com/andrebrogard/katacoda-scenarios), katacoda: [Katacoda scenario](https://www.katacoda.com/andreeva/scenarios/datadog-tutorial) and use it as a template/starting point for Katacoda. 

Do look over grammar, there quite some mistakes with spelling and formatting. You can use a tool like grammar.ly! I also think you misspell tutorial.  

Preferably, the tutorial should be step by step where you offer the reader a chance to learn what is happening, but the reader should not really have to think about what they are doing to reach the end goal (launching the jenkins containers). Simply following instructions, but you should offer the reader the chance to understand everything that they are doing and why. 
* Either, fix the tutorial to only run on Windows or Arch Linux. Or, generalize to some ubuntu distro that more people may have access to.

Create a more self-contained tutorial! Then it would really teach the reader these concepts in a more efficient and accurate way.

### End words

Thank you for this tutorial, I think that if you make this tutorial more self-contained it would be much better and I would be able to complete it!




