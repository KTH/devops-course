# Video demo: Automated development pipeline for Chrome extensions

## Members

Andreas Kärrby (karrby@kth.se)  
Github: [andreaskth](https://github.com/andreaskth)

Henrik Kultala (kultala@kth.se)  
Github: [hengque](https://github.com/hengque)

## Proposal

We would like to create a video demonstrating setup of an automated CI/CD development pipeline for developing and publishing Chrome extensions ("plugins") to the ['extensions' part of Chrome Web Store](https://chrome.google.com/webstore/category/extensions) (and to registered testers of the extension).

A rough list of things we plan to show (level of detail will be adapted to fit given video length):

- Brief introduction of how browser extensions work in Chrome (covering information such as that available [here](https://developer.chrome.com/docs/extensions/mv3/overview/))
- Show a basic template extension (a "Hello world" of sorts) whose code we will modify (and which will be the 'thing-to-deploy' in the pipeline)
- Show the actual steps in the pipeline (running automated tests, merging if they pass, deploying automatically), how they work and are setup
- Finally, showcase the pipeline working by changing some code and have it be automatically deployed to the web store and automatically updated in browsers of [trusted testers](https://developer.chrome.com/docs/webstore/using_webstore_api/#trustedtesters)
- Conclusions/take-home message

## Sources
https://developer.chrome.com/docs/extensions/mv3/overview/  
https://developer.chrome.com/docs/webstore/using_webstore_api/#trustedtesters  
