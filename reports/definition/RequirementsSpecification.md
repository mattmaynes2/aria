# Requirements Specification for Learning Home Automation System

## 1. Introduction


### 1.1 Introduction

The Smart Learning system is a learning home automation system. The system will allow a home
owner to set up a collection of devices in their home to automatically control their environment
and automate common tasks. Task automation in the system will not require any user configuration,
instead tasks will be automated based on the user's interaction with devices in the system.

The system will consist of a hub device with a simple interface that a homeowner can connect to 
a home network. After connecting the hub, the homeowner can add enabled devices for the system to
control by simply connecting them to the network. As new devices are connected, their input
will be used to make more predictive decisions about user behaviour.

### 1.2 Product Scope

The purpose of the learning home automation system is to make home automation as easy as possible
to set up. Many existing home automation systems require some form of programming from the user,
in the form of a schedule or explicit scenarios which describe how their devices should behave. This
project will improve upon such systems by inferring the desired state of devices from data collected
during the homeowner's routine use of the devices.

Activities which are "In Scope":

- Provide a range of devices that can be installed in a home which showcase the learning capabilities
  of the system 
 
- Create a hub device that collects data from installed sensors, and uses this data to infer the 
  desired values of actuators. The hub must provide a simple interface which allows the homeowner
  to toggle on/off automated control of devices.

- Develop a protocol which allows developers to enable new types of devices for use in the system

## 2. Overall Description

### 2.1 Product Perspective

Smart home systems are becoming more readily available in the general market place. This system
builds upon traditional home automation systems by adding true automation in the form of learning.
Unlike traditional smart home systems, the Smart Learning system observes user interaction and
automatically makes decisions based on historical behaviours. By combining the fields of machine
learning and home automation, the smart learning system will provide an end user with a more
customized smart home experience.

**INSERT DIAGRAM OF SYSTEM**

### 2.2 Product Functions

To provide simplicity and seamless interaction, the smart learning system must be easy to use
and highly interactive. The smart learning system will provide a central hub that will be the
base of computation and communication for all other components in the system.

The system will have many different smart devices. These devices can either be used for control
or for a task. To allow for expansion of the automation system, it must be able to accept new
devices. The system must then retain its previous model of the user's interactions but add in
the new device as evidence for predicting future behaviours. For example, a system might include
a light sensor, thermostat and curtain puller. If the ambient light outside was to drop and the
user closed the curtains then the system might predict that a change in light corresponds to that
action. If the user then changes the temperature, the system may relate light to temperature as
well. If later a temperature sensor was added to the system and the user changes the temperature
when it is too cold, the system will use this information to predict future actions.

To be able to monitor and control the smart home system, the smart hub must be controllable using
a graphical interface. This interface will likely be provided in the form of a web interface and
allow the user to view the state of the system and manually control any connected device. This
interface can be used for manually configuring desired behaviours as well as for enabling the
training mode of the system. The interface must allow the user to view the state of all devices
in the system as well as view their recorded interactions.

### 2.3 User Classes

While this primary audience of the smart learning system is a home owner, it is also for building
owners, nursing home residence or anyone who needs building automation. The end user of this
product is intended to be non-technical users who want simple control and access of their building.
This product will also provide utilities for more technically proficient users who wish to create
their own devices that communicate to the system.

#### Base User (Non-Technical Users)

- End user of the system that needs simple interface to use system
- Will want low maintenance to keep system running and expect system to perform correctly

#### Developers (Technical Users)

- Will require technical documentation about the system
- Will require set development toolkit for creating custom devices for the system
- May also be a base user

### 2.4 Design and Implementation Constraints



### 2.5 Assumptions and Dependencies

## 3. External Interface Requirements

### 3.1 User Interfaces

### 3.2 Hardware Interfaces

### 3.3 Software Interfaces

### 3.4 Communications Interfaces

## 4. System Features

![image](./SystemUseCase.png)

-----------------------------

#### Install Hub

Installation of the central hub simply requires a connection to a home network.

1. User plugs hub into outlet and turns power on
2. User connects hub to home network using Ethernet
3. Hub provides confirmation that system is online

#### Add Device

Devices can be added to the home automation system simply by powering them on and connecting
to the smart learning network.

1. User plugs in device and turns power on
2. Device discovers network
3. Hub discovers device and provides confirmation

#### Remove device

Devices will stop recording when removed from the smart learning network. To remove the history
of the device, the user can delete it using the remote interface.

1. User removes device from smart network
2. User uses remote interface to delete device history

#### Reset Device

If the input of a device is causing unexpected or undesired output then it can be reset by the
user through the remote interface.

1. User uses remote interface to delete device history

#### Training Mode

To train the system, the user must enter training mode. Training mode puts the system into a state
that observes the users interactions but does not control devices.

1. User enters training mode
2. User interacts with system and system records

#### Playback Mode

In playback mode, after the system has been trained, it can react to different inputs and make
decisions.

1. User enters playback mode
2. User interacts with system
3. System makes decisions based on historical data

#### Standby Mode

The system can be put in a state where it no longer observes user interaction and idles. This
still allows the user to manually control all devices through the system but the system will
not make any decisions.

1. User enters standby mode


## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements

#### Device Communication Range

Devices must be able to communicate wirelessly using the smart home network. The range of
communication must be sufficiently large that devices can be placed anywhere in an average home.
The smart home devices will need to be powerful enough to receive and transmit data using this
network with enough range.

**INSERT STATEMENT ABOUT DISTANCE**
- Need to discuss allowable range of different protocols
- Need to discuss average dimensions of a home


#### Discovery Time

For a device to be discovered by the smart home system it must first be connected to the smart
home network. The amount of time to connect to the network is an artifact of the protocol that
is chosen for the network. Once a device has connected to the network, it must then be discovered
by the smart home system. The amount of time required to establish this connection needs to be
minimal so that the user does is not concerned with the device operation. The well known **INSERT
STUDY HERE** study has discovered that the average human attention span is 8 seconds. To ensure
that the end user maintains focus on the system, the discovery protocol must be faster than 8
seconds. If this threshold is passed then the device should indicate that an error has occurred
during the discovery.

#### Frequency of Updates



#### Device Response Time

#### Hub Power Consumption

### 5.2 Security Requirements

#### Device Connection Security

#### Remote Interface Security

### 5.3 Quality Requirements

#### Hub Reliability

#### Device Reliability

#### Device Interoperability


