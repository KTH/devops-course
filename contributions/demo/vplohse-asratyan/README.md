# Demo Proposal

## Members

- Vincent Lohse vplohse@kth.se @olapiv
- Albert Asratyan asratyan@kth.se @Goradux

## Topic

Using Newman in Github Actions to run tests on Docker containers.

## Details

Generally, Github Actions is a great way to run tests on your application. However, you may have dockerized your application along with other applications that are supposed to work together with docker-compose.

We want to try using Github Actions to check whether our entire configuration is working. More specifically, we are building a web-server configuration for which we will be running Rest-API tests that we have previously written in Postman. Running these tests in Github Actions is possible with Postman's CLI component, called Newman. If these tests go through, we can be sure our web server configuration works as we expect it to be.

## Screencast link

[https://youtu.be/xiB2oGi45Gs](https://youtu.be/xiB2oGi45Gs)

## Demo Repository

[https://github.com/olapiv/kth-newman-docker-ci-demo](https://github.com/olapiv/kth-newman-docker-ci-demo)
