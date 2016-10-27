# 2. Automation Systems

2.1 Background
--------------

In this section we are looking at existing systems so that we can better understand what
technologies currently  exist in the market. Having a better grasp of existing technology will help
us understand how we can differentiante  our smart home automation system. In particular, we are
interested in which features are common in home automation systems and their benifits to the end
user. 

An important aspect of our project is to have custom logic for controlling smart devices in a home
automation system. Existing systems implement their own logic, so we will not be using them
directly. Looking at existing systems gives us a better understanding of what the end user expects
of home automation, allowing us to better design our own system.

The research will investigate the following characteristics of existing home automation systems:

##### Supported Communication protocols

Which protocols does the system support? If there are common protocols across all main automation
systems then they should be considered for this system. Industry standard protocols may be
discovered by reviewing these existing systems.

##### Device Discovery/Setup

How are new devices added to the system's network? If there is a special focus on the ease of use
then this system should consider the efforts that other systems have taken.

##### Network
 
How do these systems setup the network of devices. Do they use a central server, are all devices
independent? The network configuration of a system will govern its performance, power consumption
and allowable number of connections. This research will investigate how these systems organize
their network topologies to satisfy these quality attributes.

##### API

Does the system provide an API that our system could potentially use to control the devices
connected to these systems. In order to control these devices we require that the following; a way
to view all connected devices, a way to get notifications when a device in the system changes
states, a way to change the state of a device.

##### Third Party Integrations

Which companies have these systems decided are important to support? If there are accepted standards
of third party integrations then this system should consider them in its design to maximize overall
interoperability.


2.2 Insteon
-----------

### Description

Insteon is a home automation system that allows smart devices to connect over a home area network
with a focus on ease of use. Insteon allows you to monitor and control all of the devices within
the system. All devices in connect through a central Insteon smart hub which is then controlled
by the user through a app on the user's mobile device. Controlling of devices can also be automated
using manually configured schedules, IFTTT or 
through the use of **scenes**. 

A scene is configured a configuration for a room that the user sets up at a specific time or when
specific environmental conditions are met. Insteon has all of the devices remember their current
states and whenever these states are met then it has the devices recreate the saved scene.

### Technical Overview

#### Supported Communication Protocols

Insteon has a proprietary self titled [Insteon](#4.4-Insteon). This protocol is used for device 
communication.

#### Device Discovery/ Setup

Adding a new device is done through the Insteon app. The device is automatically discovered by the
system. Using the app the user selects the new device and enters the device ID after the ID is
entered the device is able to be configured, naming the device adding it to a room etc..

#### Network

Insteon uses a central hub to communicate between the devices and the users app.The central hub is
required in order for the system to work (can't use Insteon devices individually).

Insteon uses a peer-to-peer network to connect the devices. All of Insteon's devices can act as a
controller to send messages, a repeater to forward messages or a responder to receive messages.

#### API

Insteon provides a REST API to interact with their devices. 

| Feature                                | supported |
| ---------                              | --------  |
| List all devices                       |    Y      |
| Receive update on device state change  |    Y      |
| Modify device state                    |    Y      |

In order to use the API approval from Insteon is required. Applying
for an API key is done through the Insteon website.

###### Limitations

In order to use the API an Insteon Hub is required also adding new Insteon devices to a network
still require configuration through the Insteon App.

### Third Party Support

Insteon supports devices from the following manufacturers:

- Nest
- Amazon Echo
- logitech
- first Alert
- Sonos 
- MiLOCKS
- Apple HomeKit

### Evaluation

The Insteon system is very reliable and easy to setup however because they use their own
communication protocol the devices that can be added is limited mostly to those manufactured by 
Insteon.

### References

[1] Apiary, "Insteon API · Apiary,". [Online]. Available: http://docs.Insteon.apiary.io/.
Accessed: Oct. 6, 2016.

[2] Insteon®, "Home," in Insteon, Insteon, 2016. [Online]. Available: http://www.Insteon.com/.
Accessed: Oct. 6, 2016.

[3] Insteon®, "WHITEPAPER: Compared,". [Online]. Available:
http://cache.Insteon.com/documentation/Insteon_compared.pdf. Accessed: Oct. 6, 2016.

[4] Insteon®, "WHITEPAPER: The Details,". [Online]. Available:
http://cache.Insteon.com/documentation/Insteon_details.pdf. Accessed: Oct. 6, 2016.

[5] SMARTHOME®, "Insteon home automation,". [Online]. Available:
http://www.smarthome.com/sc-what-is-Insteon-home-automation. Accessed: Oct. 6, 2016.


-----------------------

2.3 Wink
--------

### Description

Wink Hub is a hub that allows connections from many different smart devices. Wink supports
control of devices using scheduling and IFTTT. 

### Technical Overview

6Wink is a central hub that supports most of the popular connection protocols so that users can
connect and control a variety of smart devices from different vendors in one app.

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

1) Pressing a button on the Wink Hub to start transmitting a pairing
signal and the new device will receive the signal and connect to the
Hub. 

2) The device needs to be setup in the manufacturers app once
this is done the device can be added to Wink through the Wink app.

#### Network

The Wink system is a central hub that connects different devices.  All of the different devices are
controlled through the central hub.

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
to connect with almost any device a user can purchase. This makes them more
attractive to consumers.

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

SmartThings is Samsung's home automation system. The System provides a 
hub that connects smart devices together. These devices are able to be controlled through
the SmartThings App. The app supports controlling devices using a schedule or using IFTTT.

### Technical Overview

#### Communication Protocols 
    
    - Z-wave
    - Zigbee
    - Wifi


#### Device Discovery/Setup
 Adding a new device is done through the app. A user will click "find device" the hub will
 then search for new z-wave and zigbee devices. After the device is found the user adds 
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
using their IPad or IPhone. Apple HomeKit doesn't require any 
central hub however if a user wants to control devices when not 
at home their needs to be an Apple device in the home that the devices are
connected to, this device can be an Ipad or apple TV.


### Technical Overview

The smart devices are able to be scheduled and controlled in groups from the app.
ex. All the lights in the living room turn off at 11:00 pm.

#### Communication Protocol

Apple HomeKit uses Wifi as the communication protocol,

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

Looking at these systems we found that we should research the
Z-wave, Zigbee, Insteon and Wifi communication protocols. We 
also found some manufacturers that are commonly supported that we 
should look at, in order to potentially provide support for their 
devices.


