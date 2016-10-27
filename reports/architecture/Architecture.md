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

### HTTP Gateway

### REST Interface

### Device Communication

### Sensor Interface

This interface allows the Device Communication to read events from sensors and 
pass them on to the communication server. This interface is provided by the
Sensor Reader and consumed by the Device Communication.

### Sensor Reader

The Sensor Reader is responsible for listening to a sensor and providing 
events when sensor data changes. The Sensor Reader will provide the Sensor Interface.

### Device Controller

### Device Control

## Deployment

![](./SystemDeployment.png)

### Smart Hub

### Smart Device

### Web Client

