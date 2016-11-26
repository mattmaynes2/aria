### Testing DeviceCommunicatin, CommunicationServer, and EventLogger

#### Context

The DeviceCommunication, CommunicationServer, and EventLogger components form the core of the 
system's hub. Each of these components is written in Python, and work together to react to 
events from devices. and to fulfill requests from the HTTP Server.

Events from connected devices are first received by the DeviceCommunication
component, which forwards messages to the CommunicationServer component. CommunicationServer routes 
messages to the appropriate component, which may be another device HTTPGateway, or EventLogger. 
This section describes the unit testing of each component, as well the method used to test that 
the components perform correctly together.

### Unit Testing

The modules that make up each component are unit tested using Python's *unittest* framework. 
The unit tests are used for regression testing, and are written by the same person who implemented
the unit under test. 

The *unittest* framework makes use of Python's `decorator` construct to provide an easy way to 
isolate components for testing. Dependencies such as threading, database, and network libraries 
can be replaced with a mock obejcts automatically by declaring a test case with the
`@unittest.patch(<dependency-name>)` decorator.  
         
### Integration Testing

Various interactions between each of the components are triggered by the receipt of messages from
smart devices, as well as requests to the REST API.

Each component is driven by the receipt of event messages from devices.
 In order to perform such testing, we need to be
able to generate events from fake devices, and observe that the event logging component is 
behaving properly. 

The communication server makes use of an adapter pattern in order to communicate with different 
types of devices by adapting the interfaces that each type of device provides to a common interface.
This structure provides a simple way to simulate events for testing purposes; an adapter can be 
created which receives events from a software source. 

The suite of event logging integration tests currently makes use of python's *unittest* framework
to create test drivers. Unlike the suite of unit tests, the integration test suite does not mock
out dependencies on threads, database, etc. The *unittest* framework is simply used as a mechanism
to automate the setup and execution of integration tests.