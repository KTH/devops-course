# Week 7

# Assignment Proposal

## Title
- Java Bytecode Normalization for Code Similarity Analysis

## Names and KTH ID

- Quang M Nguyen (mqnguyen@kth.se) 

## Deadline

- Week 7
## Category

- Scientific Paper
## Description
This work focuses on enabling similarity detection in Java bytecode, which is crucial for scenarios like plagiarism detection, copyright compliance, and Software Bill of Materials (SBOM) creation when source code is unavailable. Java bytecode varies significantly depending on compiler versions, complicating similarity analysis. To address this, the authors introduce a method called bytecode normalization through their tool jNorm, which uses Jimple as an intermediate representation to standardize bytecode across different compilation environments. Evaluating over 300 Java projects, they found that normalizing bytecode reduced compiler-induced differences by over 99%, significantly improving the reliability of bytecode similarity analysis.

**Relevance**
This work on Java bytecode similarity analysis is relevant to DevOps, particularly in Software Bill of Materials (SBOM) creation, vulnerability management, compliance verification and checking for copyright material. Since source code is often unavailable, bytecode normalization allows for consistent identification of software components, aiding SBOM accuracy and vulnerability detection. Additionally, it helps ensure artifact consistency across environments, which is crucial for reliable deployment and debugging. These capabilities are key in supporting security, compliance, and quality control within DevOps workflows.