# Assignment Proposal

## Title

LLM-Powered Multi-Agent Collaboration for Intelligent Industrial On-Call Automation (ASE 2025)

## Names and KTH ID

  - Miao Liu (miaoli@kth.se)
  - Jingze Guo (jingze@kth.se)

## Deadline

- Week 4

## Category

- Scientific paper

## Description

We plan to focus on the tree-search-based multi-agent planning mechanism that lets expert agents collaboratively explore solution paths and backtrack via reflection when a path fails, discuss the reported production results (21-second average response time versus the previous 4.6-hour manual baseline) together with the ablation study showing each module's individual contribution, and contrast OncallX's centralized, LLM-agent-driven approach with two other recent industrial systems not cited in the paper: TrioXpert (ASE 2025), which fuses multimodal metrics/logs/traces data rather than relying on LLM reasoning alone, and Comfey (FSE 2026), which triages incidents through decentralized per-team agents negotiating via a shared routing table instead of OncallX's single central planner.

**Relevance**

On-call response is one of the feedback loops that DevOps depends on to keep incidents from becoming outages, but manual triage does not scale with the growth of microservice systems. OncallX shows what happens when that loop is automated with LLM agents instead of humans or static classifiers. This is AIOps in its current LLM-driven form: using LLM agents to automate a DevOps practice that used to require humans.
