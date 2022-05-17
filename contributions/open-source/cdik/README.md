# Assignment Proposal

## Title

Grafana: Migrate from Enzyme to React Testing Library

## Names and KTH ID

- Chrysoula Dikonimaki (cdik@kth.se)

## Deadline

Deadline for task 5

## Category

Contribution to open-source

## Description

[Grafana](https://github.com/grafana/grafana) is a very popular open-source platform for monitoring and observability. 
Its frontend is written in React and all the frontend tests were written in Enzyme, a Javascript testing library which stopped supporting React versions >=17.
That's why all the tests need to be migrated from Enzyme to a better solution called React Testing Library. 
React Testing Library is a lot different from the Enzyme since it focuses on testing the DOM and not the React component. 
This way, we can be more confident that our domain logic we want our app to have is actually implemented and the user can use the app as expected.
So, in general, React Testing Library is a solution for writting better tests compared to Enzyme.

I would like to contribute to the this migration.

Issue: [#48253](https://github.com/grafana/grafana/issues/48253)
