# Assignment Proposal

## Title
Poisoning Web-Scale Training Datasets is Practical

## Names and KTH ID
* Anica Krüger (anicak@kth.se)
* Shreyas Sawai (sawai@kth.se)

## Deadline
* Week 4

## Category
* Scientific paper

## Description
This paper presents two novel, practical poisoning attacks which target web scale training datasets used for deep learning models. The authors explain how an attacker can introduce malicious data into these datasets by exploiting trust in how datasets are collected and updated. The paper presents two practical poisoning attacks on large scale web datasets used for training AI models. The first, split view poisoning, exploits mutable web content like expired domains to inject malicious data. The second, frontrunning poisoning, targets snapshot based datasets like Wikipedia by timing harmful edits just before data collection. These attacks are low cost and effective against major datasets. The authors propose defenses such as integrity checks using cryptographic hashes and randomized or delayed snapshots to mitigate these threats. The work highlights the urgent need for improved dataset security and transparency in AI development.

  The paper can be found here: [link to paper](https://ieeexplore.ieee.org/abstract/document/10646610).

**Relevance**
This paper is important for cybersecurity and AI safety because it shows how attackers can secretly tamper with large datasets used to train AI models, causing them to make wrong or unsafe decisions. These poisoning attacks are easy and cheap to carry out, especially since many AI systems rely on web scraped data. It highlights the need for strong defenses like data integrity checks and monitoring to keep AI models trustworthy and secure. In MLOps, managing clean and reliable data is key, so the paper’s findings stress the importance of protecting training data throughout the ML lifecycle to ensure safe and accurate AI deployment.
