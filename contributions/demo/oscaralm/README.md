# Demo proposal: Automatically publishing tested Node.js packages on npm with Github Actions 

## Member
Oscar Almqvist (oscaralm@kth.se)    
Github: [oscaralmqvist](https://github.com/oscaralm)

## Proposal

- Create a simple Node.js package with some functions & tests
- Set up two Github Actions that triggers when a pull request is merged to master
- When pull-request to master is created: 
  - Run tests
- When pull-request is accepted/merged:  
  - Publish the package to npm
