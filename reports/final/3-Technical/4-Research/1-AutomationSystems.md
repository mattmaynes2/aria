### Automation Systems {#section-rs-sys}

#### Background {-}

In this section we are looking at existing systems so that we can better understand what
technologies currently exist in the market. Having a better grasp of existing technology will help
us understand how we can differentiate our smart home automation system. In particular, we are
interested in which features are common in home automation systems and their benefits to the end
user.

An important aspect of our project is to have custom logic for controlling smart devices in a home
automation system. Existing systems implement their own logic, so we will not be using them
directly. Looking at existing systems gives us a better understanding of what the end user expects
of home automation, allowing us to better design our own system.

The research will investigate the following characteristics of existing home automation systems.

###### Supported Communication protocols {-}

Which protocols does the system support? If there are common protocols across all main automation
systems then they should be considered for this system. Industry standard protocols may be
discovered by reviewing these existing systems.

###### Device Discovery and Setup {-}

How are new devices added to the system's network? If there is a special focus on the ease of use
then this system should consider the efforts that other systems have taken.

###### Network {-}

How do these systems setup the network of devices. Do they use a central server, are all devices
independent? The network configuration of a system will govern its performance, power consumption
and allowable number of connections. This research will investigate how these systems organize
their network topologies to satisfy these quality attributes.

###### API {-}

Does the system provide an API that our system could potentially use to control the devices
connected to these systems. In order to control these devices we require that the following; a way
to view all connected devices, a way to get notifications when a device in the system changes
states, a way to change the state of a device.

###### Third Party Integrations {-}

Which companies have these systems decided are important to support? If there are accepted standards
of third party integrations then this system should consider them in its design to maximize overall
interoperability.


#### Insteon {-}

##### Description {-}

Insteon is a home automation system that allows smart devices to connect over a home area network
with a focus on ease of use. Insteon allows you to monitor and control all of the devices within
the system. All devices in connect through a central Insteon smart hub which is then controlled
by the user through a app on the user's mobile device. Controlling of s can also be automated
using manually configured schedules, IFTTT or through the use of **scenes**.

A scene is configured a configuration for a room that the user sets up at a specific time or when
specific environmental conditions are met. Insteon has all of the devices remember their current
states and whenever these states are met then it has the devices recreate the saved scene.[^B-1-1]

##### Technical Overview {-}

###### Supported Communication Protocols {-}

Insteon uses a proprietary messaging protocol to send messages between devices and the central hub.
The Insteon messaging protocol uses message repeating to send messages across a peer-to-peer network
of devices. This messaging protocol is outlined in a detailed
[white paper](http://cache.insteon.com/documentation/insteon_details.pdf) that describes the
network protocol as well as the messaging protocol.[^B-1-2]

Insteon also integrates with a number of third party devices and controllers. These third party
devices can be added to the network and be controlled through the Insteon smart hub. The hub's
devices can also be controlled through the integrations of these third party devices.[^B-1-2]

###### Device Discovery and Setup {-}

Adding a new device is done through the Insteon app. A new device is first plugged in and turned on.
The device then locates the user's mobile app on the network and is ready to be connected.
Using the app the user selects the new device and enters the device ID. Once the ID is
entered the device is able to be configured and added to the Insteon network.[^B-1-2]

###### Network {-}

Insteon uses a central hub to communicate between the devices and the users app. The Insteon hub
is used for all device communications and control. Devices connect and send all event information
to the central hub.

Insteon uses a peer-to-peer network to connect the devices.[^B-1-3] All of Insteon's devices can act as a
controller to send messages, a repeater to forward messages or a responder to receive messages.

###### API {-}

Insteon provides a REST API to interact with their devices.

| Feature                               | Supported |
| ---------                             | --------- |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |

In order to use the API approval from Insteon is required. Applying for an API key is done through
the Insteon website.[^B-1-4]

###### Limitations {-}

In order to use the API an Insteon Hub is required also adding new Insteon devices to a network
still require configuration through the Insteon App.

##### Third Party Support {-}

Insteon supports devices from the following manufacturers:

- Nest
- Logitech
- Amazon Echo
- Stringify
- Apple HomeKit
- Cortana
- First Alert
- Sonos
- MiLocks


##### Evaluation {-}

The Insteon system is very reliable and easy to setup however because they use their own
communication protocol the devices that can be added is limited mostly to those manufactured by
Insteon. A closed system such as this is not what we are striving for with this project.

#### Wink {-}

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


#### SmartThings {-}

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


#### Apple HomeKit {-}

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


