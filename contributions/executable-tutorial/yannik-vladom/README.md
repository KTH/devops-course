# Pijul: Haunting Git at night

[Pijul](https://pijul.org/) is a new version control system, designed with a different mindset than git. Instead of being snapshot based it manages commits as a set of sound patches. As such it allows for greater flexibility and ease of use while also providing the performance commonly accredited to to snapshot based VCSs.

In the tutorial we will:

1. discuss concepts
   - introduce patch-based version control
   - its differences to snapshot based version control
2. ~show how to install `pijul` (as of now its not yet included in most distributions)~
   Compiling the program from scratch takes quite a while. Also due to the fact that we can only wrote the instructions from the documentation, we omitted this step and use a preconfigured docker image instead.
   The installation instructions from said documentation are still referred to so this tutorial could as well be executed locally.
3. compare it to `git` the de facto standard tool
   - how to clone a repo
   - tracking changes
   - ~`git branch`~ `pijul channels`
   - undoing changes
   - pushing
   - contributing

The tutorial will be available preferably on Katacoda or an equivalent platform.

Link to the tutorial: https://www.katacoda.com/ysndr/scenarios/pijul
Link to the source: https://github.com/ysndr/katacoda-scenarios/tree/main/pijul


## Authors

- Yannik Sander ([yannik@kth.se](mailto:yannik@kth.se)), [ysndr](https://github.com/ysndr)
- Vlado Mitrovic ([vladom@kth.se](mailto:vladom@kth.se)), [vladomitrovic](https://github.com/vladomitrovic)
