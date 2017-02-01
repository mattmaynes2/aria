### Remote Testing {#section-test-remote}

#### Context {-}

The gateway and remote client work closely to provide control and observability to the Aria system.
These components are written in JavaScript and need to communicate using a REST API. The gateway
is responsible for translating REST communications to the required IPC communicates for all
operations. The remote is simply a user interface to interacting with the controls provided by
the gateway.

#### Unit Testing {-}

The gateway is executed in node.js, a server side environment for JavaScript applications. In
order to test the internal behaviours of the gateway, a common BDD testing framework called
*mocha* was used. Mocha allows for simple feature based unit tests to be constructed and executed
in the node.js environment. Mocha also provides capabilities for spying and mocking internal
classes from the gateway code.

The remote client, although written in the same language, runs in very different environments.
The web client has to be able to run in a browser. In order to test the functionality of the
remote, a unit testing framework called *karma* was used. Karma is a test runner that uses
*PhantomJS* to execute its unit tests in a browser environment.

This unit testing library is run against every build of the system and is used for regression
testing purposes.

#### Integration Testing {-}

In order to isolate the behaviours of the gateway and remote from the exchange server, an
interactive integration testing suite was added. This testing suite mocks all communication
between the gateway and exchange server in order to control the behaviour of the system.
This integration test allows the gateway to run, server the remote client and execute all
of the behaviours described by its API. This form of testing has been used to manually test
the user interface functionality in a controlled environment.

To start the gateway's integration tests, the gateway executable simply needs to be passed the
`--test` flag. This will launch the gateway with all normal parameters but will swap the
exchange communication adapter with a mocked adapter.

