---
title: HashiCorp Vault
subtitle: Manage Secrets and Protect Sensitive Data
author: Arnthór Jónsson
date: \today
fontsize: 12pt
---

## What is it?

"Vault secures, store and tightly controls access to tokens, passwords, certificates, encryption keys for protecting secrets and other sensitive data using a UI, CLI, or HTTP API."

## Dynamic Secrets

- Never provide "root" credentials to clients 
- Provide limited access credentials based on role
- Generate __On Demand__ when requested
- Audit trail can identify point of compromise 

## Dynamic Secrets

![](https://devopscube.com/wp-content/uploads/2018/07/hashicorp-vault.jpg)

<!-- - Client like myself connects to vault and says I want credentials -->
<!-- - Vaults checks I'm actually authenticated and able to do this -->
<!-- - Then it goes and talks to the database and says create a new dynamic random username and password -->
<!-- - Audit what has happened and hand it back to the client -->

## Take Home Message

Dynamic generation of unique credentials allows us to create a moving target for attackers and minimize the risk of exposing credentials.

<!-- ![](https://devopscube.com/wp-content/uploads/2018/07/hashicorp-vault.jpg){ width=85% } -->
<!-- vim:tw=60
-->
