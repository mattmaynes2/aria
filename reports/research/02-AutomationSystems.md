# 2. Automation Systems

2.1 Background
--------------

There are many different home automation systems. We are looking at these other automation systems
so that we can see know what already exists on the market. Find standards that the existing systems
use. We also want to see what other systems do well so we can take this into consideration while
designing our system.

This section will concentrate on the following characteristics:

- **Supported Communication protocols**

 What different protocols do the systems support. We want to find the protocols that the other
 systems have decided are the most important to support.

- **Device Discovery/Setup**

 How are new devices added to the automation systems network.

- **Network**
 How do these systems setup the network of devices. Do they use a central server, are all devices
 independent etc..

- **API**

 Does the system provide an API that our system could potentially use to control the devices 
connected to these systems. In order to control these devices 
we require that the following; a way to view all connected devices, 
a way to get notifications when a device in the system changes states,
a way to change the state of a device.

- **Third Party Integrations**
 
 Which companies have these systems decided are important to support

<note need to rework this>

2.2 Insteon
-----------

### Description

Insteon is a home automation system that allows control of the home through a phone. The system
supports changing device states based on a schedule or through **scenes**.

A scene is configured a configuration for a room that the user sets up at a specific time or when
specific environmental conditions are met. Insteon has all of the devices remember their current
states and whenever it sees those states it has the devices recreate the saved scene.

### Technical Overview

#### Supported Communication Protocols

Insteon created their own protocol also called Insteon which is the communication system they
support (see Communication protocols section for more on information on the Insteon protocol).

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

<need to go over evaluation>

Insteon has a spec for their messaging system and command structure which would allow us to
communicate with their devices without the use of the hub, however adding the support using their
messaging and command structures  is <something here>. Adding support for Insteon devices is
something that could be looked at in the future though is outside of the scope of the project for
now.

### Refrences

[1] Apiary, "Insteon API · Apiary,". [Online]. Available: http://docs.insteon.apiary.io/.
Accessed: Oct. 6, 2016.

[2] Insteon®, "Home," in Insteon, Insteon, 2016. [Online]. Available: http://www.insteon.com/.
Accessed: Oct. 6, 2016.

[3] Insteon®, "WHITEPAPER: Compared,". [Online]. Available:
http://cache.insteon.com/documentation/insteon_compared.pdf. Accessed: Oct. 6, 2016.

[5] Insteon®, "WHITEPAPER: The Details,". [Online]. Available:
http://cache.insteon.com/documentation/insteon_details.pdf. Accessed: Oct. 6, 2016.

[4] SMARTHOME®, "Insteon home automation,". [Online]. Available:
http://www.smarthome.com/sc-what-is-insteon-home-automation. Accessed: Oct. 6, 2016.

-----------------------

2.3 Wink
--------

### Description

Wink Hub is a hub that allows connections from many different smart devices. For the most part this
system seems to provide an app that allows the user to interface with multiple different smart
devices from different manufacturers.

### Technical Overview

Wink is a central hub that supports most of the popular connection protocols so that users can
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

## Description

SmartThings is Samsung's home automation system. 

## Technical Overview

Uses Z-Wave and ZigBee and wifi.

### API
	provides a Groovy API to create SmartApps that allow control of devices.

#### Limitations

Requires a SmartThings hub and connection to the SmartThings cloud.

### Third Party Integrations

|    	   |     	       |     	      |     		|                   |
| --- 	   | --- 	       | --- 	      | --- 		| ---    	    |
|2Gig	   |Aeon Labs 	       |Amazon	      |Belkin   	| Bose 		    |	 
|Cree 	   |ecobee 	       |Ecolink       |EcoNet Controls 	| Enerwave	    |
|Everspring|Fibaro 	       |Fidure 	      |First Alert     	|FortrezZ	    |
|GE 	   |Google 	       |Honeywell     |iHome       	|Keen Home	    |
|Kwikset   |Leak Intelligence  |Leviton	      |LiFi Labs   	| Linear	    |
|Netgear   |OSO Technologies   |OSRAM LIGHTIFY|Philips Hue 	| Remotec Technology|
|Samsung   |Samsung SmartThings|Schlage       |Sengled     	| Skybell	    |
|Spruce    |Yale 	       |Zen 	      | 		| 	  	    |  

## Evaluation

How does this specific item do against our criteria?

### References

[1] "Samsung SmartThings hub FAQ — SmartThings developer documentation," 2016. [Online].
Available: http://docs.smartthings.com/en/latest/sept-2015-faq.html. Accessed: Oct. 6, 2016.

-----------------------

2.5 Lowes Iris
---------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

-----------------------

2.6 Apple HomeKit
-----------------

### Description

### Technical Overview

### References

-------------

2.7 Summary of Evaluation
-------------------------

All of the evaluation grouped together It appears that most of these systems support the NEST
thermostat with most of these systems supporting one product this would suggest that <insert market
leader statment> because our system is more about the machine learning and communication between
devices it seems to make sense to use the NEST thermostat rather than spending time creating our
own.  <reword and maybe move to nest section in devices>

These systems seem to all provide a central hub that is used to as a central device that controls
devices as well as provides an API that allows apps to control devices. This suggest that our system
should also provide a central server with an API.

<reword maybe provide better reason>


2.8 Conclusion
--------------

What did we decide upon? Why?
