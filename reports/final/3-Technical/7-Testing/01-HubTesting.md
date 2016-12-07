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
