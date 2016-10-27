# 2. Automation Systems

2.1 Background
--------------

In this section we are looking at existing systems so that we can better understand what technologies currently 
exist in the market. Having a better grasp of existing technology will help us understand how we can differentiante 
our smart home automation system. In particular, we are interested in which features are common in home automation
systems and their benifits to the end user. 

An important aspect of our project is to have custom logic for controlling smart devices in a home automation system.
Existing systems implement their own logic, so we will not be using them directly. Looking at existing systems gives us 
a better understanding of what the end user expects of home automation, allowing us to better design our own system.

The research will investigate the following characteristics of existing home automation systems:

- **Supported Communication protocols**

 Which protocols does the system support?

- **Device Discovery/Setup**

 How are new devices added to the system's network?

- **Network**
 
 How do these systems setup the network of devices. Do they use a central server, are all devices
 independent etc..

- **API**

 Does the system provide an API that our system could use to control the connected devices? 
 In order to control these devices we require the following:
 - a way to view all connected devices 
 - a way to get notifications when a device in the system changes states
 - a way to change the state of a device

- **Third Party Integrations**
 
 How much third party support does this company have?


2.2 INSTEON
-----------

### Description

INSTEON is an automation system that allows control of the home through a smart phone. 
INSTEON supports controlling devices based on a schedule, using IFTTT or through setting 
up **scenes**.

A scene is a user defined configuration for a room that has a trigger. A trigger can be a 
specific time or be when specific environmental conditions are met. When triggered, the system
will set the environment of the room according to the scene.  

### Technical Overview

#### Supported Communication Protocols

INSTEON created their own protocol also called [INSTEON](#4.4-INSTEON) which is the communication 
protocol they support.

#### Device Discovery/ Setup

Adding a new device is done through the INSTEON app. When a new device is introduced, it is automatically
discovered by the system. The user selects the new device using the INSTEON app and enters the device ID.
After the ID is entered the device is able to be configured and controlled by the system.

#### Network

INSTEON uses a central hub to facilitate communication across the system. The central hub is
required in order for the system to work, meaning INSTEON devices cannot function independent
of the hub.

INSTEON uses a peer-to-peer network, connecting devices to other devices. This allows any INSTEON
device to act as a controller to send messages, a repeater to forward messages, or a receiver
to receive messages.

#### API

INSTEON provides a REST API to interact with their devices. 

| Feature                                | supported |
| ---------                              | --------  |
| List all devices                       |    Y      |
| Receive update on device state change  |    Y      |
| Modify device state                    |    Y      |

In order to use the API approval from INSTEON is required. Applying
for an API key is done through the INSTEON website.

### Third Party Support

INSTEON supports devices from the following manufacturers:

- Nest
- Amazon Echo
- logitech
- first Alert
- Sonos 
- MiLOCKS
- Apple HomeKit

### Evaluation

The INSTEON system is reliable and easy to setup, but is limited by having their own communication
protocol. This limits the devices that can be added to the system, as they are largly only manufactured 
by INSTEON. A closed system such as this is not what we are striving for with this project.

### Refrences

[1] Apiary, "INSTEON API · Apiary,". [Online]. Available: http://docs.insteon.apiary.io/.
Accessed: Oct. 6, 2016.

[2] INSTEON®, "Home," in INSTEON, INSTEON, 2016. [Online]. Available: http://www.insteon.com/.
Accessed: Oct. 6, 2016.

[3] INSTEON®, "WHITEPAPER: Compared,". [Online]. Available:
http://cache.insteon.com/documentation/insteon_compared.pdf. Accessed: Oct. 6, 2016.

[5] INSTEON®, "WHITEPAPER: The Details,". [Online]. Available:
http://cache.insteon.com/documentation/insteon_details.pdf. Accessed: Oct. 6, 2016.

[4] SMARTHOME®, "INSTEON home automation,". [Online]. Available:
http://www.smarthome.com/sc-what-is-insteon-home-automation. Accessed: Oct. 6, 2016.

-----------------------

2.3 Wink
--------

### Description

Wink Hub is a hub that specializes in allowing communication between many different smart devices.
Wink supports control of devices using scheduling and IFTTT. 

### Technical Overview

Wink is a central hub that supports most of the popular communication protocols for home automation,
giving users the freedom of connecting and controlling a variety of smart devices in one system.

#### Communication Protocol

Wink Hub supports the following communication protocols:

- Wifi
- Bluetooth smart (BLE)
- Z-Wave Plus
- ZigBee
- Lutron's Caseta
- Kidde

#### Device Discovery/Setup

Supporting many different manufacturers means that there are a 
variety of different ways for devices to connect to the Wink Hub.
The two most common ways are:

1) Button Pressing 
Pressing a button on the Wink Hub broadcasts a pairing signal across the network.
Any new device that recieves this signal will then appear on the network, and
can be viewed from the Wink app. The user then selects the new device and enters
the device ID (located on the physical device) to add it to the automation system. 

2) Manufacturer Setup
The new device must be added to the home network using the app provided by the manufacturer.
Once it has been added through the manyfacturers app, it will be visible using the Wink
app. It can be added to the automation system from here using the Wink app.

#### Network

The Wink system uses a central hub to connects different devices. Devices communicate only 
with the central hub.

#### API

Wink provides a RESTful service through the Wink hub and a secondary
partner PubNub. 

| Feature                                | supported |
| ---------                              | --------  |
| List all devices                       |    Y      |
| Receive update on device state change  |    Y      |
| Modify device state                    |    Y      |

#### Third Party Integrations

Wink has support for the following manufacturers:

|           |             |                     |             |         |
| ---       | ---         | ---                 | ---         | ---     |
| Nest      | Philips     | GE                  | Leviton     | Rheem   |
| Honeywell | TCP         | Kidde               | Kwiset      | Lutron  |
| Rachio    | Bali        | Amazon              | Andersen    | Canary  |
| Carrier   | Chamberlain | Commercial Electric | Cree        | Dropcam |
| Ecobee    | Emerson     | GoControl           | Hampton Bay | IHome   |
| Leaksmart | Osram       |                     |             |         |


### Evaluation

Providing support for the most popular communication protocols allows Wink
to connect with almost any device a user can purchase, making them an
attractive option to consumers. This is a feature that we hope to mimic,
although not to the full extent of Wink. Specifically, the methods of connecting
devices from any manufacturer will likely be useful to us for this project.

### References

[1] Apiary, "Wink API · Apiary,". [Online]. Available:
http://docs.winkapiv2.apiary.io/#reference/oauth/obtain-access-token.
Accessed: Oct. 9, 2016.

[2] "Wink FAQ - Wink@Home Wiki," 2015. [Online]. Available: http://wiki.winkathome.net/Wink_FAQ.
Accessed: Oct. 6, 2016.

[3] Wink, "A simpler smart home," Wink, 2016. [Online]. Available: http://www.wink.com/help/faq/.
Accessed: Oct. 8, 2016.

-----------------------

2.4 SmartThings
---------------

### Description

SmartThings is Samsung's home automation system. Similar to  Wink, they provide their
own app allowing a user to control devices using scheduling or IFTTT.

### Technical Overview

#### Communication Protocols 
    
SmartThings supports devices that communicate using the Z-Wave, ZigBee, or WiFi 
communication protocols

#### Device Discovery/Setup
Adding a new device is done through the app. A user will click "find device", prompting the hub
to search for any new Z-Wave, ZigBee, or WiFi devices. When the device is found the user adds 
it to a room and names the device.


### Network

SmartThings uses a central Hub to connect all of the smart devices. The SmartThings
app talks with the SmartThings Cloud which talks to the Hub which then controls the 
devices.

#### API

	provides a Groovy API to create SmartApps that allow control of devices.


| Feature                                | supported |
| ---------                              | --------  |
| List all devices                       |    Y      |
| Receive update on device state change  |    Y      |
| Modify device state                    |    Y      |


#### Limitations

Requires a SmartThings hub and connection to the SmartThings cloud.

### Third Party Integrations

|    	   |     	            |     	        |     		     |                      |
| --- 	   | --- 	            | --- 	        | --- 		     | ---    	            |
|2Gig	   |Aeon Labs 	        |Amazon	        |Belkin   	     | Bose 		        |	 
|Cree 	   |ecobee 	            |Ecolink        |EcoNet Controls | Enerwave	            |
|Everspring|Fibaro 	            |Fidure 	    |First Alert     | FortrezZ	            |
|GE 	   |Google 	            |Honeywell      |iHome       	 | Keen Home            |
|Kwikset   |Leak Intelligence   |Leviton	    |LiFi Labs       | Linear	            |
|Netgear   |OSO Technologies    |OSRAM LIGHTIFY |Philips Hue 	 | Remotec Technology   |
|Samsung   |Samsung SmartThings |Schlage        |Sengled     	 | Skybell	            |
|Spruce    |Yale 	            |Zen            | 		         |          	  	    |  

### Evaluation

The Samsung home automation system provides a reasonable level of support for
different communication protocols, giving it a healthy amount of third party support.
This is something that we will be striving for in out project. The dependency on the 
connection to a cloud service is something that we would like to avoid for our project.

### References

[1] "Samsung SmartThings hub FAQ — SmartThings developer documentation," 2016. [Online].
Available: http://docs.smartthings.com/en/latest/sept-2015-faq.html. Accessed: Oct. 6, 2016.

[2] SmartThings, "How it works," SmartThings, 2016. [Online]. 
Available: https://www.smartthings.com/how-it-works. Accessed: Oct. 10, 2016.

-----------------------

2.5 Apple HomeKit
-----------------

### Description

Apple HomeKit allows users to control their smart devices 
using their IPad or IPhone. Apple HomeKit does not require any 
central hub to control the devices, but does require there to be 
Apple device connected to the network at all times. If a user wants to 
control devices with an IPhone while not at home, the devices must be 
connected to an Apple product that is connected to the network, such as 
an Ipad or apple TV.


### Technical Overview

The smart devices are able to be scheduled and controlled in groups from the app.
ex. All the lights in the living room turn off at 11:00 pm.

#### Communication Protocol

Apple HomeKit uses Wifi as the only communication protocol.

#### Device Discovery/Setup

Adding new devices is done through the app. Once a device is connected to the network
it can be added to the home through Apple's app, some devices require some configuration
in their manufacturers apps.

#### Network

HomeKit uses the homes wifi network to connect devices and all devices on the network are 
able to communicate with one another.

#### API

| Feature                                | supported |
| ---------                              | --------  |
| List all devices                       |    Y      |
| Receive update on device state change  |    Y      |
| Modify device state                    |    Y      |

### Evaluation

There are a few aspecs of the Apple HomeKit that are not ideal for incorperation into 
our project. First, it is Apple excluse, which goes against the goal of having many
third party support options. The lack of a central hub also makes it difficult to 
having support for many different types of devices. The level of communication
between devices that is offered by the Apple solution is a desirable feature,
but will be difficult to achieve while maintaining diverse third party support.


### References

[1] "Use the home app on your iPhone, iPad, and iPod touch," Apple Support, 2016. [Online]. 
Available: https://support.apple.com/en-ca/HT204893. Accessed: Oct. 10, 2016.

[2] Apple, "Creating homes and adding accessories," 2016. [Online]. 
Available: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/
HomeKitDeveloperGuide/WritingtotheHomeKitDatabase/WritingtotheHomeKitDatabase.html#//apple_ref/doc/uid/TP40015050-CH4-SW1. Accessed: Oct. 10, 2016.

[3] E. Betters, "Apple HomeKit and home app: What are they and how do they work?," Pocket-lint, 2016. [Online]. Available: 
http://www.pocket-lint.com/news/129922-apple-homekit-and-home-app-what-are-they-and-how-do-they-work. Accessed: Oct. 10, 2016.

-------------

2.7 Summary of Evaluation
-------------------------

A common theme among existing home automation systems is that systems with a large amount of
third party support rely on a central communication hub. Having a hub allows components from
different manufacturers to communicate to each other through the hub. A challenge that supporting
a large number of devices presents is how to discover new devices into a system, which can be delt
with in several different ways such as manual button pressing or app configuration. 

Looking at these systems also presented several communcation protocols to investigate, including
Z-wave, Zigbee, Insteon and WiFi. Along side these are devices from many different manufacturers 
which operate using these communication protocols. Deciding on a communicaiton protocol and 
subsequent device manufactures to support is an important part of our design for our home
automation system.


