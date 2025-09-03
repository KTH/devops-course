# Assignment Proposal

## Title
Safe Friday Deployments: How AWS Uses Canary Releases to Minimize Risk and Maximize Agility

## Names and KTH ID

  - Shreyas Sawai (sawai@kth.se)
  - Miguel Valgañón (valganon@kth.se)

## Deadline
- Week 3

## Category
- Presentation

## Description

This is a case study about how AWS engineering teams implemented canary release strategies to enable safe production deployments even on Fridays, where you dont want to waste your weekend on debugging the issues :). This approach talks about how new application versions are initially released to a small subset of users (the "canary group"), while the majority continue using the existing stable version. The AWS team closely monitors key performance indicators (KPIs) such as error rates, response times, and system health using AWS's observability tools like CloudWatch. If the canary deployment shows no critical issues, the update is gradually rolled out to the full user base. Should anomalies arise, the deployment is instantly rolled back, minimizing user impact and ensuring service reliability.

**Relevance**

This case is highly relevant to Continuous Deployment best practices. It demonstrates how canary releases reduce deployment risk, allowing teams to confidently deliver code before weekends or holidays when incident response is harder. This technique also leverage real time monitoring and automated rollback to prevent widespread outages, ensuring user experience is protected. Additionally, it also facilitates agile and frequent releases by allowing rapid feedback, safer experimentation, and increased resilience during high-risk periods.