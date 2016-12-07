## Requirements {#section-reqs}

### Overview

#### Introduction {-}

The Autonomous Real-Time Interactive Architecture (ARIA) will allow a homeowner to set up a collection
of devices in their home which will automatically control their environment and automate common tasks.
Task automation in the system will not require any user configuration, instead tasks will be automated
based on the user's interaction with devices in the system.

The system will consist of a hub device with a simple interface that a homeowner can connect to their
home network. After connecting the hub, the homeowner can add enabled devices for the system to
control by simply connecting them to the network. As new devices are connected, their input will be
used to make more predictive decisions about user behaviour.

#### Project Scope {-}

The purpose of the system is to make home automation as easy as possible to set up. Many existing
home automation systems require some form of programming from the user, in the form of a schedule or
explicit scenarios which describe how the devices connected to them should behave. This project will
improve upon such systems by inferring the correct state of connected devices from data collected
during the homeowner's routine use of the devices.

Activities which are "In Scope":

- Provide a range of devices that can be installed in a home which showcase the learning
 capabilities of the system.

- Create a hub device that collects data from installed sensors, and uses this data to infer the
  desired values of actuators.

- Provide a simple interface which allows the homeowner to toggle on/off automated control of
 devices.

- Develop a protocol which allows developers to enable new types of devices for use in the system

### Overall Description

#### Product Perspective {-}

Systems are becoming more readily available in the general market place. This system builds upon
traditional home automation systems by adding true automation in the form of learning. Unlike
traditional systems, this system observes the homeowner's interactions with devices and
automatically makes decisions based on historical behaviours. By combining the fields of machine
learning and home automation, the our system will provide an end user with a simplified
smart home experience.

#### Product Functions {-}

To provide simplicity and seamless interaction, the system must be easy to use and highly
interactive. The system will provide a learning hub that will be the base of computation and
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
be used for manually configuring desired behaviours as well as for enabling the training mode of the
system. The interface must allow the user to view the state of all devices in the system as well as
view their recorded interactions.

#### User Classes {-}

While the primary audience of the system is a homeowner, it is also for building owners, nursing
home residence, or anyone who needs building automation. The end user of this product is intended to
be non-technical users who want simple control and automation of their building. This product will
also provide utilities for more technically proficient users who wish to create their own devices
that communicate to the system.

##### Base User (Non-Technical Users) {-}

- End user of the system that needs simple interface to use system - Will want low maintenance to
keep system running and expect system to perform correctly

##### Developers (Technical Users) {-}

- Will require technical documentation about the system - Will require a development toolkit for
creating custom devices for the system - May also be a base user

### System Features

![][system-use-case]

#### Install Hub {-}

The user installs the learning hub in their home in order to enable automation of their smart
devices.

1. User plugs hub into outlet and turns power on
2. User connects hub to a home network using Ethernet
3. Hub provides confirmation that system is online

##### Add Device {-}

Devices can be added to the system simply by powering them on and connecting to the network.

Precondition: A learning hub must be installed in the user's home.

1. User plugs in device and turns power on
2. Device discovers network
3. Hub discovers device and provides confirmation

Postcondition: The device's state will now be used as input in training mode. If the device contains
an actuator, the actuator will be controlled by the learning hub in playback mode.

##### Enter Training Mode {-}

The user enters training mode in order to indicate to the system that it should begin recording
changes in the state of connected devices, without attempting to control them. Training mode
accomplishes the user's goal of configuring the system without manual programming.

1. User selects enter training mode
2. While the system is in training mode, the system will record the user's interactions with
   connected devices.
3. When the user selects playback mode or standby mode, the system exits training mode.

Postcondition: The system saves changes in the state of connected devices.

##### Enter Playback Mode {-}

The user enters playback mode in order to instruct the system to begin controlling connected
devices.

1. User selects enter playback mode
2. System exits the currently active mode 
3. System begins controlling connected actuators, using the data collected during training mode
   to infer the desired state of the system.

Postcondition: The system maintains control over connected actuators.

##### Enter Standby Mode {-}

The user enters standby mode in order to instruct the system that control over connected devices
should be halted, and changes in the state of devices should not be accepted as training data.
Standby mode allows a user to control their devices under exceptional circumstances without training
the system to perform an incorrect task.

1. User enters standby mode
2. System exits the active mode

Postcondition: System does not accept training data, System does not modify the state of devices

##### Remove device {-}

Devices will stop recording when removed from the smart learning network. To remove the history of
the device, the user can delete it using the remote interface.

1. User disconnects device from the network
2. If the user wishes to remove the device permanently, include use case Reset Device

##### Reset Device {-}

If the input of a device is causing unexpected or undesired output then it can be reset by the user
through the remote interface.

1. User logs in to remote interface
2. User selects a device
3. User selects reset device
4. System erases the saved historical states of the device

Postcondition: States of the selected devices from before the reset are no longer used to infer
states in playback mode.

### External Interface Requirements

#### User Interfaces {-}

##### Remote Interface {-}

The remote interface will allow the user to control the system and any device that is connected in
the network. The remote interface will be a web application that is served to the user's computer
from the learning hub.

###### Accessing the Interface {-}

To load the web application, the user will navigate through a web browser to the address of their
learning hub. The hub will then provide the remote interface and prompt the user with a login. The
first time the user opens the hub control page they will be prompted to create an account.

###### Viewing and Controlling Devices {-}

The primary use of this remote interface will be to observe the state of the system as well as
control any connected device. The remote interface must provide access to the recent history of all
interactions that have occurred in the system. The interface must provide a mechanism for searching
the logs and grouping them based on time and device.

The system must also be able to control the devices that are connected to it. The remote interface
must provide the appropriate controls for each device that is connected to the system.

###### Controlling the Hub {-}

The interface must graphically provide methods to customize the learning hub's operation. This will
include properties related to the system such as network connections, login options and any other
hub specific items.

###### Exiting the Remote {-}

Once the user is finished with the remote interface, they can log out or simply close the web
application. For security reasons, if a user is inactive in their session for more than a set amount
of time then they will be logged out automatically.

![][remote-use-case]

#### Hardware Interfaces {-}

##### Learning Hub Interface {-}

To maximize simplicity, the learning hub interface will have a clean and minimal interface. It will
provide the user with three control buttons and one reset button. The control buttons will allow the
user power off and on the device as well as toggle the state between training mode, playback mode
and standby.

The hub will provide user feedback with a single multi-colour LED. The LED will be used to indicate
the state of the device. There will be a state for all three operation modes; training, playback and
standby. If there is an error in the device, the LED can be used to indicate the error.

There will also be two external ports on the device. One will be used to power the device from a
standard home wall outlet. The other can be a standard Ethernet port and be used to connect to the
network.

### Other Nonfunctional Requirements

#### Performance Requirements {-}

##### Device Communication Range {-}

Devices must be able to communicate wirelessly using the network. The range of communication must be
sufficiently large that devices can be placed anywhere in an average home. The smart home devices
will need to be capable of receiving and transmitting data using this network with enough range.

The distance between nodes in our system must be no more than 50 meters. The will allow for any
protocol to communicate with the necessary nodes.

##### System Responsiveness {-}

The system must readily adapt to environmental changes to be effective. When in training mode, the
system does not make any decisions and therefore has no responsiveness requirement. However, when
the system enters playback mode it must make decisions as fast as environmental changes are
received. This will ensure that the system is as responsive as possible when a user performs an
action.

#### Security Requirements {-}

##### Device Connection Security {-}

All commands to devices must be authenticated to ensure that they are from an authorized source.
This is in order to eliminate the possibility of malicious entities taking control of a home's
devices.

##### Remote Interface Security {-}

Digital access to the hub's configuration interface must be secured using TLS 1.2 (RFC 5246) and
HTTP basic authentication as described in RFC 2617. Use of these Internet Official Protocol
Standards ensures that the system uses widely accepted authentication practices.

#### Quality Requirements {-}

##### Learning Hub Reliability {-}

The learning hub is the center of communications and is responsible for interfacing with the system
user. It must record data on some form of internal storage to log actions that have occurred as
well as decisions that is has made. It is critical that the learning hub not lose its data as this
would set the system back to its initial, untrained state. Precautions should be taken so that in
the case of a system failure or power failure, the critical system data is preserved. Hub
operations should be atomic and reversible should they fail.

The learning hub must also be online and available to record system events. If the learning hub is
to go into a state faulty state then it should indicate this to the user. The system must provide
a mechanism for resetting itself if errors are occurring.

##### Device Reliability {-}

Devices in the system do not need to meet as high of a standard as the learning hub for
reliability. However, devices should have some indicator when faults occur. Devices may be hard
to access so any device that can be restarted should provide functionality for doing so from the
remote interface. If this is not possible then as a minimum, the remote interface should
indicate whether or not a device has encountered a fault or if it is no longer responding.
Restarting a device in the network should then reconnect to the system and retain all of its
history within the learning hub.




