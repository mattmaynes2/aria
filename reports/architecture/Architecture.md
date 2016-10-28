Architecture
===========

## Introduction


## Components

![](./SystemComponents.png)

### Event Logger

The event logger is responsible for listening to all event signals and record them in a central
database. This data will be accessible by the remote client as well as the ML algorithm component.
The events recorded will be used to make decisions about actions to carry out. The event logger
will consume the event interface that is provided by the communication server and will simply
observe all data.

### Event Interface

The event interface is the protocol that will be used to send event within the smart learning
system. This interface will define the structure of data that will be sent from smart devices to
the communication server as well as any other listening parties. Events that are sent from third
party devices will use a different protocol to communication to the central hub. This protocol is
designed for custom built devices. Events that are sent using this interface will have the
following message protocol.

#### Message Protocol

Messages have to be sent between all components in the smart home system. The smart home system
uses UDP to send messages. The following is a proposal for an encoding structure for all messages
sent in the system. It is assumed that all data in the payload field is JSON encoded unless the
message type indicates otherwise.

##### General Message Structure

```
+--------+---------+----------+-------------+--------------+
|  type  |   size  |  sender  | destination |   payload    |
+--------+---------+----------+-------------+--------------+
| 1 byte | 4 bytes | 16 bytes |  16 bytes   | 'size' bytes |
+--------+---------+----------+-------------+--------------+
```

##### Message Types

| Name        | Type  | Value       |
| -----       | ----- | ----------- |
| Error       | ERR   | 0x01        |
| Request     | REQ   | 0x02        |
| Event       | EVT   | 0x03        |

### ML Algorithm

This algorithm is responsible for reading events, generating a model of interactions and then
making decisions about actions to perform. The implementation of this algorithm can be customized
as long as it provides the decision interface. The ML algorithm will receive data from the
event logger using snapshots of data. These data snapshots will reduce the amount of information
that the ML algorithm needs to process by removing redundant information.

### Decision Interface

The decision interface allows the ML algorithm to enter commands into the communication server
which will be translated into events for the system. This interface must be provided by the ML
algorithm and will be consumed by the communication server.

### Snapshot Interface

This interface allows the ML algorithm to receive a subset of the data from the event logger.
The snapshots remove any duplicate information before sending it to the ML algorithm for
processing. This reduces the amount of data that needs to be sent as well as the amount of data
that needs to be processed by the algorithm.

### Communication Server

The communication server is responsible for routing all messages through the smart home system.
The server has a cache of all connected devices and must store any related settings for each.
Events and messages are routed through the communication server using the event interface. The
communication server is also responsible for sending messages to other third party protocols.
The server should provide a mechanism for installing plugins for other third party devices that
are not natively supported.

### HTTP Gateway

The HTTP gateway is responsible for supporting the web client interface. It must serve the web
client's requests over a REST interface and translate them to the internal event interface used
by the communication server. The gateway must be able to support multiple web clients.

### REST Interface

The REST interface allows web communication from web clients to the HTTP gateway. This
representational state transfer protocol must allow the web client to carry out interactions
with the various devices connected in the system as well as view the current system state. This
interface must provide both a monitoring and controlling the system.

### Device Communication

Device Communication is responsible for passing events between the device and 
the Communication Server. The Device Communication consumes the Device Control, Sensor Interface
and the Event Interface.

### Sensor Interface

This interface allows the Device Communication to read events from sensors and 
pass them on to the communication server. This interface is provided by the
Sensor Reader and consumed by the Device Communication.

### Sensor Reader

The Sensor Reader is responsible for listening to a sensor and providing 
events when sensor data changes. The Sensor Reader will provide the Sensor Interface.

### Device Controller

The Device Controller is responsible for controlling the physical device. It consumes events
and modifies the output of the device accordingly. The Device Controller provides the Device 
Control Interface.

### Device Control

This interface allows the device communication to pass events to the Device controller.


## Deployment

![](./SystemDeployment.png)

### Smart Hub

The central point of control of this smart home system is the smart hub. This hub is the central
point of communication for all devices in the smart home system. It houses all of the data
storage for events in the system and makes decisions using a smart learning algorithm. The hub
will provide a minimal hardware interface for starting the system and changing the system state
from training to normal to standby. The smart hub needs to be connected to a internet access
point in order for it to serve the web interface to a client's computing device.

### Smart Device

In this diagram, smart device refers to any smart device in the system. This could be a custom
built device or a third party device. There will be many of these devices within the system all
communicating to the central smart hub.

### Web Client

The web client is the end user's browser and will present a remote interface for controlling the
smart hub as well as all devices that are connected to the system. The web interface must be able
to render on various industry standard browsers (Chrome, Firefox, IE, Safari).



## Database Entity-Relationship

![](./SystemER.png)

### Devices

The individual devices connected to the system

### Device_Types 

The different types of possible devices, (WeMo switch,,Hue lights, etc...)


### User

A person that can add and control devices

### User_Devices

The devices a user has access to

### Event

A snapshot of a device state at a certain time

