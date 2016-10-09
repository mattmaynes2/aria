# 6. Custom-Built Devices

6.1 Background
--------------

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

#### Compatibility with computing devices and communication protocols

What communication protocols can be supported by the device? How does it interact with a processor?

#### Ease of use

The principle objective of the product is to simplify configuration of home automation systems. Devices
which require complex setup are contrary to the system's objectives. 


### Devices of Interest

This section contains a list of device types which were investigated, and a short explanation of why 
the devices could showcase the machine learning capabilities of the system. In general, we believe that 
in order to showcase the machine learning capabilities of the system, it will be important to 
include a wide range of sensors, as well as actuators whose desired states may be influenced by several 
unrelated sensors. By providing such a range of devices, we hope to demonstrate that the machine
learning algorithm is capable of identifying more complex interactions between devices than a 
simple "If this then that" relationship.

In addition to providing a varied range of sensors, we would like to provide several sensors and 
actuators with non-binary inputs and outputs. The interactions between such devices may be more
complex than for binary devices due to the increased number of possible states.

With the goal of providing a range of actuators which are potentially related to multiple different
sensors, as well as devices with non-binary inputs and outputs, we have investigated the following
devices:

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

A dimmer switch is an example of a non-binary output device. 

- Alarm Clock

- Energy monitoring switch

- Coloured Lighting

- Coffee Makers

6.2 Motion Sensor
-----------------

### Description

### Technical Overview

This section considers devices that can be used to alert the system when a person
enters or leaves an area of the home. 

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

PIR sensors are easy to use, the main difficulties that a user may encounter in setting up a 
PIR sensor are ensuring that the detectorès field of view covers the correct area, as well 
as potentially adjusting the sensitivity of the detector.

PIR sensors are available with a range which is suitable for a typical room (approximately 7m range).


The following tutorials explain how to interface with PIR modules:

[https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf]
[https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/]

Relation to research objectives

- Low level of hardware expertise required
- Reliable
- Widely Available
- Estimated time investment is under 10 hours

#### Doppler-Effect based sensors

Several types of motion detectors use the Doppler effect to detect motion. The detector transmits
A signal of a known frequency. This signal is reflected by any objects in its path and 
detected when it returns to the sensor. The sensor tracks frequency of the reflected wave; when
a wave is reflected off of a moving object the frequency of the reflected wave differs from that 
of the incident wave due to the Doppler effect. This change in frequency is detected by the 
sensor and registered as motion. 

#### Infrared Break-Beam 

An infrared break-beam sensor consists of two physical modules separated by some distance. 
One side of the detector transmits a beam of infrared light which is detected by the other
side. 

Expertise Required 
- Little expertise required, circuits are simple 
- Tutorials widely available online

INSERT CIRCUIT DIAGRAM

Time Investment
- Comparable to light switch; the software and hardware complexity is low

Component Availability
- Components widely available

Reliability
- Sensors generally have a lower range than PIR sensors, availability of detectors with a longer
range may be lower
- Allows for finer control over the area of detection than a PIR sensor

Useability
- More difficult than a PIR sensor, requires the user to precisely aim the transmitted beam.

### Evaluation

How does this specific item do against our criteria?

-----------------------

6.3 Dimmer Switch
------------------

The objective of thios device is to allow precise control of the amount of AC power given 
to a device such as a light bulb or a fan. 

Expertise Required

- Safety concerns: A dimmer switch is likely to be used with devices that plugin in to 
wall outlets. Therefore, building this device may involve the use of high voltages which
should not be undertaken without the proper training. For this reason alone, the dimmer
switch may not be a good candidate for a custom-built device.


Time Investment

- Circuits presented in mopst online tutorials are much more complex than the simple 
light switch circuit. This would lead to a higher amount of time investment required
to understand and construct the circuit.

6.4 Light Sensor
----------------

### Description

This section investigates devices which can detect the amount of ambient light in an
area of the house.

#### Photoresistors

Light sensors generally make use of a component called a photoresistor. The resistance
of a photoresistor differs depending on the amount of light incident to the component.
Phtoresistors are also called photocells.

##### Reliability Characteristics

- Photoresistors are unsuitable for precise lighting measurements because its resistance
may vary due to temperature as well as light

- Photoresistor may exhibit latency (delay between a change in light and a change in resistance)

#### Photodiode 

Photodiodes are components which can be used similarly to photoresistors to detect light.
A photodiode allows electrons to pass when there is light shining on it. The current
allowed to pass is proportional to the amount of light incident on the device.

Unlike photoresistors, a photodiode is not sensitive to temperature changes and may allow
for more accurate light detection. The circuit required to interface with a photodiode is
of similar complexity to the circuit required to interface with a photoresistor.

### Expertise Required

INSERT CIRCUIT DIAGRAM

##### Time Investment Required

Due to the simplicity of the photoresistor circuit and the wide availability of the 
required components and tutorials, a custom-built light sensor is expected to require
less than 5 hours to build.

[http://www.resistorguide.com/photoresistor/]

6.5 Alarm Clock
---------------

6.6 Energy Monitoring Switch
----------------------------

6.7 Coloured Lighting
---------------------

6.8 Coffee Makers
-----------------


6.9 Summary of Evaluation
-------------------------

All of the evaluation grouped together

6.10 Conclusion
---------------

What did we decide upon? Why?
