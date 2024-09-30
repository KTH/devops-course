# Assignment Proposal

## Title

End-to-end training of a neural network to deployment in a live application

## Names and KTH ID

  - Fredrik Gölman (golman@kth.se)

## Deadline
- Task 2

## Category
- Executable tutorial

## Description

I'd like to make an executable tutorial that goes through the training of a neural network in a Jupyter notebook on Colab, handling the intermediary steps, and deployment to some live application, so the end-to-end process. I'd put limited focus on the ML aspects and greater focus on the DevOps aspects. I'd like to whip together my own functionality for the DevOps parts, if I may, as it's a fun learning experience and could be meaningful scripts for future usage. The deployment criteria for the model could be to exceed previous test data accuracy, but there could also be any other reasonable criteria. I haven't fully decided on the functionality for the MLops/DevOps part. The bare minimum is actually deploying the model live when fulfilling the criteria. Other things being considered are model storage/rollback, job scheduling/queue in running notebooks, monitoring of multiple notebooks, etc.

Architecture wise there would be:
- The Colab notebook running the ML stuff (and some network connectivity).
- An MLops tool consisting of a backend and a corresponding GUI (web).
- A demo web application that uses the model on the backend.

I asked TA about this briefly in a lab session (not previous, but one before that) and it sounded OK. I meant to register it earlier, but other coursework came in between. I think it's still OK to register an MLops task since it's asynchronous and there is no "week" folder structure in the directory tree. So if it is, and the proposal sounds OK, is all I have to do commit to a deadline and deliver?

**Relevance**

Jupyter Notebook/Lab is often used for processing, preparing, and visualizing data, as well as subsequently training machine learning models. The process of deriving a model is often an iterative process to determine suitable model architectures and optimal hyperparameters. Models may furthermore require continuous altering after deployment as more data becomes available or use cases change. This process is presumably often done manually, particularly as data scientists and conventional developers may be different teams, but there are clear benefits in automating the process.
