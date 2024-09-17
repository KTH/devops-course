# Assignment Proposal

## The risk of using open-source ecosystems

## Names and KTH ID

  - Josephine Kuo (jkuo@kth.se)
  - Vanja Vidmark (vanjav@kth.se)

## Deadline

- Week 6

## Category

- Presentation

## Description

We are going to bring light to the topic of using third party libraries without caution, using the event stream incident as an example. We will highlight some key reasons for these attacks such as blind trust, handing over projects insecurely, non-present security checks and the tradeoff between security and openness. 

We will then go over some mitigations and “good practices” to resolve this issue. One example of a mitigation is dependency pinning, that is to require specific versions of libraries, rather than ranges to prevent auto-updates from pulling in malicious versions.

**Relevance**

In DevOps, automation often relies on third-party libraries, and this incident demonstrates the vulnerability of open-source dependencies. Ensuring the security of external code is crucial, as compromised libraries can introduce security risks into the CI/CD pipeline without immediate detection. 
