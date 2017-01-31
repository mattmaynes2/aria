### A-1 Automation Systems {- #A-1}

##### Background {-}

This section contains research on existing home automation systems in order to better understand
what technologies currently exist. This research is intended to help understand how a new system
could improve on existing technology or if there are particular architecture patterns that are
relevant for this system's design. In particular, this research focuses on features that are common
between home automation systems and their benefits to the end user.

Since usability is the focus of this system, it is important to investigate the features that a
user would expect in a smart home system. It is also important to examine any short comings of
existing systems and if these short comings can be addressed.

In order to compare these smart home systems, a set of criteria is required such that they can
be evaluated. For this research, the following criteria will be examined: supported communication
protocols, device discovery and setup, network configuration, application programming interfaces,
third party integrations and limitations. If there are common protocols across all main automation
systems then they should be considered for this system. Industry standard protocols may be
discovered by reviewing these existing systems. If there is a special focus on the ease of use
then this system should consider the efforts that other systems have taken. The network
configuration of a system will govern its performance, power consumption and allowable number of
connections. This research will investigate how these systems organize their network topologies
to satisfy these quality attributes. In order to control these devices we require that the
following; a way to view all connected devices, a way to get notifications when a device in the
system changes states, a way to change the state of a device. Finally, if there are accepted
standards of third party integrations then this system should consider them in its design to
maximize overall interoperability.

#### A-1-1 Insteon {- #A-1-1}

##### Description {-}

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

##### Technical Overview {-}

###### Supported Communication Protocols {-}

Insteon uses a proprietary messaging protocol to send messages between devices and the central hub.
The Insteon messaging protocol uses message repeating to send messages across a peer-to-peer network
of devices. This messaging protocol is outlined in a detailed
[white paper](http://cache.insteon.com/documentation/insteon_details.pdf) that describes the
network protocol as well as the messaging protocol.[^A-1-2]

Insteon also integrates with a number of third party devices and controllers. These third party
devices can be added to the network and be controlled through the Insteon smart hub. The hub's
devices can also be controlled through the integrations of these third party devices.[^A-1-2]

###### Device Discovery and Setup {-}

Adding a new device is done through the Insteon app. A new device is first plugged in and turned on.
The device then locates the user's mobile app on the network and is ready to be connected.
Using the app the user selects the new device and enters the device ID. Once the ID is
entered the device is able to be configured and added to the Insteon network.[^A-1-2]

###### Network Configuration {-}

Insteon uses a central hub to communicate between the devices and the users app. The Insteon hub
is used for all device communications and control. Devices connect and send all event information
to the central hub.

Insteon uses a peer-to-peer network to connect the devices [^A-1-3]. All of Insteon's devices can
act as a controller to send messages, a repeater to forward messages or a responder to receive
messages.

###### Application Programming Interfaces {-}

Insteon provides a complete REST API for querying the properties of their hub. The REST API allows
a client to query properties about the hub, the connected devices, any connected cameras, contacts,
scenes, rooms and more. The API also provides endpoints for setting data values in devices and
configuring properties of users [^A-1-4].

The REST documentation does state that there are some limitations in the design of the protocol.
It states that the REST API does not provide full support for configuring devices and scenes and
states that the Insteon app is still required for complete access [^A-1-4].

###### Third Party Support {-}

Insteon produces its own devices for most of its smart home purposes [^A-1-5]. On top of these
basic devices, Insteon has created integrations with a number of third party smart technology
vendors. These vendors include: Nest, Logitech, Amazon Echo, Stringify, Apple HomeKit,
Cortana, First Alert, Sonos, and MiLocks [^A-1-6].

This exceptional list of partners demonstrates that the Insteon API is flexible enough to
support many existing industry technologies. This may indicate that their platform is
generic enough to support all smart device requirements. The framework developed by Insteon
would be a valuable area of study for this project's design.

###### Limitations {-}

As stated in the API section of this analysts, in order to properly configure all devices and
scenes in the Insteon system, the Insteon app is required. This limitation impedes on the
user experience of the system and would hurt the overall usability.

##### Summary {-}

#### A-1-2 Wink {-}

##### Description {-}

Wink Hub is a hub that specializes in allowing communication between many different smart devices.
Wink supports control of devices using scheduling and IFTTT.

##### Technical Overview {-}

Wink is a central hub that supports most of the popular communication protocols for home automation,
giving users the freedom of connecting and controlling a variety of smart devices in one system.

###### Communication Protocol {-}

Wink Hub supports the following communication protocols:

- WiFi
- Bluetooth smart (BLE)
- Z-Wave Plus
- ZigBee
- Lutron's Caseta
- Kidde

###### Device Discovery and Setup {-}

Supporting many different manufacturers means that there are a variety of different ways for
devices to connect to the Wink Hub. The two most common ways are:

###### 1) Button Pressing {-}

Pressing a button on the Wink Hub broadcasts a pairing signal across the network. Any new device
that receives this signal will then appear on the network, and can be viewed from the Wink app. The
user then selects the new device and enters the device ID (located on the physical device) to add
it to the automation system. 

###### 2) Manufacturer Setup {-}

The new device must be added to the home network using the app provided by the manufacturer. Once
it has been added through the manufacturers app, it will be visible using the Wink app. It can be
added to the automation system from here using the Wink app.

###### Network {-}

The Wink system uses a central hub to connects different devices. Devices communicate only with the
central hub.

###### API {-}

Wink provides a RESTful service through the Wink hub and a secondary partner PubNub.

| Feature                               | Supported |
| ---------                             | --------  |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |

###### Third Party Integrations {-}

Wink has support for the following manufacturers:

|           |             |                     |             |         |
| ---       | ---         | ---                 | ---         | ---     |
| Nest      | Philips     | GE                  | Leviton     | Rheem   |
| Honeywell | TCP         | Kidde               | Kwiset      | Lutron  |
| Rachio    | Bali        | Amazon              | Andersen    | Canary  |
| Carrier   | Chamberlain | Commercial Electric | Cree        | Dropcam |
| Ecobee    | Emerson     | GoControl           | Hampton Bay | IHome   |
| Leaksmart | Osram       |                     |             |         |

##### Evaluation {-}

Providing support for the most popular communication protocols allows Wink to connect with almost
any device a user can purchase, making them an attractive option to consumers. This is a feature
that we hope to mimic, although not to the full extent of Wink. Specifically, the methods of
connecting devices from any manufacturer will likely be useful to us for this project.


#### A-1-3 SmartThings {-}

##### Description {-}

SmartThings is Samsung's home automation system. Similar to  Wink, they provide their own app
allowing a user to control devices using scheduling or IFTTT.

##### Technical Overview {-}

###### Communication Protocols {-}

SmartThings supports devices that communicate using the Z-Wave, ZigBee, or WiFi communication
protocols

###### Device Discovery and Setup {-}

Adding a new device is done through the app. A user will click "find device", prompting the hub
to search for any new Z-Wave, ZigBee, or WiFi devices. When the device is found the user adds 
it to a room and names the device.

##### Network {-}

SmartThings uses a central Hub to connect all of the smart devices. The SmartThings app talks with
the SmartThings Cloud which talks to the Hub which then controls the devices.

###### API {-}

SmartThings provides a Groovy API to create SmartApps that allow control of devices.

| Feature                               | Supported |
| ---------                             | --------  |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |


###### Limitations {-}

Requires a SmartThings hub and connection to the SmartThings cloud.

##### Third Party Integrations {-}

|            |                     |                |                 |                    |
| ---        | ---                 | ---            | ---             | ---                |
| 2Gig       | Aeon Labs           | Amazon         | Belkin          | Bose               |
| Cree       | ecobee              | Ecolink        | EcoNet Controls | Enerwave           |
| Everspring | Fibaro              | Fidure         | First Alert     | FortrezZ           |
| GE         | Google              | Honeywell      | iHome           | Keen Home          |
| Kwikset    | Leak Intelligence   | Leviton        | LiFi Labs       | Linear             |
| Netgear    | OSO Technologies    | OSRAM LIGHTIFY | Philips Hue     | Remotec Technology |
| Samsung    | Samsung SmartThings | Schlage        | Sengled         | Skybell            |
| Spruce     | Yale                | Zen            |                 |                    |

##### Evaluation {-}

The Samsung home automation system provides a reasonable level of support for
different communication protocols, giving it a healthy amount of third party support.
This is something that we will be striving for in out project. The dependency on the 
connection to a cloud service is something that we would like to avoid for our project.


#### A-1-4 Apple HomeKit {-}

##### Description {-}

Apple HomeKit allows users to control their smart devices using their iPad or iPhone. Apple HomeKit
does not require any central hub to control the devices, but does require there to be Apple device
connected to the network at all times. If a user wants to control devices with an iPhone while not
at home, the devices must be connected to an Apple product that is connected to the network, such
as an iPad or Apple TV.

##### Technical Overview {-}

The smart devices are able to be scheduled and controlled in groups from the app.

###### Communication Protocol {-}

Apple HomeKit uses WiFi as the only communication protocol.

###### Device Discovery and Setup {-}

Adding new devices is done through the app. Once a device is connected to the network
it can be added to the home through Apple's app, some devices require some configuration
in their manufacturers apps.

###### Network {-}

HomeKit uses the homes WiFi network to connect devices and all devices on the network are 
able to communicate with one another.

###### API {-}

| Feature                               | Supported |
| ---------                             | --------  |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |

##### Evaluation {-}

There are a few aspects of the Apple HomeKit that are not ideal for incorporation into our project.
First, it is Apple exclusive, which goes against the goal of having many third party support
options. The lack of a central hub also makes it difficult to having support for many different
types of devices. The level of communication between devices that is offered by the Apple solution
is a desirable feature, but will be difficult to achieve while maintaining diverse third party
support.


#### Summary of Evaluation {-}

A common theme among existing home automation systems is that systems with a large amount of
third party support rely on a central communication hub. Having a hub allows components from
different manufacturers to communicate to each other through the hub. A challenge that supporting
a large number of devices presents is how to discover new devices into a system, which can be delt
with in several different ways such as manual button pressing or app configuration. 

Looking at these systems also presented several communication protocols to investigate, including
Z-wave, Zigbee, Insteon and WiFi. Along side these are devices from many different manufacturers 
which operate using these communication protocols. Deciding on a communication protocol and 
subsequent device manufactures to support is an important part of our design for our home
automation system.

[^A-1-1]: "Home," in Insteon, Insteon, 2016. [Online]. Available: <http://www.insteon.com/>. Accessed: Oct. 6, 2016.
[^A-1-2]: "WHITEPAPER: The Details,". [Online]. Available: <http://cache.insteon.com/documentation/insteon_details.pdf>. Accessed: Oct. 6, 2016.
[^A-1-3]: "WHITEPAPER: Compared,". [Online]. Available: <http://cache.insteon.com/documentation/insteon_compared.pdf>. Accessed: Oct. 6, 2016.
[^A-1-4]: "Insteon API · Apiary,". [Online]. Available: <http://docs.insteon.apiary.io/>. Accessed: Oct. 6, 2016.
[^A-1-5]: "Technology," in Insteon, Insteon, 2016. [Online]. Available: <http://www.insteon.com/technology/>. Accessed: Jan. 31, 2017.
[^A-1-6]: "Insteon Connects," in Insteon, Insteon. [Online]. Available: <http://www.insteon.com/connects>. Accessed: Jan. 31, 2017.
[^A-1-7]: "Wink API · Apiary,". [Online]. Available: <http://docs.winkapiv2.apiary.io/#reference/oauth/obtain-access-token>. Accessed: Oct. 9, 2016.
[^A-1-8]: "Wink FAQ - Wink@Home Wiki," 2015. [Online]. Available: <http://wiki.winkathome.net/Wink_FAQ>. Accessed: Oct. 6, 2016.
[^A-1-9]: "A simpler smart home," Wink, 2016. [Online]. Available: <http://www.wink.com/help/faq/>. Accessed: Oct. 8, 2016.
[^A-1-10]: "Samsung SmartThings hub FAQ — SmartThings developer documentation," 2016. [Online]. Available: <http://docs.smartthings.com/en/latest/sept-2015-faq.html>. Accessed: Oct. 6, 2016.
[^A-1-11]: "How it works," SmartThings, 2016. [Online]. Available: <https://www.smartthings.com/how-it-works>. Accessed: Oct. 10, 2016.
[^A-1-12]: "Use the home app on your iPhone, iPad, and iPod touch," Apple Support, 2016. [Online]. Available: <https://support.apple.com/en-ca/HT204893>. Accessed: Oct. 10, 2016.



