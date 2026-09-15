# Assignment Proposal

## Title

Prompt injection protection of a customer support AI bot using Promptfoo

## Names and KTH ID

  - Tobias Bjurström (tbju@kth.se)
  - Peter Byström  (pbystrom@kth.se )

## Deadline

- Week 4

## Category

- Demo


## Description

We demo setting up rules and policies for a customer support chatbot and test it against prompt injections and out of scope answers. Each prompt is wrapped by a text declaring the purpose and limitations of the chatbot. A simple devops pipeline is constructed using Github Actions and Promptfoo to define the tests for each pull request. We showcase:

- The chatbot being vulnerable to prompt injections and going out of scope when the text wrapper is not enabled.
- The wrapper being enabled and it preventing the previous behaviour.
- The .yaml file declaring the tests for the chatbot to pass. This defines the policy-as-code.
- The .yaml file for the Github Actions workflow.
- A pull request failing the defined tests by changing the wrapper text, thus breaking the pre-defined policy.

We plan to use Gemini CLI as the chatbot and give it simple instructions on what purpose and what limitations it has. For example, bookings at a restaurant, directions there etc. The prompt injection will be to simply try to go out of scope.

**Relevance**

Continuous maintenance of AI chatbots are becoming more and more common. OWASP cites multiple vulnerabilities in LLMs, for example prompt injections (LLM01:2026). By integrating the development and maintenance of the AI model using Devops principles, we show that such attacks can be prevented and remain prevented.
