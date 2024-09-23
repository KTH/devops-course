# Assignment Proposal

## Title

_TruffleHog - Identifying vulnerable management of secrets for IaC_

## Names and KTH ID

  - Olle Gunnemyr (ollegu@kth.se)
  - Sam Maltin (smhanna@kth.se)

## Deadline

- Week 5

## Category

- Presentation

## Description
This presentation aims to inform the audience of the security practice of managing secrets for Infrastructure as Code (IaC) and how the Open-Source tool TruffleHog can be used to detect vulnerable uses of secrets. We will first introduce the topic of managing secrets for IaC and what could be considered as poor uses with code snippets. Then present the tool TruffleHog, what it is, works and how it could be used to mitigate risks with exposed secrets in IaC environments. Lastly, we will reflect over Trufflehog, which cases it is most suitable and end with a conclusion.


**Relevance**
In IaC, poor management of secrets such as passwords and sensitive keys could easily lead to them being exposed and used by attackers for exploitations. For example, accidentally storing secrets using simple text files or Source Code Managements (SCMs) such as Git could lead to them being exposed. Therefore, it is important to use secrets scanning tools such as TruffleHog, which can scan the Git history and identify strings that could indicate a secret that has been committed to a repository,  allowing you to address these issues before they lead to exposure. 