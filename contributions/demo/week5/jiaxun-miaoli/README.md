# Assignment Proposal

## Title

Local-first Infrastructure as Code: emulating AWS with MiniStack, orchestrated by .NET Aspire

## Names and KTH ID

  - Jiaxun Wei (jiaxun@kth.se)
  - Miao Liu (miaoli@kth.se)

## Deadline

- Week 5

## Category

- Demo

## Description

We want to demonstrate an Infrastructure as Code workflow that runs locally, with no cloud account involved. The solution is based on a [.NET Aspire](https://learn.microsoft.com/dotnet/aspire/) AppHost that starts [MiniStack](https://ministack.org), a free local emulator of AWS. We will deploy an AWS CDK stack to it, and then change the stack live, redeploy it, and show a small service that reads and writes the new resources through the AWS SDK.

**Relevance**

When we practise Infrastructure as Code, every change is normally verified by deploying it to a real cloud account, which is faithful but slow, costs money, and requires credentials for everyone on the team. Running the same stack against a local emulator moves that feedback into the inner development loop and makes infrastructure changes cheap to test. Reproducible environments and dev/prod parity are core DevOps concerns, and the demo shows both what local emulation buys and where it breaks down.
