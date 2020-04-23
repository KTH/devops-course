# Demo Proposal

## Members

- Vincent Lohse vplohse@kth.se @olapiv
- Albert Asratyan asratyan@kth.se @Goradux

## Topic

Using Github Actions to run tests on Docker containers.

## Details

Generally, Github Actions is a great way to run tests on your application. However, you may have dockerized your application along with other applications that are supposed to work together with docker-compose. We want to try writing tests in Github Actions that first verify that your application actually builds via Docker and is also able to work with other containers.
