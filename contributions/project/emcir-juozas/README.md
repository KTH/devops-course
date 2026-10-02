# Assignment Proposal

## Title

Reproducible Testing and Secure Delivery for a Sailing Team MQTT Web Application

## Names and KTH ID

- Ettore Mugisha Cirillo (emcir@kth.se)
- Juozas Skarbalius (juozas@kth.se)

## Deadline

- Task 3

## Category

- Project

## Description

We propose extending an existing Sailing Team monitoring application with a reproducible testing environment and an integrated DevOps pipeline. The application is an Angular/TypeScript frontend that communicates directly with an MQTT broker over secure WebSockets. It displays live telemetry and a map, handles connection failures and stale data, and provides role-dependent controls for sending commands.

The main challenge is validating changes without relying on the physical boat or its operational broker. Current automated checks do not cover the complete browser-to-broker interaction over a real connection. We will extend this coverage with integration and end-to-end tests, using a containerized boat simulator and a real Eclipse Mosquitto broker. The simulator will publish representative telemetry and handle a defined subset of commands using the application's MQTT topics and message formats. This will allow us to verify actual network communication, broker permissions and recovery from failures.

The planned workflow and deliverables are:

- **Build and testing (CI):** GitHub Actions will run linting, type checks, unit tests and builds on pull requests and pushes to `main`. It will then provision an isolated integration environment and run browser-based E2E tests with Playwright. Scenarios will cover telemetry reaching the UI, malformed messages, stale data after the simulator stops, recovery after a broker restart, and broker-enforced denial of unauthorized guest commands. Test results and failure diagnostics will be retained before the environment is destroyed.
- **Deployment (CD):** after successful checks on `main`, GitHub Actions will deploy the validated frontend build to GitHub Pages. The same build output will be used for E2E testing and deployment, with public environment settings supplied separately at runtime. GitHub Pages hosts the frontend; the operational MQTT broker remains an external service and is not provisioned by this pipeline.
- **Infrastructure as code:** Terraform with the Docker provider will manage the integration environment's network, broker, frontend server and simulator containers, together with the required configuration mounts. The environment will be reproducible locally and in CI. We will validate the configuration and verify that a second apply produces no changes. Terraform is chosen to practise explicit resource dependencies, planning and state management; Docker Compose would also be a reasonable choice at this scale. Test credentials and TLS material will be supplied or generated at runtime, and secrets and Terraform state will stay outside version control.
- **Development platform:** GitHub will host the unified project repository, issues and pull requests, with required CI checks and peer review before merging.
- **Quality and security automation:** ESLint, Gitleaks secret scanning and dependency vulnerability scanning will run in CI. Detected secrets, lint errors and dependency findings above a documented severity threshold will block the release. Controlled examples using nonfunctional test tokens will demonstrate that the checks detect problems. Any exceptions will be narrow and documented.
- **Repository and report:** the repository will contain the application, simulator, infrastructure, workflows, tests and reproduction instructions. Development and test tooling will be runnable through containers. A 2-3 page report will explain the architecture, component interactions, design decisions and limitations, including synthetic telemetry, differences between Mosquitto and the operational broker, and the limits of automated security checks.

**Relevance**

This project addresses a practical delivery problem: how to change a connected monitoring application confidently when its hardware is not always available. Infrastructure as code creates the test environment, a real broker and simulator exercise the application, quality and security checks gate changes, and CD publishes the validated frontend. These components form one workflow rather than separate demonstrations of tools.
