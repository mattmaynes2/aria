Automation Systems
=============

### Background

There are many different 

### Relation to System

We are looking at other homew automation systems so that we can see if there are any devices
that exist on the market that our system could use in order to lower the time required to build our own.
Adding support for other smart devices also makes our system more appealing to the end user because
they are not limited to only using devices we create but can go to a store and purchase any device
that from supported vendors. 

<note need to rework this>



Insteon
------------

## Description

Insteon is a home automation system that allows control of the home through a phone. 
The system 

## Technical Overview

Technically speaking, what does this item do?
Insteon has a line of smart sensors and devices that using their hub. 

### Insteon Hub

The hub is a central device that connects to all of the Insteon devices sending commands 
and monitoring sensor states. The hub is able to schedule devices to turn on and off  

### Insteon devices

Insteon supports control of:

- lights
- outlets
- thermostats
- cameras 


Insteon uses a peer-to-peer network to connect the devices. All of Insteon's devices
can act as a controller to send messages, a repeater to forward messages or a responder to receive messages

### API 

 Insteon provides a REST API to interact with their devices. 
 The API provides supports adding devices, 
 
 #### Limitations 
 
 In order to use the API an Insteon Hub is required also adding new Insteon devices to 
 a network still require configuration through the Insteon App.

## Evaluation

How does this specific item do against our criteria?

Issue with integrating with insteon using their API is that it requires their central hub. 
Their hub system does most of what we want our system to do and we ould like to learn how to 
do this rather than just use someone elses.

Insteon has a spec for their messageing system and command structure which would
allow us to communicate with their devices without the use of the hub, however adding 
the support using their messageing and command structures  is <something here>. 
Adding support for Insteon devices is something that could be looked at in the future though 
is outside of the scope of the project for now.

## Refrences

[1]	Apiary, "Insteon API · Apiary,". [Online]. Available: http://docs.insteon.apiary.io/. Accessed: Oct. 6, 2016.
[2]	Insteon®, "Home," in Insteon, Insteon, 2016. [Online]. Available: http://www.insteon.com/. Accessed: Oct. 6, 2016.
[3] Insteon®, "WHITEPAPER: Compared,". [Online]. Available: http://cache.insteon.com/documentation/insteon_compared.pdf. Accessed: Oct. 6, 2016.
[4] SMARTHOME®, "Insteon home automation,". [Online]. Available: http://www.smarthome.com/sc-what-is-insteon-home-automation. Accessed: Oct. 6, 2016.
-----------------------

Wink
------------

## Description

Wink Hub is a hub that allows connections from many different smart devices. For the most part
this system seems to provide an app that allows the user to interface with multiple different
smart devices from different manufacturors.

## Technical Overview

Wink Hub supports the following comunication protocols:
- Wifi
- Bluetooth smart (BLE)
- Z-Wave Plus
- ZigBee
- Lutron's Caseta
- Kidde


## Evaluation

This system supports multiple 

## References

[1]	"Wink FAQ - Wink@Home Wiki," 2015. [Online]. Available: http://wiki.winkathome.net/Wink_FAQ. Accessed: Oct. 6, 2016.

-----------------------

SmartThings
------------

## Description

What is this item?

## Technical Overview

Technically speaking, what does this item do?

## Evaluation

How does this specific item do against our criteria?

-----------------------

Lowes Iris
------------

## Description

What is this item?

## Technical Overview

Technically speaking, what does this item do?

## Evaluation

How does this specific item do against our criteria?

-----------------------


### Summary of Evaluation

All of the evaluation grouped together

### Conclusion

What did we decide upon? Why?
