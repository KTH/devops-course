# Assignment Proposal

## Title

Enforced software authenticity for K8s using Sigstore and Kyverno

## Names and KTH ID

  - Ivar Boqvist (ivarbo@kth.se)
  - Amin Nouiser (anouiser@kth.se)

## Deadline

- Week 6

## Category

- Demo

## Description

Typesquatting and tampering remain as common techniques used to attack software supply chains. By default, a Kubernetes cluster will run any image you point it to without any checks to see if the image is provided by a trusted author. By setting up [Kyverno](https://kyverno.io/) on the cluster enforcing [Sigstore](https://www.sigstore.dev/) signatures, these types of exploits can be partially mitigated.

In this demo we will present how to incorporate Sigstore into an existing CI-CD pipe to automatically sign new container builds and how to use Kyverno in a cluster to enforce trusted image execution using policies. To further ensure code provenance, we will configure a GitHub Runner to only allow [gitsign](https://github.com/sigstore/gitsign)-signed commits and, if that can be assured, self-sign main-branch builds using Sigstore. The demo will look into edge cases where the setup may be restricted or break in any way. 

**Relevance**

Using Kyverno to verify image signatures using Sigstore is relevant to DevOps, or specifically DevSecOps, as it provides for a secure and automated way to ensure only builds signed by a verified workflow identity can be run inside your K8s cluster. Using Sigstore on its own without Kyverno provides for a way to sign and verify builds, but nothing prevents unsigned or improperly signed builds from being run on the K8s cluster by someone with access to it. 

