# Assignment Proposal

## Title

Ensuring the integrity and source of software packages

## Names and KTH ID

- Martin Lindefors (lindefor@kth.se)
- Melvin Jakobsson (melvinj@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

We intend to demonstrate how easy it can be to fall victim to attacks such as typosquatting or dependency confusion. We will do this by creating two bogus packages in `pip` & `npm` and highlight some weaknesses in those package managers. We will then show how to cryptographically verify the authenticity of packages using Sigstore & `npm audit`. Finally we will end with a note on the importance of verifying the origin of software, an often overlooked aspect of software development.

**Relevance**

Since the demo will include both package managers and software verification it is relevant for both of this weeks topics. In particular, verifying the origin of software packages is more relevant than ever because of the widespread nature of package managers and the comfortability of outsourcing code to these packages. Furthermore, there are several examples of attacks related to package managers.