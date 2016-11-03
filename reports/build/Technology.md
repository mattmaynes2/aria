## Aria Technologies

The Aria system is composed of many different technologies that each serve a different, task
specific purpose. This document outlines the details about the technologies chosen and the
reasons for them being selected. This document is broken down into the different subsystem
of the Aria system.

### Exchange Server

The exchange server is responsible for logging and sending messages throughout the Aria system.
The exchange server functions as the central communication point for all messages within the
Aria system. This server needs to support the main communication protocols that are required for
interfacing with several different protocols, including UDP, UPnP, Z-Wave and others. To
accommodate this requirement, Python 3 was selected as the primary language.

Python 3 offers support for most of the desired protocols since it can directly interface with
C it can support any external library implementations. As for the version decision of Python,
choosing 3 over version 2 allows us to use many of the new features that Python offers. It also
means that we are not writing Python using a set of deprecated standards.

- Python 3
- sqlite
- Pyflakes
- setuptools
- unittest
- nose
- ouimeaux

### HTTP Gateway

- NodeJS
- Express
- Mocha
- NPM
- Webpack
- JSHint

### Remote

- Webpack
- Babel
- NPM
- Jasmine
- Karma
- JSHint
- jQuery
- PhantomJS


