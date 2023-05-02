# Assignment Proposal

## Title

The OWASP DevSecOps Verification Standard

## Names and KTH ID

  - Minh Allan Dao (madao@kth.se)
  - Moritz Lübken (mlubken@kth.se)

## Deadline

- Week 7

## Category

- Presentation

## Description

Since DevOps has been a very popular topic for many years now, there is a huge variety of tools and techniques present.

As a company with less advanced DevOps processes or as a student just starting a career in software development or DevOps, a comprehensive overview of all techniques that should be applied would be very helpful. This is true even more when it comes to security since "sorry, we're new at this" is not a good excuse if you or your customers get hacked. 

Even acknowledging good faith efforts to introduce security across organizations of all kinds, OWASP (Open Worldwide Application Security Project) compiled a valuable list of the top 10 key security risks of web applications. The nature of the list indicates that current industry security standards are still lacking. With a high amount of reported incidents behind the common and arguably incomplex 10 categories representing broad buckets of security risks, it is evident that current security efforts are either insufficient or nowhere near comprehensive.

The [OWASP DevSecOps Verification Standard](https://github.com/OWASP/www-project-devsecops-verification-standard) is an open-source framework that tries to give a full list of best-practices to be applied
in DevSecOps. It can be used for gap analysis, project/maturity roadmaps or external maturity/risk assessments.

We aim to give an overview of the standard and its maturity levels. Given that seven minutes is quite brief to go into detail for all the phases, we will look at the *test phase* and especially at *DAST (Dynamic Application Security Testing)*. We will explain what DAST is, why it should be done, examine DAST from the lense of the standard, and will examine Zed Attack Proxy (which is conveniently one of OWASP's flasgship projects) as an example.

**Relevance**

To build secure DevOps environments and to develop safe and secure software, it is not enough to know some tools and techniques.
It needs robust norms and frameworks to make sure all necessary security measures have been taken.
While most traditional standards do not include a lot of DevSecOps requirements, the OWASP DevSecOps Verification Standard is designed
to provide requirements specifically for DevSecOps. However, it is not finished yet, as can be seen by a lot of "lorem ipsum" in the individual
requirement descriptions. The GitHub repository was initialized in 2022, so it is a very recent and ongoing project.

**Readings**
- https://github.com/OWASP/www-project-devsecops-verification-standard
- https://docs.docker.com/engine/security/trust/
- https://owasp.org/www-project-devsecops-maturity-model/ (Careful, it's something different)

**Misc**

@mlubken, @allandao