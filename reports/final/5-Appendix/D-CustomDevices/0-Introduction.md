## D Custom-Built Devices {- #D}

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

##### Quality Comparisons {-}

Commercially available devices may offer features which could be useful to demonstrate the system,
but are difficult to include in a custom-built device. It will be useful to determine whether or not
the devices described by most custom-build tutorials are fully featured. In some cases, the features
of a typical custom-built device will be compared against several commercial options.

#### Devices of Interest {-}

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

##### Motion Sensors {-}

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

##### Thermostat {-}

The setting of a thermostat may be affected by several different factors, such as temperature, time
of day, and light levels. Since thermostats are also a non-binary output device, their behaviour
when controlled by the machine learning algorithms may be more varied than other devices.

##### Light Sensor {-}

A light sensor provides a non-binary input to the machine learning component. Similar to a motion
sensor, the level of light in a room may be related to the behaviour of many other devices.

##### Dimmer Switch {-}

A variable-voltage switch is an example of a non-binary output device. A variable-voltage switch
could be used to control the brightness of lights, or the speed of a fan.

##### Coffee Makers {-}

The coffee maker could be turned on in response to several different input devices (light sensor,
motion sensor)

