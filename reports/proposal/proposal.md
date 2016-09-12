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

The maintenance of the environment within a building such as a home or a school can often be a burden
on homeowners and maintenance staff. Controlling temperatures and lighting, for instance, is often a 
repetitive task which would be convenient to automate.

This report contains a proposal for a project to eliminate such tasks. The objective of the project
is to build a system to automate control of a building's environment which uses machine learning 
algorithms to minimize manual configuration. The proposal presents several motivations for using 
the environmental control system, as well as a detailed description of the project's objectives.
The proposal also includes a timeline for the completion of concrete milestones for the project 
as well as a technical summary of the proposed solution.

People spend a large amount of time in their homes, so any task in a home that becomes
automated saves the building owner a substantial amount of effort. This is particularly important 
in the case where someone has physical limitations preventing them from independently maintaining their
house. A system which controls the living environment without requiring substantial configuration
can give these people more independence, or allow their caregivers to focus on other priorities.

There is also a place for automated environment control in a commercial setting. An example of
this is in education buildings, where there are hundreds, if not thousands, of people in many 
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

Supervised machine learning traditionally requires massive data sets with a map of inputs to
expected outputs. It then requires tuning, either automated or manual to achieve a desired level
of correctness. This process is tedious and massively time consuming.

The downside of existing automated environment systems is the amount of configuration required to
have the system meet your specific needs. By having the system learn the habits of the user
dynamically, the configuration is essentially eliminated, leading to an ease of installation that
does not currently exist.

Supervised learning also requires massive amounts of computation and data storage. One goal of
this system is to have records and learn sessions with live input and interactions from users in
a physical environment. This data will be mapped to the machine learning algorithm and then mapped
back to the physical domain.

## Objectives

Currently, supervised learning algorithms require a complete input dataset and a meticulously
configured output to train the system. We want to have the algorithm be trained in a real world
environment where users perform live actions and the system determines relevant changes and
environmental factors. This automated learning system will be generic and use only the categorical
and numerical information provided by sensors and actuators.

Manual adjustment of a home's environment can be tedious. A goal of the project will be to use the
automated learning system to create a system that can be installed in the home to automatically
adjust the home environment based on input from a number of sensors. The system should support
simple configuration of any type of sensor; the system should not contain detailed knowledge about
any sensors and actuators.

This system will have dynamically updatable configuration of sensors and actuators. This will have
minimal overhead for adding and remove new devices from the system. The smart algorithm will then 
adjust to take these new devices into account when performing its computations.

## Technical Overview

This project consists of several smaller components that will be described in more detail in this
section. These components do not necessarily run on the same computer or even in the same process.
This is a list of the high level major technical components that will drive this system.

#### Machine Learning Algorithm

The machine learning algorithm will accept tables of categorical and numerical data and produce sets
of decisions based on historical events. The implementation of this algorithm will be configurable and
tunable for optimal output.

#### Training Method

The server will be trained using a watch and learn method. A user will train the system
by using a web interface or manual controls. The user will enter the desired action they would like the building
to perform at a certain time. The server will then store the current sensor information and the desired state.
The server will have the following three modes: record and learn, assisted and live mode. 

In record and learn mode, the server makes no decisions on its own. It records the users interactions with the 
system and logs them in a database. It then will use these decisions to make future estimations about
desired behaviour.

Assisted mode allows the server to make decisions, but will continue to receive user direction about expected 
behaviour. The system will record all user interactions, using them for behaviour prediction. This will be
the same as record and learn mode, except the system will make its own decisions. If the system makes a decision
that a user does not agree with, the user can reject the decision.

Under live mode, the system will make all decisions based on its historically recorded inputs. The system
will no longer allow the user to reject a behaviour. 

#### Central Control Server

This server will encompass the machine learning algorithm as well as database management for logging
device inputs and control events. These event will also be stored with historical expected outputs
so that they can be used for future decisions. The central server will also be responsible for
communicating to the communication service.

#### Communication Service

The communication service is the central node for all communications in the network. It is responsible for
forwarding all messages to all participants in the system. It is the only component that will communicate
directly to the central server. All devices will communicate to this server using a special protocol that
will be design for this system

#### Devices

To interact with the physical world, different embedded devices will be used in the system. These
devices will use sensors and actuators to record different properties and interact with their environment.
The devices will use a discovery protocol to automatically add themselves to the network. This will make
configuration very simple and dynamic. Devices announce themselves with categorical information about the
device such that a user will know to accept them. Once the device is connected, it will be added to the
machine learning server and be logged and controlled with other devices.

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

| ID   | Milestone                                 | Date                   |
| ---- | ----------------------------------------- | ---------------------- |
| 1    | Machine Leaning Server Prototype          | September 25th, 2016   |
| 2    | Communicating Protocol and Service        | October 16th, 2016     |
| 3    | Sensor Communication and Discovery        | November 6th, 2016     |
| 4    | Sensors and Actuators; Inputs and Control | November 6th, 2016     |
| 5    | Gateway and Web Client                    | January 29th, 2017     |
| 6    | Remote Record and Learn                   | February 12th, 2017    |

### Milestones

#### 1. Machine Learning Server Prototype

This will include the central server as well as the machine learning algorithm. This will
use sample data for inputs and output. All learning will be simulated for tuning and testing.

#### 2. Communication Protocol and Service

By the end of the milestone the protocol will be defined and the communication service 
will be running using simulated data. The service will only be communicating with the
machine learning server at this time.

#### 3. Sensor Communication and Discovery

Sensor communication will all be routed through the communication service. This will use the
communication protocol from the previous milestone. To aid in usability, when a new device is
added to the network, it will follow a discovery protocol to add itself to the machine learning
server's system. The discovery protocol and implementation will be completed in this milestone.

#### 4. Sensors and Actuators; Inputs and Control

During the development of milestone 3, sensor reading and actuator control will be programmed.
This can be done concurrently with the development of the communication of the sensors themselves.
Data values will be read from sensors while control signals will need to be sent to actuators.
The system must log both data values and control values so they can be used to learn the patterns
of a user and apply them to the system

#### 5. Gateway and Web Client

The system will have a user interface for a high level user remote control. This remote will be
controlled by a web client. This client will be served through a simple web gateway that will
provide a simple REST API for interacting to the communication service.

#### 6. Remote Record and Learn

By the end of the milestone, the three modes will be added to the machine learining server. 
The server will also use training data from a recording session instead of simulated data.

## Required Facilities

This project will require access to a variety of sensors and actuators which can be manipulated 
using a microcontroller such as an Arduino or Raspberry Pi.


