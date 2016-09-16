Machine Learning Smart Building
===============================

Supervisor: Babak Esfandiari

| Name              | Student Number | Email                              |
| ----              | -------------- | -----                              |
| Matthew Maynes    | 100882216      | mattmaynes@cmail.carleton.ca       |
| Cameron Blanchard | 100886476      | cameronblanchard@cmail.carleton.ca |
| Jeremy Dunsmore   | 100889935      | jeremydunsmore@cmail.carleton.ca   |
| Peter Mark        | 100886038      | petermark@cmail.carleton.ca        |

## Introduction

Maintaining a comfortable environment within a building such as a home or a school can often be a burden
on homeowners and maintenance staff. Adjustment of the temperature and lighting in a room, for instance, 
is often a repetitive task which it would be convenient to automate.

This report contains a proposal for a project to eliminate these manual tasks. The objective of the project
is to build a system to automate control of a building's environment, which uses machine learning 
algorithms to minimize manual configuration. The proposal presents several motivations for using 
the environmental control system, as well as a detailed description of the project's objectives.
The proposal also includes a timeline for the completion of concrete milestones for the project 
as well as a technical summary of the proposed solution.

## Background

Any home maintenance task which can be automated can save the owner a substantial amount of time and money.
Automated environmental control is not a novel concept; devices such as light timers and programmable 
thermostats have existed for many years. Most of these common devices, however, must be configured 
manually. The system proposed in this report is able to configure itself based on normal actions taken
by the user. By having the system learn the habits of the user dynamically, the configuration is essentially 
eliminated, leading to an ease of installation that does not currently exist.

One scenario in which a home automation system could be a significant help is in the case of 
a homeowner with physical limitations that prevent them from independently maintaining their
house. A system which controls the living environment without requiring substantial configuration
can give these people more independence, or allow their caregivers to focus on other priorities.

There is also a place for automated environment control in a commercial setting. An example of
this is in educational buildings, where there are thousands of people in many 
different rooms at all times of day. Maintaining a single building in this situation requires
full time staff. For example, during a lecture at sunset, an instructor may have to adjust the blinds
and contact the maintenance staff to adjust the temperature at the same time each day. The cost and 
effort of this maintenance is multiplied for every building in a given institution. If a system could
be installed in each building that learns to handle this activity automatically, it would help reduce 
the burden and cost of maintenance.

Another benefit of automated environment control is improved energy efficiency. It is not uncommon
to leave a room forgetting to turn off a light, or to leave a building with the air conditioning still
running. This leads to needless consumption of energy, again increasing the cost of maintaining the 
building. Removing this responsibility from the building owner also removes this waste of energy.
An automated environment control can also improve energy efficiency beyond just removing negligence.
Once the desired temperature of a room for a given time is known, options besides air conditioning
or heating can be explored first. If the room temperature must be raised, and the temperature outside
is warm enough, the system could open the room windows. Once the desired temperature has been reached, 
the windows could be automatically shut again.

## Objectives

Currently, supervised learning algorithms require a complete input dataset and a meticulously
configured output to train the system. We want to have the algorithm be trained in a real world
environment where users perform live actions and the system determines relevant changes and
environmental factors. This automated learning system will be generic and use only the categorical
and numerical information provided by sensors and actuators.

Manual adjustment of a building's environment can be tedious. A goal of the project will be to create 
a system which uses automated learning to adjust the environment based on input from a number of sensors. 
The system should support simple configuration of any type of sensor, and should not contain detailed 
knowledge about any sensors or actuators.

This system will support dynamic updates to the configuration of sensors and actuators. Overhead for adding 
and removing new devices from the system will be minimal. The learning algorithm will then adjust to take these
new devices into account when altering or maintaining the environment.

## Technical Overview

This project consists of several smaller components that will be described in more detail in this
section. The following is a list of the high level technical components of the system.

#### Machine Learning Algorithm

The machine learning algorithm will accept tables of categorical and numerical data which will be
used to produce sets of decisions based on historical events. The implementation of this algorithm 
will be configurable and tunable for optimal output.

#### Training Method

The server will be trained using a watch and learn method. A user will train the system
by using a web interface or manual controls. The user will enter the desired action, and
the server will associate the current sensor information with the desired state. The server
will have the following two modes: record and learn and assisted. 

In record and learn mode, the server makes no decisions on its own. It records the user's interactions with the 
system and logs them in a database. It will then use this information to make future estimations about
desired behaviour.

Assisted mode allows the server to make decisions, but will continue to receive user direction about expected 
behaviour. The system will record all user interactions, using them for behaviour prediction. The system
makes its own decisions, while still accepting feedback from the user.


#### Central Control Server

This server will contain the machine learning algorithm as well as database management for logging
device inputs and control events. These events will also be stored with the expected outputs
so that they can be used for future decisions. The central server will also be responsible for
communicating to the communication service.

#### Communication Service

The communication service is the central node for all communications in the network. It is responsible for
forwarding all messages to the appropriate devices in the system. It is the only component that will communicate
directly with the central server. All devices will communicate with the communication service using a special 
protocol that will be designed for this system.

#### Devices

To interact with the physical world, different embedded devices will be used in the system. These
devices will use sensors and actuators to record different properties and interact with their environment.
The devices will use a discovery protocol to automatically add themselves to the network. This will make
configuration simple and dynamic. Once the device is connected, it will be added to the machine learning 
server and be logged and controlled with the other devices.

#### HTTP Gateway

The gateway is a thin HTTP wrapper around the communication interface's API and acts as a bridge
between the web client and the core services. The gateway will serve the web pages for the web client
and provide a RESTful API for interacting with the communication protocol.

#### Web Interface

The web interface provides direct user interaction through a graphical user interface. This
interface will communicate through the HTTP gateway using a RESTful API. The web client will
provide remote control capabilities, allow for device simulation, and provide overall information
monitoring.

## Schedule

| Milestone  | Date                |
| :--------: | ----------------    |
| 1          | October 9th, 2016   |
| 2          | November 13th, 2016 |
| 3          | January  8th, 2016  |
| 4          | February 19th, 2016 |


### Milestones

#### Milestone 1

This iteration will contain the minimal viable product for the smart building system. This iteration
will contain a basic regression algorithm acting as the machine learning system. The system's central
communication service will be operational as well as a database storage system. This initial system
will use simulated devices to model data and interactions within the system.

#### Milestone 2 

This iteration will add the web interface that allows a user to control the system.
The simulated devices from the previous milestone will be replaced with 2 real devices
a temperature sensor and a thermostate controller.

#### 3. Sensor Communication and Discovery

Sensor communication will all be routed through the communication service. This will use the
communication protocol from the previous milestone. To aid in usability, when a new device is
added to the network, it will follow a discovery protocol to add itself to the machine learning
server's system. The discovery protocol and implementation will be completed in this milestone.

#### Milestone 4

This iteration will focus on improving the complete system developed in the first three iterations.
We will add a motion sensor and a light control in order to test the system with multiple types
of devices. Another goal of this iteration will be to improve the basic machine learning algorithm
which is used for the first three iterations.

## Required Facilities

This project will require access to a variety of sensors and actuators which can be manipulated 
using a microcontroller such as an Arduino or Raspberry Pi.


