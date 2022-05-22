# Assignment Proposal

## Title

Grafana: Migrate from Enzyme to React Testing Library + Improve Keyboard A11y (Accessibility)

## Names and KTH ID

- Chrysoula Dikonimaki (cdik@kth.se)

## Deadline

Deadline for task 5

## Category

Contribution to open-source

## Description

[Grafana](https://github.com/grafana/grafana) is a very popular open-source platform for monitoring and observability. 

1. Test Migration

Its frontend is written in React and all the frontend tests were written in Enzyme, a Javascript testing library which stopped supporting React versions >=17.
That's why all the tests need to be migrated from Enzyme to a better solution called React Testing Library. 
React Testing Library is a lot different from the Enzyme since it focuses on testing the DOM and not the React component. 
This way, we can be more confident that our domain logic we want our app to have is actually implemented and the user can use the app as expected.
So, in general, React Testing Library is a solution for writting better tests compared to Enzyme.

I would like to contribute to the this migration.

Issue: [#48253](https://github.com/grafana/grafana/issues/48253)

2. A11y Bug

A11y (Accessibility - "A" then 11 letters then "y") in web development means making websites that can be used by as many people as possible, including people with disabilities. Grafana can be improved to support A11y and make it easier for people to navigate through the app without using a mouse but using the keyboard or voice over.

For this reason, extra buttons have to be added to reduce the number of times the user presses the arrow keys.

Issue: [#46498](https://github.com/grafana/grafana/issues/46498)


Submission:

Grading Citeria : 
✔️ The contribution fixes bugs
✔️ The contribution is a difficult piece of engineering
✔️ There is an interesting engineering conversation with the maintainers
✔️ The contribution is merged in the main branch.

1. Test Migration
* Pull Requests: [#48887](https://github.com/grafana/grafana/pull/48887), [#48918](https://github.com/grafana/grafana/pull/48918), [#48982](https://github.com/grafana/grafana/pull/48982), [#49107](https://github.com/grafana/grafana/pull/49107), [#49119](https://github.com/grafana/grafana/pull/49119), [#49148](https://github.com/grafana/grafana/pull/49148)

* Why are these tests important? Why is this migration important?

Grafana has 3 types of tests: frontend tests, backend tests and end-to-end tests. Given that Grafana is a UI tool for observability, having good tests to test that the UI functionality works is very important. 
Looking the package.json file, we see that the React version that is used by Grafana is the ‘17.0.2’. Enzyme is not compatible with this file of React. It is compatible with React versions<16. Given the importance of these tests, problems will occur in the future if we don't move to a compatible solution.
That’s why there is a need to migrate to React Testing Library which is one of the top solutions to test React UIs these days. 
React Testing Library is a very lightweight solution which provides lightweight functions to test DOM in a way that encourages good testing practices.  We do not focus on testing the React component. This way our tests are not tight with the specific implementation but they test if the business logic of our application is satisfied. We test our components the way the fuser will.
Compared to Enzyme, the React Testing Library is better as it does not allow you to access the internal workings of the component so this way discourages bad testing practices.  

* Difficulty?

In order to migrate from one tool to another somebody needs to have an understanding of both tools. Even though Enzyme and React Testing Library have the same purpose, the way of thinking to write these tests is different. So migrating requires somebody to study both frameworks and study some basic ways to think when migrating. Then focusing on the React Testing Library and how to write the specific type of tests given. For example, the way we find things is different since we focus on how the user find things so I had to find alternatives ways to get the DOM elements since the existenting ways with Enzyme are not good practises and/or they are not easily supported to be written in the React Testing Library. An very characteristic example that I encounted is when I had a html list. Using Enzyme you find it using the 'li' tag. On the other hand, when writting tests with React Testing Library, somebody has to get them by a role which is called 'listitem'. There many roles like this that somebody should search for when doing the migration. I had to search the DOM tree to find the best option to select what I wanted based on the priority a user gives when navigating through the app.

* Test selection?

I started with simpler tests which were focusing on testing the existence of a text etc. Then, I moved to more complex tests which required to change the logic the tests are written due to the difference of the tools. For example, the tests written with Enzyme sometimes render Components which is something you cannot do with the React Testing Library because we should focus on testing the DOM elements (better practise). Then, I've written tests for user events, like hover or click. 


2. A11y Bug
* Pull Requests: [#49075](https://github.com/grafana/grafana/pull/49075), [#49076](https://github.com/grafana/grafana/pull/49076)
* Solution? I proposed two different solutions that could work and after having a discussion with mentainers they decided which solution they currently want to use.
