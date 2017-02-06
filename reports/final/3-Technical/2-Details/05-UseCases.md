### Use Cases

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

Postcondition: The device's state will now be used as input in learning mode. If the device contains
an actuator, the actuator will be controlled by the learning hub in normal mode.

##### Enter Learning Mode {-}

The user enters learning mode in order to indicate to the system that it should begin recording
changes in the state of connected devices, without attempting to control them. Learning mode
accomplishes the user's goal of configuring the system without manual programming.

1. User selects enter learning mode
2. While the system is in learning mode, the system will record the user's interactions with
   connected devices.
3. When the user selects normal mode or standby mode, the system exits learning mode.

Postcondition: The system saves changes in the state of connected devices.

##### Enter Normal Mode {-}

The user enters normal mode in order to instruct the system to begin controlling connected
devices.

1. User selects enter normal mode
2. System exits the currently active mode
3. System begins controlling connected actuators, using the data collected during learning mode
   to infer the desired state of the system.

Postcondition: The system maintains control over connected actuators.

##### Enter Standby Mode {-}

The user enters standby mode in order to instruct the system that control over connected devices
should be halted, and changes in the state of devices should not be accepted as learning data.
Standby mode allows a user to control their devices under exceptional circumstances without learning
the system to perform an incorrect task.

1. User enters standby mode
2. System exits the active mode

Postcondition: System does not accept learning data, System does not modify the state of devices

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
states in normal mode.


