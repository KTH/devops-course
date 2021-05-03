Feedback Proposal
Tutorial: Configuration of CI/CD infrastructure with Ansible
Members
Kalle Meurman (kallem@kth.se), Github: Wizkas0

Tutorial to give feedback on

I plan to give feedback on this tutorial https://github.com/KTH/devops-course/pull/1102 , #1268

Feedback given on: #1351

# Feedback
## Overall thoughts
Overall, I thought the tutorial was of great quality. It was easy to follow, and it taught me exactly what was advertised. The tutorial made the topic feel interesting, something that cannot be said for some  of tutorials out there. I feel this was because the purpose of each step was clearly communicated, so it never felt like I was just following instructions without knowing what affect they were having. The usefulness of each tool and method, in the wider scope of continuous deployment, was always made clear. All the parts were woven together seamlessly into the whole, in a way that felt natural and comprehensible.

I really liked how the steps involving the playbook built upon each other in a sensible way, at each step adding a new feature, then running it again. Doing it multiple times, each time slightly altering the playbook made me comfortable with the procedure and made me appreciate what each part of the playbook did.

My only overall gripe with the tutorial is the estimated length. It took me about double the suggested time to complete the tutorial (30min), and while that might be because I was trying to be extra thorough, I feel that more than fifteen minutes are required to truly comprehend the material. I do, however, have some suggestions for small improvements for some of the steps, which I will lay out below.

## Suggestions

### Introduction
The sentence `“In one of the two parts that form DevOps, operations, continuous deployment (CD) is the core principle.”` is unwieldy, so you may want to change it to `“Operations is one of the two parts that form DevOps, and its core principle is continuous deployment.“`. Also, I would suggest bumping up the estimated time to 25 min, since that is closer to my experience, and since the tutorial is aimed at beginners.

### Step 1
The first time I ran the `minikube start --wait=false` command, the process terminated after a few minutes with the output `killed`, which looks like another error than the one mentioned in the text. Rerunning fixed the error, just like the one mentioned in the text, so you should perhaps add to the instructions that the `killed` error can be solved in the same way.

### Step 3
Since the tutorial is aimed at beginners, it might be beneficial for them if you specify exactly what part of the output from the `kubectl cluster-info` command constitutes the clusters IP address. Though it is obvious to me what part is the IP and what part is the port number, to a complete beginner, it might not be. I suggest that you include an example output (just like you did for the hosts file) with the IP underlined, just to be sure (something like this: `Kubernetes master is running at https://_._._._:8443`). Furthermore, after running the `echo "[master]" > hosts` command, the hosts file would not show up until I refreshed the file tree. You should add instructions to press the `refresh tree` button at the top after running the command.

### Step 4
I believe the description for the `become` command could be extended, since this is the only command that I did not quite understand the purpose of. It would be great if you could explain what privilege escalation entails and what its purpose is.

### Step 5
I completed this tutorial two times, and the first time, after running the `ansible-playbook -i hosts playbook.yml` command, I did not receive the `ok=2` and `changed=1` message as expected. It seems the installation of yamllint failed, so I got to `ok=2` and `failed=1`. No step after this one failed however, and this step worked perfectly on my second run of the tutorial, so I am not quite sure what caused the error. Since this failure did not seem to affect the subsequent steps, perhaps this task could be removed or replaced with something less prone to failure, though this might just be user error, or something katacoda-related. Furthermore, just like in step 3, I had to refresh the file tree to be able to see the playbook file.

`I did not find any faults with the steps not mentioned.`

## Conclusion and easter egg
In conclusion, this was truly a great tutorial, with only some minor issues. I can add that I did find the easter egg, it was hidden in an ingenious way, both hard to find and very rewarding! You obviously worked hard on this tutorial and it shows. Bravo!