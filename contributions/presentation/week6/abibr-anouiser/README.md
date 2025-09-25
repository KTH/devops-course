# Assignment Proposal

## Title

Week 6: Can Obfuscation Protect Python in DevSecOps?

## Names and KTH ID

  - Ahmedhadi Bashir (abibr@kth.se)
  - Amin Nouiser (anouiser@kth.se)

## Deadline

- Week 6

## Category

- Presentation

## Description

This presentation explores **PyArmor**, a Python obfuscation and licensing tool that helps teams protect source code from reverse engineering and unauthorized use.  

In many DevOps environments, Python code including deployment scripts, automation tools must be shared across teams, deployed to servers, or distributed as packages. Without protection, this code can be easily read, modified, or stolen.  

PyArmor addresses this challenge by:  
- Obfuscating Python bytecode to make reverse engineering difficult.  
- Enabling runtime checks and licensing controls.  
- Integrating into build pipelines to automatically produce protected artifacts.  

We will explain how PyArmor works, show an example of obfuscating a Python script, and discuss how it can be integrated into a CI/CD pipeline. Finally, we will reflect on the trade-offs between obfuscation (security through obscurity) and other DevSecOps practices like dependency scanning.  


**Relevance**

PyArmor is relevant to DevOps because it allows teams to integrate code protection directly into CI/CD pipelines, ensuring that deployment scripts, and internal codebase. Python packages are harder to reverse engineer or misuse. This helps safeguard intellectual property, reduce leaks, and support compliance without disrupting automation workflows.