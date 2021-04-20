# Feedback 
Feedback on Tutorial: Proposal for Pi-Hole Docker tutorial by cjgst - PR ID: #974
The feedback can be found on PR #1013
## Members

Andreas Kärrby (karrby@kth.se)  
Github: [andreaskth](https://github.com/andreaskth)

Eleonora Borzi (borzi@kth.se)  
Github: [EleonoraBorzis](https://github.com/EleonoraBorzis)


# Feedback by Eleonora Borzi 
## Summary:
The tutorial is well planned, everything was clear and easy to follow. The steps were divided in a logical way, I did not feel rushed or confused. The tutorial provides all the guidance to complete it, even if something went wrong. The text was divided into paragraphs with titles, the commands and actions were written in bold which makes the tutorial more intuitive. These features show that you have put some thought into how to best guide the user. Some changes would make the tutorial better, such as more info about Docker and references where the user can find some information.

## Intro
- The description of Docker felt too short. The formulation of the second sentence is confusing, it does not give a clear picture of the functionality of Docker.
- Suggestion: I would add where the user can read more about Docker and Pi-hole.
## Step 1
- Short and clear description at the top, but I would have prefered it to be at the start page in the introduction section.
- The reference where the user can find the ads web address shows that you have thought about making the user experience as simple as possible.
- The actual action to perform in the cmd is written in bold which makes it easier for the user to find and draws the eyes attention.
- You also give advice if something went wrong, such as try another address if it went wrong. Again, it shows that you want to guide the user in every possible way and you have tried to foresee any problems that may occur.
- Suggestion: Explain the output that you get from the dig command (example.com. 4541 IN A 93.184.216.34). By doing so, any question that the user may have regarding the output are answered.
## Step 2
- You made clear that Docker is available on the tutorial but not on the user local machine. You give the resource how to get docker, which shows that you want to give all the resources to the user.
- Suggestion: When you introduce a new concept it would be nice to suggest where the user can read about it, perhaps add a “Read more about it here” and link to a source. For example, when you introduce Docker Compose, reference to this webpage: https://docs.docker.com/get-started/08_using_compose/
- Again, the command and the actions are written in bold which make the tutorial more intuitive.
- Suggestion: In the content provided, which should be then pasted in the yaml file, the TZ is set to Sweden/Stockholm. Add a side note that notifies the user to change the TZ to the actual one.
- I like that you make sure that the user has done all the steps before going to the next step, warnings can lead to fewer errors in the execution.
## Step 4
- Good that you explained the flag --detach, it clarifies any doubts.
- Suggestion: instead of “say 0.0.0.0” use the word "display" or "output".
## Ending
Nice that you explained how the user should fully set it up with the port forwarding. However, I think that you should refer the user to other tutorials on how to do port forwarding. For example: https://www.lifewire.com/how-to-port-forward-4163829

## Github repo:
- I would add a short description of the assignment and the tutorial in the README since it is the first thing someone sees in the repo.
- I would also add an explanation of why you created this tutorial, not only for university purposes but also why is it important and why you chose Docker. It would be a nice touch if you specify to whom is the tutorial for, who is the target audience.
- Overall the tutorial is intuitive and easy to follow. Some changes would make it better and there is no interactive tutorial regarding this topic elsewhere. I think you did a good job!

# Feedback by Andreas Kärrby
Overall a very nice tutorial, and also something I've been meaning to look up how to do for a while, so that's a plus. :) I added some feedback comments/thoughts and suggestions below as I went through the tutorial.

## Intro page
- +1 for the classic "it worked fine on my machine!"
- Good that you include a source for https://hub.docker.com/r/pihole/pihole
## Step 1 of 4
- > On the web we are blasted with ads and many ad blockers are imperfect and work in-browser.

Perhaps you could write:

- > On the web we are blasted with ads and many ad blockers are imperfect and only work on a browser-basis, which means you have to install them on all your devices (which is often not even possible on some devices, e.g. mobile phones).

to emphasize the drawbacks of only using ad blockers.

- Another possible clarification:

> by not resolving to a host

could be

> by not resolving certain host names to IP addresses, if the host name is in the aforementioned list of known ad providers

- Overall really nice description of Pi-hole and why it works (by also explaning DNS and that Pi-hole resolves ad providers to 0.0.0.0).

- One thing you cannot really control but that confused me slightly was that my screen is too narrow to show entire lines, so it looked like you had example output of:

    ;; ANSWER SECTION:   
    example.com.        4541      IN      A     
    93.184.216.34    

instead of the IP address actually being on the same line (which I could only see by moving the terminal-split further to the right). Maybe add a disclaimer so users aren't confused by this if they don't realize it's because of the window size.

- I guess the target audience could be computer science students in which case they should know about DNS resource records and their types and classes etc, but you could maybe include a link if someone wants to read further about these things (that appear in dig output).

- Another possible clarification:

> The last entry is the IP address to the host (server) that example.com points to.

could be

> The last entry in the answer section is the IP address to the host (server) that example.com points to.

- Very good that you (in the final sentence) emphasize to remember the address that we will get back to.

## Step 2 of 4
- Nice that you include resources for installing Docker.

- > It is simple to use and easy to get started, the only trick is to create a working configuration file but in this tutorial that has already been done for you.

I'm not sure I understand what is meant here. Is the configuration file /etc/docker/daemon.json as mentioned here or is the configuration file what we create below, i.e. docker-compose.yaml? If the former, maybe briefly mention what the config file does and a source for interested readers, and if the latter then maybe clarify the quote above!
(Also, below you write "Now that you have a docker-compose configuration [...]" so if the docker-compose.yaml isn't the configuration file then maybe clarify this sentence as well)

- Also, related to above, if docker-compose.yaml is a configuration file as well, then it could be good to emphasize that Docker itself has a configuration file "for the entirety of Docker" (so to speak) and that docker-compose is something different that has its own configuration file.

- Bonus: maybe add service names (as #comments) in the list of TCP/UDP ports (like DNS, HTTP and so on) in docker-compose.yaml

- Could add a note on what docker-compose up --no-start does by referencing https://docs.docker.com/compose/reference/up/ (I especially was confused by --no-start-flag)

- Bonus: It could be pedagogical to show (as an aside) a "before and after" of docker-compose up --no-start. I googled and saw you can write docker-compose ps (found here) to list containers. Running that before and after docker-compose up --no-start clearly shows the newly created container, which was a nice sanity-check.

## Step 3 of 4
- Good that you explain what --detach does!

- How does docker-compose up --detach without specifying pihole know to start specifically pihole? Or does it start all created containers (i.e. all containers that would appear with docker-compose ps)?

- (Here you could also benefit from docker-compose ps which would show that the user successfully managed to start the container)

## Step 4 of 4
- > If all went well it should now, instead of displaying a proper IP address, say 0.0.0.0.

Almost don't want to add this point because I feel silly for misunderstanding but I thought you were using "say" in the sense of "assuming we have, say, 5 apples", so if you want to change the sentence to avoid this it could be nice, but again it was probably just me being confused...

- For some reason only the first address in the list seems to work (i.e. return 0.0.0.0) for me? Second, third and fourth still resolve to IP-addresses, and fifth one gives NXDOMAIN. I assume this is something to do with Pi-hole and not your tutorial but I still thought you should know.

## "Finishing up" page
- Awesome that you include info on "what to do now"! If you could also find one or two resources detailing these "future steps" further then you could add that, but you already give some pointers for it so it's not strictly necessary, I think.
## Final thoughts
As you can see, some clarification-suggestions are a bit minor; I figured it was better to note down everything I thought about and you can decide which make sense to change! Anyways as I said in the start, overall really really nice and interesting tutorial. Good job and good luck with your other assignments. 🎉 🥇

