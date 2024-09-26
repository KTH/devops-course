# Assignment Proposal

## Title

Integrate RetireJS into Github workflow through OWASP ZAP

## Names and KTH ID

- Olle Gunnemyr (ollegu@kth.se)
- Sam Maltin (smhanna@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

We will start by extending the ability of OWASP ZAP by integrating the open-source tool RetireJS into the ZAP scanning process. RetireJS is built to specifically scan used JavaScript libraries for known vulnerabilities. The scan will then be integrated into a Github CI/CD pipeline via Github Actions, thus mitigating the risks from vulnerable libraries early in the Software Development Life Cycle (SDLC).

_Relevance

With the growing number of Javascript libraries on the web and Node.js application, it is easier to unknowingly choose insecure libraries during development. Automating the vulnerability detection in the CI/CD pipeline through OWASP ZAP and extending the scanning by also considering vulnerable Javascript Libraries through RetireJS, would be a relevant security practice within DevSecOps. 