# Course automation: Checking link validity in the course github text descriptions

## Members

Chen, Zidi: zidi@kth.se, https://github.com/Chen-Zidi
Chen, Sihan sihanc@kth.se, https://github.com/Spycsh


## Content

You can view the concrete implementation code and the usage of this automation tool with the link below:

[https://github.com/Chen-Zidi/check-modified-contents-link-validity-action](https://github.com/Chen-Zidi/check-modified-contents-link-validity-action)

This project creates GitHub action, which checks the validity of the links in the modified content for a pull request. If there are invalid links in the added content, the output of the GitHub action should be false, and the pull request will be **closed**. Meanwhile, the invalid links are **commented** in the closed pull request so contributers can be notified about the invalid links. This action should be triggered by pull_request_target event, which means it can serve as an early-check before manual merging. Notice that we only check the links which start with **http://** and **https://**.

You can view a demo of our action here [https://github.com/Chen-Zidi/devops-course/](https://github.com/Chen-Zidi/devops-course/), and the action name is `check-link-validity`.
