## Testing {#section-testing}

This section describes how the system's components are tested. The section is organized by 
component; for a description of the purpose of each component, please see
[System Components](#section-design-components).

### Hub Testing {#section-test-hub}

#### Context {-}

The DeviceCommunication, CommunicationServer, and EventLogger components form the core of the 
system's hub. Each of these components is written in Python, and work together to react to 
events from devices. They are also responsible for fulfilling requests from the HTTP Server.

Events from connected devices are first received by the DeviceCommunication component, which 
forwards messages to the CommunicationServer component. CommunicationServer routes messages to the
appropriate component, which may be another device HTTPGateway or EventLogger. This section 
describes the unit testing of each component, as well the method used to test that the components 
perform correctly together.

#### Unit Testing {-}

The modules that make up each component are unit tested using Python's *unittest* framework. 
The unit tests are used for regression testing, and are written by the same person who implemented
the unit under test. 

The *unittest* framework makes use of Python's `decorator` construct to provide an easy way to 
isolate components for testing. Dependencies such as threading, database, and network libraries 
can be replaced with a mock obejcts automatically by declaring a test case with the
`@unittest.patch(<dependency-name>)` decorator. These mock objects are used as stubs to provide 
control the behaviour of the dependencies of a module. For example, mock objects are used to 
return test data when a module attempts to read data from a network socket.

#### Integration Testing {-}

Interactions between each of the components are triggered by the receipt of messages from
smart devices, as well as requests to the REST API. In order to make tests repeatable and to
minimize testing time, we chose to test the integration of these components using mock device data.
Using mock device test data also allows development of the components to proceed before the 
implementation of communication with physical devices is complete.

The DeviceCommunication component makes use of an adapter pattern to provide communication with 
different devices (which may have varying interfaces), through a common interface. This structure 
provides a simple way to simulate events for testing purposes; an adapter was created which 
generates events from software source. Automated tests enqueue various messages in the test adapter,
which are then propagated through the system as if they came from a physical device.

The choice of SQLite as a database engine makes the system easier to test. SQLite databases are
contained in a single file; this makes it inexpensive to tear down and re-create a database which
is used for testing. The simplicity of SQLite allows each test case to write to its own instance of 
the database. The advantage of having one database per test case is that any test failures 
can be debugged in isolation because the state of the database after a test faiure is preserved.

The suite of integration tests also makes use of python's *unittest* framework
to create test drivers. Unlike unit tests, the integration test suite does not mock
out dependencies such as threads, database, etc. The *unittest* framework is used only to automate
the execution of tests, so the behaviour of the components is as close as possible to their actual
behaviour when the entire system is running.

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

