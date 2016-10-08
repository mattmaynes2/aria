Section Title
=============

### Background

The purpose of this section is to present our investigation into the process of building various types
of smart devices which might be of use for home automation. The purpose of this investigation is to provide 
information that the team can use to decide which devices will be included in the system to showcase 
its machine learning capabilities. In particular, this section will examine the feasibility of 
assembling such devices from basic electronic components, rather than purchasing a complete off-the-shelf
system.

In this section, a **smart device** refers to a sensor or actuator which can be controlled over a 
wireless network. The process of building a smart device is expected to consist of interfacing 
a basic hardware module with a microcontroller which is capable of controlling the device and 
communicating over a network.

The research will focus determining several characteristics:

#### Expertise required

The team consists solely of software engineering students. Some complex devices will be impractical
for the team to build due to the lack of hardware knowledge available on the team. Factors which 
will be considered in the evaluation of the devices include the availability of tutorials and 
development kits. Safety will also be a critical factor (Does the team have the facilities and 
expertise necessary to build the device safely).

#### Time Investment

The project has a fixed deadline; in order to allow the team to focus on the machine learning aspects
of the system, devices which can be used to demonstrate the system must be available quickly. For each 
device, an estimate of the time investment required to build the devices will be an important factor
in the decision of whether to use a commercially available alternative or not. When possible, an
estimate of the number of hours required should be sought out.

#### Component Availability

Due to the time constraints of the project, it may be infeasible to build a device for which components
are not readily available.

#### Reliability

The system is only useful if its decisions are observable through the devices which are connected to it. 
Therefore, we must be abale to trust that any custom devices are highly reliable.

- Compatibility with computing devices and communication protocols

What communication protocols can be supported by the device? How does it interact with a processor?

- Ease of use

The principle objective of the product is to simplify configuration of home automation systems. Devices
which require complex setup are cointrary to the system's objectives. 


### Devices of Interest

This section contains a list of device types which were investigated, and a short explanation of why 
the devices could showcase the machine learning capabilities of the system.

- Motion Sensors

Many actions could be triggered by aa person entering or leaving a house or a room. A motion sensor could
potentially interact with every other device on this list. Due to the wide range of potential interactions,
we expect that a motion sensor will be a good test of the machine learning component's ability to 
determine the relationships inputs and outputs. The motion sensor could also reveal flaws in the 
machine laerning algorithm. For example, the machine learning algorithm may determine that when a motion
sensor is triggered outside a homeowner's bedroom, the coffee machine should be turned on. However, this 
behaviour would only be desired during certain hours of the day (the coffee machine should not turn on
when the homeowner goes to bed, for example). It is likely that there are many such scenarios that we 
haven't thought of which would present challenging cases for the machine learning component to handle.

- Range Sensors

- Thermostat

- Digital Locks

Digital locks are of interest because correct control of locks is a concern of homeowners. While their 
output is binary (locked/unlocked), their behaviour is potentially affected by many factors
 (lighting levels, time of day, motion sensors, etc.), which could be challenging for the machine
 learning algorithm to infer.

- Light Sensor

A light sensor provides a non-binary input to the machine learning component. Similar to a motion sensor,
the level of light in a room may be related to the behaviour of many other devices.

- Dimmer switch

A dimmer switch is a nexample of a non-binary output device. 

- Alarm Clock

- Energy monitoring switch

- Coloured Lighting

- Coffee Makers

Motion Sensor
------------

## Description

## Technical Overview

### Sensor Technologies

This section provides a comparison of several different sensor technologies that are commonly used in
motion detection.

#### Passive Infrared (PIR)

A passive infrared sensor detects motion using the infrared radiation (heat) from a
warm body. A sensor contains two slots, each of which contains a material which is 
sensitive to infrared radiation. As a warm body passes in front of the sensor, a 
different amount of radiation is received at each slot. This difference in radiation
causes a signal in the output of the device.

Use of the PIR modules encountered during this research does not require expert knowledge of circuit 
design; the complexity of the circuits involved in connecting the modules to a microcontroller is 
comparable to that of a simple LED circuit. A power source and a resistor is sufficient to get the
module up and running.

Most PIR modules have 3 pins to connect to a circuit. One pin connects to ground, another to power, 
andthe third pin is used for output. The output consists of a single digital signal indicating 
when motion is detected. 

Tutorials describing how to connect PIR modules to common microcontrollers, such as a Raspberry Pi
or Arduino are widely available online. 

The complexity of the circuit required to interface with a PIR module is comparable to the light 
switch circuit, consisting of a single push button used to toggle an LED. Therefore, development 
time required for the complete device is expected to be under 10 hours.

PIR sensor modules are reliable because they do not typically contain any moving components, 
other than potentiometer used for sensitivity adjustment. 

The following tutorials explain how to interface with PIR modules:

[https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf]
[https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/]

Relation to research objectives

- Low level of hardware expertise required
- Reliable
- Widely Available
- Estimated time investment is under 10 hours

#### Microwave



#### Vibration

#### Ultrasonic

#### Reflective Infrared

## Evaluation

How does this specific item do against our criteria?

-----------------------


### Summary of Evaluation

All of the evaluation grouped together

### Conclusion

What did we decide upon? Why?
