# Assignment Proposal

## Title
The event stream incident - vulnerabilities of open source dependencies and possible mitigations. 

## Names and KTH ID

  - Josephine Kuo (jkuo@kth.se)
  - Vanja Vidmark (vanjav@kth.se)

## Deadline

- Week 6

## Category

- Presentation

## Description

We are going to bring light to the topic of using third party libraries without caution, using the event stream incident as an example. We will highlight some key reasons for these attacks such as blind trust, handing over projects insecurely, non-present security checks and the tradeoff between security and openness. 

We will then go over three mitigations to resolve this issue. 
- Dependency pinning. That is to require specific versions of libraries, rather than ranges to prevent auto-updates from pulling in malicious versions.
- Using lockfiles (such as package-lock.json in NPM) to record the exact versions of installed packages, minimizing the risk of unintended updates.
- Scanning for known vulnerabilities in the dependencies using npm audit. 

**Relevance**

In DevOps, automation often relies on third-party libraries, and this incident demonstrates the vulnerability of open-source dependencies. Ensuring the security of external code is crucial, as compromised libraries can introduce security risks into the CI/CD pipeline without immediate detection. 
