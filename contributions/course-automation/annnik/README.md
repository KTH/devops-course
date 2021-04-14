# Course automation: Improve communication with Discord integration

## Members
Anna Nikolskaya (annnik@kth.se)

Github username: annsudo

## Proposal 
The goal of this automation is to help TAs and Professors to reach students through Discord with imergent announsements. If the "Extra"-section is implemented the action will also decrease the respond time from the students on making changes to their pull requests

## What the action does 

 - ✅    Filter the actors (Triggered only on comments from  (monperrus, bbaudry, SophieHYe, Deee92, cesarsotovalero,khaes-kth) and author (annsudo))
 - ✅    Filter events (Triggered: on comment for both issues and pull_requests)
 - ✅    Standarize format (Message together with a GIF is send in respons that the message was succesfully send to discord)
 - ✅    Integrate with Discord 
 - ✅    Customize what information should be included in the Discord messages (Included: auther, message, which issue/PR, link)
 - ✅    Connect back to Github (Navigate back to issue by pushing on "Go to github on discord message" )

## Structure

I structured this automation as 2 parts with goal of making it reusable for other users. [1st part](https://github.com/annsudo/discord-comments) is an action that is useful for all github+discord lovers: it messages on both PR and Issues and send them to Discord beautifully formated. [2nd part](https://github.com/annsudo/comment-to-Discord-action) AKA Head project is more corse-spesific where I show how to filter actors who can trigger this action and combine it with some fun gifs.

## Code + documentation + how to use
The head project is found [here](https://github.com/annsudo/comment-to-Discord-action) 
