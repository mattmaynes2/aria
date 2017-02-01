### E-9 Aeon Labs {- #E-9}

#### Description {-}

Aeon Labs is a company that produces a large variety of Z-Wave devices. They also provide
the ability to create your own home automation hub.

#### Technical Overview {-}

Aeon Labs produce a USB dongle that allows you to turn any computing device into a Z-Wave
communication hub. This hub allows the user to manually control any Z-Wave device on the Z-Wave
network, and provides the functionality to add and remove devices to/from the network. To add a
Z-Wave device, start by unplugging the dongle from the hub and pushing the button on it. Then
walk to the new device and push the button on the device. The dongle must also be unplugged to
remove a device from the network. To put it in removal mode, push and hold the button on the
dongle. Then go to each device you wish to remove from the network and push the button. The dongle
can be bought for about $60.

They do not provide their own hub, which is ideal for out project. They simply allow the ability
to turn a computing device into a custom hub by providing the required RF signal to communicate
with Z-Wave devices. To begin development for Z-Wave devices, The list of Z-Wave devices from
Aeon Labs alone is fairly extensive. The list include but is not limited to: door sensors, window
sensors, lights, energy meters, range extenders.

The specification for interacting with Z-Wave devices is public, and available at
<http://zwavepublic.com/specifications>. There is also an open Z-Wave sdk available, to communicate
from the controller to devices.

#### Available Devices of Interest {-}

1. MultiSensor
- Motion Sensor
- Temperature Sensor
- Light Sensor
- Humidity Sensor
- Vibration Sensor
- UV Sensor

The MultiSensor is a Z-Wave device, meaning that it follows the Z-Wave protocol for commands
interacting with each individual sensor. As stated above, the speficication for interacting with
Z-Wave devices is available at <http://zwavepublic.com/specifications>. 

Individual Z-Wave sensors are also available, and function using the same specifications as the
MultiSensor above. AARTech is one alternative which has a selection of individual sensors if the
MultiSensor is unnecessary.

2. Door / Window Sensor
- Detect window/door state
 The Door/Window sensor is purposed to be able to detect the state of doors or windows. This allows
 the system to use information about the state of doors and windows to make decisions about what
 actions to take. 

 
#### Evaluation {-}

Aeon Labs is an ideal solution for our project. To start, there is an easy way to set up our own
hub, instead of being constrained to buying one. This allows us to implement the features we want,
and add support for protocols we want without restriction. Having access to an sdk is very
important to us as well. It lets us not be responsible for implementing the Z-Wave stack protocol,
while also giving us the freedom to use the information received by the devices in a unique way.
Specifically, this will provide us with data for the machine learning algorithm.

