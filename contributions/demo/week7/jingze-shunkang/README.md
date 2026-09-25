# Assignment Proposal

## Title

Observing and Debugging a Browser Agent with [Arize Phoenix](https://github.com/Arize-ai/phoenix)

## Names and KTH ID

- Jingze Guo (jingze@kth.se)
- Shunkang Jia (shunkang@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

We will demonstrate an observable browser-agent workflow using the OpenAI Agents SDK, Playwright MCP, and Arize Phoenix. The agent will interact with Amazon: find products matching a budget and quantity requirement, add them to the cart, and verify the items, quantities, and displayed total.

Phoenix will capture agent, model, and client-side browser-tool traces. We will inspect tool inputs and outputs, repeated actions, and latency. To demonstrate debugging, we plan to configure an overly short client-side tool timeout, examine the resulting failure, then adjust the timeout and rerun from a clean browser session.

**Relevance**

The demo illustrates observability for tool-using agents. It connects multiple components and shows why a final answer alone is insufficient to assess execution or task completion.
