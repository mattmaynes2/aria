### B-5 Custom-Built Devices {- #B-5}

#### Background {-}

The purpose of this section is to present our investigation into the process of building various
types of smart devices which might be of use for home automation. The purpose of this investigation
is to provide information that the team can use to decide which devices will be included in the
system to showcase its machine learning capabilities. In particular, this section will examine the
feasibility of assembling such devices from basic electronic components, rather than purchasing a
commercial device.

In this section, a **smart device** refers to a sensor or actuator which can be controlled over a
wireless network. The process of building a smart device is expected to consist of interfacing a
hardware module with a microcontroller which is capable of controlling the device and communicating
over a network.

Evaluation of custom devices will focus on the following characteristics:

##### Expertise required {-}

How difficult is it for a team of software engineering students to build the device?  Some complex
devices will be impractical for the team to build due to the lack of hardware knowledge.  Factors
which  will be considered in the evaluation of the devices include the availability of tutorials and
development kits. Safety will also be a critical factor (Does the team have the facilities and
expertise necessary to build the device safely).

##### Level of Effort {-}

In order to allow the team to focus on the machine learning aspects of the system, devices which can
be used to demonstrate the system must be available quickly. In order to measure this criteria, the
amount of effort required to build an LED controlled through a voltage relay will be used as a
baseline for estimation. The following scale will be used:

###### Low {-}

- Comparable to baseline (less than a day of work)

###### High {-}

- High effort (A couple days)

###### Extreme {-}

- Extreme effort (many days or weeks)

###### Quality Comparisons {-}

Commercially available devices may offer features which could be useful to demonstrate the system,
but are difficult to include in a custom-built device. It will be useful to determine whether or not
the devices described by most custom-build tutorials are fully featured. In some cases, the features
of a typical custom-built device will be compared against several commercial options.

##### Devices of Interest {-}

This section contains a list of device types which were investigated, and a short explanation of why
the devices could showcase the machine learning capabilities of the system. In general, we believe
that in order to showcase the machine learning capabilities of the system, it will be important to
include a wide range of sensors, as well as actuators whose desired states may be influenced by
several unrelated sensors. By providing such a range of devices, we hope to demonstrate that the
machine learning algorithm is capable of identifying more complex interactions between devices than
a simple IFTTT relationship.

In addition to providing a varied range of sensors, we would like to provide several sensors and
actuators with non-binary inputs and outputs. The interactions between such devices may be more
complex than for binary devices due to the increased number of possible states.

This section investigates some smart devices which are potentially within the team's ability to
build.

###### Motion Sensors {-}

Many actions could be triggered by a person entering or leaving a house or a room. A motion sensor
could potentially interact with every other device on this list. Due to the wide range of potential
interactions, we expect that a motion sensor will be a good test of the machine learning component's
ability to determine the relationships between inputs and outputs. The motion sensor could also
reveal flaws in the machine learning algorithm. For example, the machine learning algorithm may
determine that when a motion sensor is triggered outside a homeowner's bedroom, the coffee machine
should be turned on. However, this behaviour would only be desired during certain hours of the day
(the coffee machine should not turn on when the homeowner goes to bed, for example). It is likely
that there are many such scenarios that we haven't thought of which would present challenging cases
for the machine learning component to handle.

###### Thermostat {-}

The setting of a thermostat may be affected by several different factors, such as temperature, time
of day, and light levels. Since thermostats are also a non-binary output device, their behaviour
when controlled by the machine learning algorithms may be more varied than other devices.

###### Light Sensor {-}

A light sensor provides a non-binary input to the machine learning component. Similar to a motion
sensor, the level of light in a room may be related to the behaviour of many other devices.

###### Dimmer Switch {-}

A variable-voltage switch is an example of a non-binary output device. A variable-voltage switch
could be used to control the brightness of lights, or the speed of a fan.

###### Coffee Makers {-}

The coffee maker could be turned on in response to several different input devices (light sensor,
motion sensor)

#### Motion Sensor {-}

##### Technical Overview {-}

This section considers devices that can be used to alert the system when a person enters or leaves
an area of the home.

##### Sensor Technologies {-}

This section provides a comparison of several different sensor technologies that are commonly used
in motion detection.

###### Passive Infrared (PIR) {-}

A passive infrared sensor detects motion using the infrared radiation (heat) from a warm body. A
sensor contains two slots, each of which contains a material which is sensitive to infrared
radiation. As a warm body passes in front of the sensor, a different amount of radiation is received
at each slot. This difference in radiation causes a signal in the output of the device.

Use of the PIR modules encountered during this research does not require expert knowledge of circuit
design; the complexity of the circuits involved in connecting the modules to a microcontroller is
comparable to that of a simple LED circuit. A power source and a resistor is sufficient to get the
module up and running.

Most PIR modules have 3 pins to connect to a circuit. One pin connects to ground, another to power,
andthe third pin is used for output. The output consists of a single digital signal indicating when
motion is detected.

Tutorials describing how to connect PIR modules to common microcontrollers, such as a Raspberry Pi
or Arduino are widely available online.

The complexity of the circuit required to interface with a PIR module is comparable to the light
switch circuit, consisting of a single push button used to toggle an LED. Therefore, development
time required for the complete device is expected to be under 10 hours.

PIR sensor modules are reliable because they do not typically contain any moving components, other
than potentiometer used for sensitivity adjustment.

PIR sensors are easy to use, the main difficulties that a user may encounter in setting up a PIR
sensor are ensuring that the detectorès field of view covers the correct area, as well as
potentially adjusting the sensitivity of the detector.

PIR sensors are available with a range which is suitable for a typical room (approximately 7m
range).

The following tutorials explain how to interface with PIR modules:

<https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf>
<https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/>


###### Doppler-Effect based sensors {-}

Several types of motion detectors use the Doppler effect to detect motion. The detector transmits a
signal of a known frequency. This signal is reflected by any objects in its path and detected when
it returns to the sensor. The sensor tracks the frequency of the reflected wave; when a wave is
reflected off of a moving object the frequency of the reflected wave differs from that of the
incident wave due to the Doppler effect. This change in frequency is detected by the sensor and
registered as motion.

###### Infrared Break-Beam {-}

An infrared break-beam sensor consists of two physical modules separated by some distance.  One side
of the detector transmits a beam of infrared light which is detected by the other side.

###### Expertise Required {-}

- Little expertise required, circuits are simple
- Tutorials widely available online

###### Component Availability {-}

- Components widely available

###### Reliability {-}

- Sensors generally have a lower range than PIR sensors, availability of detectors with a longer
    range may be lower

- Allows for finer control over the area of detection than a PIR sensor

###### Usability {-}

- More difficult setup than a PIR sensor, requires the user to precisely aim the transmitted beam.

##### Feature Comparison {-}

| Feature    | Custom | D-Link Wifi Motion Sensor | Samsung SmarttThings Motion Sensor  | Belkin |
| -------    | ------ | ------------------------- | ----------------------------------- | ------ |
| Range      | 7m     | 8m                        | 15m - 40m                           | 3m     |
| Interfaces | _      | WiFi                      | ZigBee                              | WiFi   |
| Type       | PIR    | PIR                       | PIR                                 | PIR
|

Note: The custom device can potentially support multiple different communication interfaces

##### Evaluation {-}

| Criterion          | Score |
| ---------          | ----- |
| Expertise Required | Low   |
| Level of Effort    | Low   |
| Quality Comparison | Equal |


#### Variable-Voltage Switch {-}

The characteristics of variable-voltage switches vary significantly depending on the type of device
that the switch is expected to control (DC vs AC).

##### Controlling DC power {-}

If the type of device being controlled requires DC power input, the amount of power supplied to the
device can be controlled using pulse-width modulation (PWM). A digital output is used to create a
square wave. By varying the frequency of the square wave, it is possible to simulate the application
of a steady voltage between the pin's high and low voltages.

Limitations to simple PWM

- Power available to the device is limited by the power supplied by the controlling device - Limited
to DC devices

###### Expertise Required {-}

Minimal expertise is required to use PWM to control a device. The circuits required are as simple as
the circuits required to power a simple LED.

###### Reliability {-}

Simple PWM circuits are limited to controlling devices with low power requirements. While the
technique is reliable for devices which meet the power requirements, such as LED lamps, the power
requirements of most home devices means that the applicability of this technique will be severely
limited. Most devices are intended to be connected to a wall socket, meaning that they are expecting
AC current, which a significantly higher amount of power than is available from a microcontroller
such as an Arduino.

##### Controlling AC power {-}

###### Expertise Required {-}

- Safety concerns: Controlling devices which expect to receive the voltages available from
 a wall socket means dealing with high voltages. Without any team members trained in using high
 voltages, building a device to control high voltages is a very serious safety risk.

- Lack of trusted tutorials: For most of the circuits considered during this research, it has
 been possible to find tutorials online from trusted sources, such as the official Arduino website.

###### Level of Effort {-}

- When it was possible to find a tutorial online for building a circuit to control AC
 voltages, the circuit was found to be much more complex than the simple light switch circuit. Due
 to the amount of time required to fully understand these circuits, it is estimated that effort
 required is high.

| Feature            | Custom     | GE Z-Wave Plugin-in Smart Dimmer | Philips Hue Dimmer Switch | Lutron Caseta Wireless Plugin-In Lamp Dimmer |
| -------            | ------     | -------------------------------- | ------------------------- | -------------------------------------------- |
| Compatible Devices | AC devices | AC devices                       | Philips Hue Products      | AC Devices                                   |
| Interfaces         | _          | Z-Wave                           | ZigBee                    | Lutron Integration Protocol                  |

##### Evaluation {-}

| Criterion          | Score |
| ---------          | ----- |
| Expertise Required | High  |
| Level of Effort    | High  |
| Quality Comparison | Equal |

Note: There are safety concerns for custom-building this device

#### Light Sensor {-}

##### Description {-}

This section investigates devices which can detect the amount of ambient light in an area of the
house.

###### Photoresistors {-}

Light sensors generally make use of a component called a photoresistor. The resistance of a
photoresistor differs depending on the amount of light incident to the component. Phtoresistors are
also called photocells.

###### Reliability Characteristics {-}

- Photoresistors are unsuitable for precise lighting measurements because its resistance
 may vary due to temperature as well as light

- Photoresistors may exhibit latency (delay between a change in light and a change in resistance)

###### Photodiode {-}

Photodiodes are components which can be used similarly to photoresistors to detect light.  A
photodiode allows electrons to pass when there is light shining on it. The current allowed to pass
is proportional to the amount of light incident on the device.

Unlike photoresistors, a photodiode is not sensitive to temperature changes and may allow for more
accurate light detection. The circuit required to interface with a photodiode is of similar
complexity to the circuit required to interface with a photoresistor.

##### Expertise Required {-}

Minimal expertise is required to build the devices described by most guides and tutorials.  The
circuit is not significantly more complex than the light switch.

##### Level of Effort {-}

Due to the simplicity of the photoresistor circuit and the wide availability of the required
components and tutorials, a custom-built light sensor is required requires a low amount of effort.

##### Feature Comparison {-}

Many commercially available light sensors are included in combination devices which include several
different types of sensors. Commercial solutions provide very little data about the range of light
that their products can detect. For a custom built solution, the range of detectable light depends
on combination of the particular photocell chosen. Assuming that both a custom device and most
commercial devices are able to differentiate between daytime and evening levels of light, additional
features available from commercial devices are generally related to other types of sensors

##### Evaluation {-}

| Criterion          | Score   |
| ---------          | ------- |
| Expertise Required | Low     |
| Level of Effort    | Low     |
| Quality Comparison | Equal   |

#### Thermostat {-}

This section considers controlling a typical wall-mounted thermostat using a microcontroller such as
an Arduino.

##### Expertise Required {-}

Safety: Controlling a wall-mounted thermostat means working with mains voltage levels.  Without
knowledge in using high voltages, building this device is a significant safety risk

##### Effort Level {-}

Due to the lack of trusted tutorials online, as well as the wealth of features that users are used
to having in a thermostat, the time investment required to build a fully-featured thermostat is
extreme.

##### Evaluation {-}

Due to the extreme level of effort required and the safety concerns with building a thermostat, a
custom-built thermostat is not feasible for this project.

#### Alarm Clock {-}

There are a large variety of features available for alarm clocks, this section will focus on a
simple alarm clock that beeps at a programmed time of day. The clock should have manual (button)
input in order to allow the user to set alarm times so that the machine learning component can be
trained. More sophisticated clocks are expected to be much too complex for the team to build.

After review of many online tutorials for building alarm clocks, a common structure for a clock
circuit has been identified.

The basic alarm clock circuit generally requires the following components:

- LCD display
- Microcontroller
- Piezo Buzzer or Speaker
- Varying numbers of push buttons for manual configuration

##### Level of Effort {-}

Due to the need to interface with an LCD display, and because of the large number of components, a
custom build of an alarm clock is expected to be more complex than the light switch. The level of
effort is estimated to be high because of this.

##### Feature Comparison {-}

Homeowners may be used to alarm clocks with nice interfaces, often in the form of an app on their
phone. The custom alarm clocks investigated have significantly inferior interfaces, making use of a
4-button interface to set the time. The clocks considered here also lack features such as adjustable
alarm sounds, configuring multiple alarms, and setting weekly alarm schedules. Making a custom built
alarm clock as usable as commercially available clocks would require significant time investment.

#### Coffee Makers {-}

##### Using a Relay Switch {-}

A simple way to connect a coffee machine to a microcontroller is by using a voltage relay. A voltage
relay is an electrically controlled switch for high power devices. A simple coffee machine that only
needs to be plugged in in order to start brewing could be controlled using a simple voltage relay
circuit.

##### Level of Effort {-}

The same circuit which is used in the LED switch could be used to control the coffee machine, since
both the coffee machine and LED can be connected to the same voltage relay, so the level of effort
required is low.

##### Required Expertise {-}

- Safety risks: Coffee machine are normally connected directly into a wall socket. Controlling
 the coffee machine using a voltage relay would therefore involve high voltage levels which are
 unsafe to work with without proper training

In order to interface a microcontroller with more sophisticated coffee machines, some level of
reverse engineering of the coffee machine's control circuits would be necessaary. This would greatly
increase the amount of time necessary to create the device, due to the lack of electronics knowledge
on the team.

##### Evaluation {-}

Custom builds of both simple and fully-featured coffee makers may be infeasible due safety concerns
when controlling high voltage devices.

#### Summary of Evaluation {-}

| Device        | Level of Effort | Safety Concerns | Fully-Featured |
| ------        | --------------- | --------------- | -------------- |
| Motion Sensor | Low             | None            | Yes            |
| Light Sensor  | Low             | None            | Yes            |
| Dimmer Switch | Low             | High Voltage    | Yes            |
| Coffee Maker  | High            | High Voltage    | No             |
| Thermostat    | High            | High Voltage    | No             |
| Alarm Clock   | Low             | None            | No             |

#### Conclusions {-}

It is feasible for the team to build motion sensor, light sensors, and an alarm clock if no
acceptable commercial solution is available. We should avoid building dimmer switches, coffee
makers, and thermostats due to the potential high-voltage work involved and the lack of electronics
knowledge available.
