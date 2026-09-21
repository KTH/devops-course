# Assignment Proposal

## Title

Learning-to-Rank vs Ranking-to-Learn: Strategies for Regression Testing in Continuous Integration

## Names and KTH ID

  - Miami Alvelistin (miami@kth.se)
  - Mostafa Faik (mfaik@kth.se)

## Deadline

- Week 4

## Category

- Scientific paper

## Description

We propose to present the paper *Learning-to-Rank vs Ranking-to-Learn: Strategies for Regression Testing in Continuous Integration* by Antonia Bertolino, Antonio Guerriero, Breno Miranda, Roberto Pietrantuono, and Stefano Russo, published at the 42nd ACM/IEEE International Conference on Software Engineering (ICSE 2020).

The paper investigates the use of machine learning for regression test prioritization in Continuous Integration (CI). In CI environments, software changes are frequently integrated and automatically tested. As test suites grow, executing all regression tests can delay feedback to developers. The paper investigates machine-learning-based strategies for prioritizing test cases so that tests more likely to reveal failures can be executed earlier.

The presentation will explain the problem addressed by the paper, its main contribution, experimental methodology, and results. We will focus on the technical mechanisms behind machine-learning-based test prioritization and compare the paper's learning-to-rank and ranking-to-learn strategies.

We will critically examine the paper's assumptions, limitations, and threats to validity, including its reliance on historical testing data and the generalizability of its results to different software projects and CI environments.

For related work, we will focus on recent research published after the selected paper. We will compare the paper with *Revisiting Machine Learning based Test Case Prioritization for Continuous Integration* by Zhao, Hao, and Zhang (ICSME 2023), which revisits ML-based test case prioritization using a common experimental setup and evaluates multiple techniques across open-source projects. We will also compare it with *Revisiting Test-Case Prioritization on Long-Running Test Suites* by Cheng, Wang, Jabbarvand, and Marinov (ISSTA 2024), which studies test-case prioritization using a large dataset of CI builds and test-suite runs from large open-source projects.

The presentation will conclude by discussing when machine-learning-based test prioritization is useful in DevOps environments, when its additional complexity may not be justified, and which types of CI pipelines and development teams are most likely to benefit from it.

**Relevance**

The paper is directly relevant to DevOps because it addresses Continuous Integration, automated regression testing, and rapid feedback following software changes. Automated testing is a central part of CI/CD pipelines, but large test suites can become a bottleneck as software projects grow.

Machine-learning-based test prioritization provides an example of applying data-driven techniques to improve an existing DevOps automation process. By prioritizing tests that are more likely to reveal failures, the approach aims to provide useful feedback earlier while still allowing the complete test suite to be executed.

The topic also connects to the Week 4 focus on MLOps/AIOps/LLMOps by examining how machine learning can be incorporated into an established software-engineering workflow rather than being treated as an isolated ML task.
