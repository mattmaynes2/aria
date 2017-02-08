### Overview {#sec-3-2-1-1}

#### Introduction {-}

The Autonomous Real-Time Interactive Architecture (Aria) will allow a homeowner to set up a collection
of devices in their home which will automatically control their environment and automate common tasks.
Task automation in the system will not require any user configuration, instead tasks will be automated
based on the user's interaction with devices in the system.

The system will consist of a hub device with a simple interface that a homeowner can connect to their
home network. After connecting the hub, the homeowner can add enabled devices for the system to
control by simply connecting them to the network. As new devices are connected, their input will be
used to make more predictive decisions about user behaviour.

#### Product Functions {-}

To ensure a non-technical user can utilize the system, the system must be easy to use and highly
interactive. The system will provide a smart hub that will be the base of computation and
communication for all other components in the system.

The system will have many different smart devices. These devices can be sensory inputs or controls
for a task. To allow for expansion of the automation system, it must be able to accept new devices.
The system must then retain its previous model of the user's interactions but add in the new device
as evidence for predicting future behaviours. For example, a system might include a light sensor,
thermostat and curtain puller. If the ambient light outside was to drop and the user closed the
curtains then the system might predict that a change in light corresponds to that action. If the
user then changes the temperature, the system may relate light to temperature as well. If later a
temperature sensor was added to the system and the user changes the temperature when it is too cold,
the system will use this information to predict future actions.

To be able to monitor and control the system, the learning hub must be controllable using a
graphical interface. This interface will be provided in the form of a web interface and allow the
user to view the state of the system and manually control any connected device. This interface can
be used for manually configuring desired behaviours as well as for enabling the learning mode of the
system. The interface must allow the user to view the state of all devices in the system as well as
view their recorded interactions.


