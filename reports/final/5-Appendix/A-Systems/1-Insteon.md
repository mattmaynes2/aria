### A-1 Insteon {- #A-1}

#### Description {-}

Insteon is a home automation system that allows smart devices to connect over a home area network
with a focus on ease of use. Insteon allows you to monitor and control all of the devices within
the system. All devices in connect through a central Insteon smart hub which is then controlled
by the user through a app on the user's mobile device. Controlling devices can also be automated
using manually configured schedules, IFTTT or through the use of **scenes**.

A scene allows a user to configure device behaviours based on grouping of devices in their home.
The devices are grouped into rooms which can represent the physical rooms of the home. The user
can then create a configuration for a specific date, time or environmental condition. Insteon
then monitors the state of the home for these conditions, when they are met then it recreates
the user's configuration. [^A-1-1].

#### Technical Overview {-}

##### Supported Communication Protocols {-}

Insteon uses a proprietary messaging protocol to send messages between devices and the central hub.
The Insteon messaging protocol uses message repeating to send messages across a peer-to-peer network
of devices. This messaging protocol is outlined in a detailed
[white paper](http://cache.insteon.com/documentation/insteon_details.pdf) that describes the
network protocol as well as the messaging protocol.[^A-1-2]

Insteon also integrates with a number of third party devices and controllers. These third party
devices can be added to the network and be controlled through the Insteon smart hub. The hub's
devices can also be controlled through the integrations of these third party devices.[^A-1-2]

##### Device Discovery and Setup {-}

Adding a new device is done through the Insteon app. A new device is first plugged in and turned on.
The device then locates the user's mobile app on the network and is ready to be connected.
Using the app the user selects the new device and enters the device ID. Once the ID is
entered the device is able to be configured and added to the Insteon network.[^A-1-2]

##### Network Configuration {-}

Insteon uses a central hub to communicate between the devices and the users app. The Insteon hub
is used for all device communications and control. Devices connect and send all event information
to the central hub.

Insteon uses a peer-to-peer network to connect the devices [^A-1-3]. All of Insteon's devices can
act as a controller to send messages, a repeater to forward messages or a responder to receive
messages.

##### Application Programming Interfaces {-}

Insteon provides a complete REST API for querying the properties of their hub. The REST API allows
a client to query properties about the hub, the connected devices, any connected cameras, contacts,
scenes, rooms and more. The API also provides endpoints for setting data values in devices and
configuring properties of users [^A-1-4].

The REST documentation does state that there are some limitations in the design of the protocol.
It states that the REST API does not provide full support for configuring devices and scenes and
states that the Insteon app is still required for complete access [^A-1-4].

##### Third Party Support {-}

Insteon produces its own devices for most of its smart home purposes [^A-1-5]. On top of these
basic devices, Insteon has created integrations with a number of third party smart technology
vendors. These vendors include: Nest, Logitech, Amazon Echo, Stringify, Apple HomeKit,
Cortana, First Alert, Sonos, and MiLocks [^A-1-6].

This exceptional list of partners demonstrates that the Insteon API is flexible enough to
support many existing industry technologies. This may indicate that their platform is
generic enough to support all smart device requirements. The framework developed by Insteon
would be a valuable area of study for this project's design.

##### Limitations {-}

As stated in the API section of this analysts, in order to properly configure all devices and
scenes in the Insteon system, the Insteon app is required. This limitation impedes on the
user experience of the system and would hurt the overall usability.

#### Summary {-}


[^A-1-1]: "Home," in Insteon, Insteon, 2016. [Online]. Available: <http://www.insteon.com/>. Accessed: Oct. 6, 2016.
[^A-1-2]: "WHITEPAPER: The Details,". [Online]. Available: <http://cache.insteon.com/documentation/insteon_details.pdf>. Accessed: Oct. 6, 2016.
[^A-1-3]: "WHITEPAPER: Compared,". [Online]. Available: <http://cache.insteon.com/documentation/insteon_compared.pdf>. Accessed: Oct. 6, 2016.
[^A-1-4]: "Insteon API · Apiary,". [Online]. Available: <http://docs.insteon.apiary.io/>. Accessed: Oct. 6, 2016.
[^A-1-5]: "Technology," in Insteon, Insteon, 2016. [Online]. Available: <http://www.insteon.com/technology/>. Accessed: Jan. 31, 2017.
[^A-1-6]: "Insteon Connects," in Insteon, Insteon. [Online]. Available: <http://www.insteon.com/connects>. Accessed: Jan. 31, 2017.



