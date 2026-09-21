# Assignment Proposal
 
## Title
Automated Testing, APK Builds & Firebase Feature Flags for Mobile Application
 
## Names and KTH ID
- Pavlos Spanoudakis (pavloss@kth.se)
- Bogdan-Laurentiu Stefanescu (blst@kth.se)

## Deadline
Week 2
 
## Category
Demo
 
## Description
For this demo, we'll set up a DevOps workflow for an existing mobile application, covering automated testing, automated delivery, and controlled feature rollout.

We'll configure GitHub Actions to automatically run the test suite whenever a pull request is opened or code is pushed, so issues are caught before reaching the main branch. We'll also add a build pipeline that automatically generates an APK on pushes to a designated branch, ensuring a testable build is always available without manual steps. Finally, we'll introduce feature flags using Firebase Remote Config, allowing features to be toggled on or off remotely without requiring a new app release.

**Relevance**
This demo directly covers this week's topics:

- **Testing automation** - building an automated test suite for the mobile app
- **Continuous Integration** - GitHub Actions run the test suite automatically from version control on every change, and create an APK build if the tests pass.
- **Feature flags** - Firebase Remote Config is used to toggle app features on or off remotely, without shipping a new release.
