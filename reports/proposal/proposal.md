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

## Scenarios

In order to create concrete goals for the project, we have identified a collection of scenarios. Each
scenario describes a common situation which occurs in a home's environment, and how the home
automation system should respond.

### Light Automation

Nearly every room contains several lights which need to be adjusted regularly in response to
various stimuli. It is very common for occupants to forget to turn off lights when they are
not in use, leading to and unnecessary waste of money and energy. In order to save money and
energy, the home automation system should be capable of automating the following tasks:

* Turn on lights at a given time
* Turn off lights at a given time
* Turn on lights when dark outside
* Turn off lights when light outside

### Curtain Automation

### Temperature Automation

## Schedule

The project has been broken down into several week long iterations. The focus of each iteration 
is to introduce a useful (demoable) feature to the system. By breaking the project into 
demoable iterations, we will be able to commit to a set of concrete goals on a weekly basis. 
The emphasis on demoable increments will allow us to have a product that always in a working state.
Iterations have been grouped into larger milestones; each milestone marks the implementation of 
one of the scenarios described in the previous section.

### Iteration 1
> October 5, 2016

- Arduino micro-controller hooked up to a voltage relay
- Relay hooked up to a single light switch
- A single button to toggle the state of the light

### Iteration 2
> October 12, 2016

- Light sensor reading values
- Arduinos communicating to central server

### Iteration 3
> October 19, 2016

- Light sensor communication to light controller

#### Milestone: Automated Lighting Control

### Iteration 4
> October 26, 2016

- Arduino motor that moves a curtain track
- Button that control Arduino motor

### Iteration 5
> November 2, 2016

- Add communication to curtain Arduino

##### Milestone: Automated Curtain Control

### Iteration 6
> November 9, 2016

- Web API

### Iteration 7
> November 16, 2016

- Static functioning web interface

#### Milestone: Functional Web Interface

### Iteration 8
> November 23, 2016

- Add temperature control buttons
- Add temperature LED display

### Iteration 9
> November 30, 2016

- Add temperature device communication

#### Milestone: Automated Temperature Control

### Iteration 10
> December 7, 2016

- Add basic decision making software

### Iteration 11
> January 4, 2017

- Add device discovery

#### Milestone: Automated Configuration

### Iteration 12
> January 11, 2017

- Improved web client

### Iteration 13
> January 18, 2107

- Improved decision making

### Iteration 14
> January 25, 2017

- Add record and learn

##### Milestone: Complete System

## Team Responsibilites

Responsibilites will change on an iteration by iteration basis. Each team member will
rotate and contribute to different elements of the system. This will allow each member
on the team to have a good understanding of the entire system.

## Required Facilities

### 4 Arduinos

These will be used for interfacing with senosrs and controlling motors. Two different devices were
considered for this role; an Arduino and a Raspberry Pi. The size of an Arduino is much smaller than
a Raspberry Pi and therefore more applicable to the embedded device use case. Working with hardware
from a Rasperry Pi requires more accessories than an Arduino and is therefore more difficult to setup
than an Arduino.

### Sensors

- Photo Transistor Light Sensor
- Digital Temperature Sensor

### Output Devices

- Standard 16x2 LCD
- AC voltage relay

### Control Devices

- (10) Buttons


