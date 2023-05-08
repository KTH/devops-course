# Assignment Proposal

## Title

SOPS: Encrypt and decrypt files automatically

## Names and KTH ID

  - Gabriel Christensson (gabchr@kth.se)
  - Martin Arenbro (arenbro@kth.se)

## Deadline

Week 7

## Category

Demo

## Description

SOPS (Secrets Operations) is a simple and light-weight tool for editing and automatically encrypt/decrypt files. In contrast to traditional encryption services, SOPS encrypts a file immediately when it is saved and decrypts it when it is opened in a fully automated fashion. It is even possible to choose different encryption methods such as GPG, AWS KMS, Azure Key Vault, and more. We wish to demonstrate how SOPS can be used with GPG and Github.

**Relevance**

SOPS provides automated encryption/decryption of files, making using a git repo (or similar) to store secrets viable and offers easy collaboration. For example, a CI may read entire files or even extract specific fields from encrypted JSON/YAML files directly from the repo.
