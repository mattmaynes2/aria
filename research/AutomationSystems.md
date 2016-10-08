Automation Systems
=============

### Background

There are many different home automation systems. We are looking at
these other automation systems so that we can see know what 
already exists on the market. Find standards that the existing 
systems use. We also want to see what other systems do well so
we can take this into consideration while designing our system.

This section will concentrate on the following characteristics:

- **Supported Communication protocols**

 What different protocols do the systems support. We want
 to find the protocols that the other systems have decided
 are the most important to support.

- **Device Discovery/Setup**

 How are new devices added to the automation systems network.

- **Home Network (Design, layout, configuration?)** <need to pick name>

 How do these systems setup the network of devices. Do they use a 
 central server, are all devices independent etc..

- **API**

 Does the system provide an API that our system could potentially use
 to control the devices from these systems.


<note need to rework this>



Insteon
------------

### Description

Insteon is a home automation system that allows control of the home 
through a phone. The system supports changing device states based 
on a schedule or through **scenes**. 

A scene is configured a configuration for a room that the user 
sets up at a specific time or when specific environmental 
conditions are met. Insteon has all of the devices remember their
current states and whenever it sees those states it has the devices
recreate the saved scene.

## Technical Overview

#### Supported Communication Protocols

Insteon created their own protocol also called Insteon 
which is the communication system they support (see Communication
protocols section for more on information on the Insteon protocol).

#### Device Discovery/ Setup

Adding a new device is done through the Insteon app. The device is
automatically discovered by the system. Using the app the user
selects the new device and enters the device ID after the ID is 
entered the device is able to be configured, naming the device 
adding it to a room etc.. 

#### Network

Insteon uses a central hub to communicate between the devices and
the users app.The central hub is required in order for the system
to work (can't use Insteon devices individually).

Insteon uses a peer-to-peer network to connect the devices. All of 
Insteon's devices can act as a controller to send messages, a 
repeater to forward messages or a responder to receive messages.

#### API 

 Insteon provides a REST API to interact with their devices. 
 The API provides supports adding devices, 
 
###### Limitations 
 
 In order to use the API an Insteon Hub is required also adding new 
 Insteon devices to a network still require configuration through the
 Insteon App.

## Evaluation

Issue with integrating with insteon using their API is that it
requires their central hub. Their hub system does most of what we 
want our system to do and we ould like to learn how to do this
rather than just use someone elses.

Insteon has a spec for their messageing system and command structure
which would allow us to communicate with their devices without the 
use of the hub, however adding the support using their messageing and
command structures  is <something here>. Adding support for Insteon
devices is something that could be looked at in the future though 
is outside of the scope of the project for now.

## Refrences

[1]	Apiary, "Insteon API · Apiary,". [Online]. Available: http://docs.insteon.apiary.io/. Accessed: Oct. 6, 2016.

[2]	Insteon®, "Home," in Insteon, Insteon, 2016. [Online]. Available: http://www.insteon.com/. Accessed: Oct. 6, 2016.

[3] Insteon®, "WHITEPAPER: Compared,". [Online]. Available: http://cache.insteon.com/documentation/insteon_compared.pdf. Accessed: Oct. 6, 2016.

[5] Insteon®, "WHITEPAPER: The Details,". [Online]. Available: http://cache.insteon.com/documentation/insteon_details.pdf. Accessed: Oct. 6, 2016.

[4] SMARTHOME®, "Insteon home automation,". [Online]. Available: http://www.smarthome.com/sc-what-is-insteon-home-automation. Accessed: Oct. 6, 2016.

-----------------------

Wink
------------

### Description

Wink Hub is a hub that allows connections from many different smart devices. For the most part
this system seems to provide an app that allows the user to interface with multiple different
smart devices from different manufacturers.

### Technical Overview

Wink Hub supports the following communication protocols:
- Wifi
- Bluetooth smart (BLE)
- Z-Wave Plus
- ZigBee
- Lutron's Caseta
- Kidde


### Evaluation

This system supports multiple 

### References

[1]	"Wink FAQ - Wink@Home Wiki," 2015. [Online]. Available: http://wiki.winkathome.net/Wink_FAQ. Accessed: Oct. 6, 2016.

-----------------------

SmartThings
------------

### Description

What is this item?

### Technical Overview

Uses Z-Wave and ZigBee and wifi.

### API
	provides a Groovy API to create SmartApps that allow control of devices.

#### Limitations

requires a SmartThings hub and connection to the SmartThings cloud.

### Evaluation

How does this specific item do against our criteria?

### References

[1]	"Samsung SmartThings hub FAQ — SmartThings developer documentation," 2016. [Online]. Available: http://docs.smartthings.com/en/latest/sept-2015-faq.html. Accessed: Oct. 6, 2016.

-----------------------

Lowes Iris
------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

-----------------------

Apple HomeKit
-------------

## Description

## Technical Overview

## References

-------------

### Summary of Evaluation

All of the evaluation grouped together
It appears that most of these systems support the NEST thermostat
with most of these systems supporting one product this would 
suggest that <insert market leader statment> because our system
is more about the machine learning and communication between
devices it seems to make sense to use the NEST thermostat
rather than spending time creating our own.
<reword and maybe move to nest section in devices>

These systems seem to all provide a central hub that is used
to as a central device that controls devices as well as provides
an API that allows apps to control devices. This suggest that 
our system should also provide a central server with an API.

<reword maybe provide better reason>


### Conclusion

What did we decide upon? Why?
