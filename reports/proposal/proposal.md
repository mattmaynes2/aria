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

The maintenance of the environment withing a building such as a home or a school can often be a burden
on homeowners and maintenance staff. Controlling temperatures and lighting, for instance, is often a 
repetitive task which would be convenient to automate.

This report contains a proposal for a project to eliminate such tasks. The objective of the project
is to build a system to automate control of a building's environment which uses machine learning 
algorithms to minimize manual configuration. The proposal presents several motivations for using 
the environmental control system, as well as a detailed description of the project's objectives.
The proposal also includes a timeline for the completion of concrete milestones for the project 
as well as a technical summary of the proposed solution.

## Motivation

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

People spend a large amount of time in their homes, so any task in a home that becomes
automated saves the building owner a substantial amount of effort. This is particularly important 
in case where someone has physical limitations preventing them from independently maintaining their
house.  A system which controls the living environment without requiring substantial configuration
can give these people more independence, or allow their caregivers to focus on other priorities.

There is a place for automated environment control in a commercial setting as well.  An example of
this is in education buildings, where there are hundreds, if not thousands, of people in many 
different rooms at all times of day.  Maintaining a single building in this situation requires
full time staff, as well as effort from the individuals in the rooms.  For example, a class
at sunset may have to adjust the blinds at the same time each day, while increasing the 
temperature of the room.  A system that tracks this activity and learns to handle it all automatically
would eliminate this issue.

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

The server prototype will include a machine learning algorithm. This algorithm will accept
arbitrary categorical and numerical data. The initial server will use simulated data with
pre-defined outputs for testing. This will be used to test the machine learning algorithm for
correctness. The server will also be responsible for database logging and mapping between input
and output domains.

Interfacing with the server will be done through a simple command line interface for this
milestone. Communication to other devices will be added in the next milestone but will be
considered in this one. This will ensure that there is the correct infrastructure for remotely
controlling the server.

#### 2. Communication Protocol and Service
The communication protocol will define a set of rules that allows devices to  interact with the machine learning server.

The communication service will run on top of  the machine learning server. It will pass messages between the machine learning server and the exterior devices.
#### 3. Sensor Communication and Discovery

Sensor communication will all be routed through the communication service. This will use the
communication protocol from the previous milestone. To aid in usability, when a new device is
added to the network it will follow a discovery protocol to add itself to the machine learning
server's system. The discovery protocol and implementation will be completed in this milestone.

#### 4. Sensors and Actuators; Inputs and Control



#### 5. Gateway and Web Client

#### 6.  Remote Record and Learn

## Required Facilities





