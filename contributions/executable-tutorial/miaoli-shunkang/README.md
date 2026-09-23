# Assignment Proposal

## Title

RAG Quality Gates: Automated Evaluation Pipelines with RAGAS

## Names and KTH ID

  - Miao Liu (miaoli@kth.se)
  - Shunkang Jia (shunkang@kth.se)

## Deadline

- Task 2

## Category

- Executable tutorial

## Description

We will build a Google Colab notebook that shows how to automatically test whether a RAG (Retrieval-Augmented Generation) application's answer quality holds up before a change is merged. The reader sets up a small RAG system with LangChain and FAISS, then runs RAGAS on a provided test set of questions with reference answers (and adds a couple of their own) to score retrieval and generation quality (faithfulness, answer relevancy, context precision, context recall). The reader then deliberately weakens the retrieval step, watches the scores drop, and finally wires the evaluation into a CI step that blocks the change if the scores fall below a threshold.

**Relevance**

A RAG application's quality depends heavily on its retrieval setup, such as the chunking strategy, the embedding model, and the retrieval parameters. These get changed often, but unlike application code, there is no test that catches it when such a change quietly makes answers worse. RAGAS turns answer quality into something measurable, making it possible to apply the same continuous integration discipline (automated checks that gate every change) to the retrieval and generation layer of an LLM application.

