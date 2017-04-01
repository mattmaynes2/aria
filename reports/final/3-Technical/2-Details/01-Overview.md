### Overview {#sec-3-2-1-1}

#### Introduction {-}

The Autonomous Real-Time Interactive Architecture (Aria) allows a homeowner to set up a system in 
their home which will automatically control their environment and automate common tasks.
Task automation in the system does not require manual programming; instead, tasks automation is
learned based on the user's interaction with devices in the system.

The system consists of a hub device with a simple interface that a homeowner can connect to their
home network. After connecting the hub, the homeowner can add enabled devices for the system to
control by simply connecting them to the network. As new devices are connected, their input is
used to make more predictive decisions about user behaviour.

#### Product Functions {-}

The system provides a smart hub that acts as a central communication and control point for the 
system.

The system may be connected to have many different smart devices. These devices can be sensors,
or controllable actuators. The system must provide a simple way to connect new devices to the system.
After adding a new device, the system should not require a complete re-training (i.e. it should
continue to automate tasks based on data from before the new device was added).
For example, consider a system that is connected to a light sensor, thermostat and curtain puller.
If the ambient light level outside drops and the user closes the curtains, the system might predict
that a change in light level should activate the curtain puller. If the user later installs a
temperature sensor, the system should continue activating the curtain puller when the light level 
changes, while using the new temperature data to learn additional behaviours.

To be able to monitor and control the system, the learning hub must be controllable using a
graphical interface. This interface will be provided in the form of a web interface and allow the
user to view the state of the system and manually control any connected device. This interface can
be used for enabling or disabling learned behaviours as well as for controlling the system's learning
mode. The interface must also allow the user to view the state of all devices in the system.


