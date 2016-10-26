 3. Smart Devices

3.1 Background
--------------

In the context of this project, a smart device is a device that is capable of communicating with
a computer or microcontroller using a wireless protocol, such as Wifi or Z-Wave. Each device 
provides a set of inputs and outputs which can be controlled and examined using the communication
protocol.

3.2 Relation to System
----------------------

We are looking at existing smart devices so that we can see if there are any devices that exist on
the market that our system could use in order to lower the time required to build our own. Adding
support for other smart devices also makes our system more appealing to the end user because they
are not limited to only using devices we create but can go to a store and purchase any device that
use technologies we support.

**Rough List of Attributes**

- list of inputs and outputs
- communication protocol
- developer support

3.3 WeMo
--------

### Description

WeMo is a line of smart products made by Belkin. These devices are able to be controlled over a WiFi
connection with a phone.

### Devices

WeMo have the following smart devices:
- Light switch
- Outlet switch
- Camera
- LED lights
- Slow Cooker
- Coffeemaker
- Air Purifier
- Humidifier 
- Heater


### Technical Overview


#### Communication Protocol

WeMo only supports WiFi for communicating with devices. With WeMo devices no central
hub is required in oder to be controlled, it is possible to communicate and control 
the devices directly.

WeMo uses Universal Plug And Play protocol for discovery and operating the devices.


#### API

There is a community supported open source python API for controlling WeMo devices `ouimeaux`. 
There is are also many UPnP libraries available that can allow us to communicate with the devices.


### Evaluation



### References

[1] B. International, "WeMo," WeMo, 2014. [Online]. Available:
http://www.belkin.com/whatiswemo/. Accessed: Oct. 6, 2016.

[2] "Ouimeaux 0.8: Python package index,". [Online]. Available:
https://pypi.python.org/pypi/ouimeaux. Accessed: Oct. 6, 2016.

-----------------------

3.4 Nest Thermostat 
--------

### Description

The nest thermostat is a smart learning thermostat. The thermostat 
doesn't need to be programed through use the thermostat learns the home
owner's routine and sets the temperature accordingly. It is also able 
to turn off when no one is home and be controlled remotely.

### Technical Overview

Nest communicates using WiFi and a custom nest protocol called **Nest Weave**. Nest Weave uses
WiFi and Thread.

Nest provides API support through the nest cloud. They provide access
either through using Firebase or REST.

### Evaluation


### References

[1] "Meet the nest learning thermostat," Nest Labs, 2016. [Online]. Available: https://nest.com/ca/thermostat/meet-nest-thermostat/. Accessed: Oct. 24, 2016.

[2] [Online]. Available: https://developers.nest.com/documentation/cloud/data-structure-and-access. Accessed: Oct. 24, 2016.
-----------------------

3.5 Philips Hue
---------------

### Available Devices

1. White Bulbs
Least features of all bulbs. Simple white light.
- On/Off Automation
- Dimming

2. White Ambiance Bulbs
Same features as white bulbs but the shade of white can be changed

3. Colour Ambiance Bulbs
Same features as white bulbs but the colour can be changed

4. Lightstrips
Adhesive strips of lights. 
Dimmable.
Can change colours.
Dynamic lighting/colour schemes
Can't do white

5. Lightstrip Plus
Able to do white (All light)
Brighter (1600 Lumen)
Fine fading control

6. Dimmer switch
- Battery-powered switch to dim ^hue lights
- Doesn't require the Hue bridge
- Can't use it with other AC devices, no electrical contact with bulbs

7. Tap Switch
Powered by touch - no battery or wires
Need bridge and app to set this up

### Developing with Hue

- Devices use ZigBee Light Link

- The Hue bridge is the device that allows lights to be controlled using Wifi. It bridges 
  the ZigBee protocol used by lights to Wifi used by apps.

- Bridge works with standard ZigBee lights

- Hue Bridge provides a RESTful API for controlling connected lights. API is only accessible 
  when you're on the same LAN as the bridge.

### Inputs and Outputs

There are numerous inputs and outputs possible with the Philips Hue API, I have included
ones that an end-user cares about.

#### Lights

- on/off (both)
- brightness (both)
- colour (both)
- saturation (both)

#### Sensors

- can't tell yet, need to wait for an account

[http://www.developers.meethue.com/documentation/how-hue-works]
[http://www.developers.meethue.com/]

-----------------------


3.8 Osram LIGHTIFY
------------------

### Description

LIGHTIFY is a line of lighting products which are designed to be controlled using 
the LIGHTIFY mobile app. LIGHTIFY provides two separate product lines; LIGHTIFY Pro
and LIGHTIFY Home. LIGHTIFY Pro products are designed to be highly scalable for
office environments. This research focuses on the LIGHTIFY Home line of products.

The LIGHTIFY system consists of a gateway which connects to all of the bulbs installed
in the home. Using the LIGHTIFY app, a homeowner can control connected lights from a 
mobile device.

### Available Devices

1. Surface Light TW
- Dimmable
- Adjustable colour temperature
- White only

2. Surface Light W
- Dimmable
- White only

3. Flex RGBW
- RGB colour control
- Adjustable colour temperature
- Dimmable

### Technical Overview

LIGHTIFY products use the ZigBee protocol for communication between the gateway and 
lighting products. The gateway connects to a local Wifi network, allowing the 
LIGHTIFY app to control the system over the Internet.

Due to the use of the open ZigBee protocol, LIGHTIFY products can be controlled using any 
ZigBee controller

The LIGHTIFY gateway also provides a RESTful API for controlling lights over internet. One
notable limitation of the LIGHTIFY API is that it is a cloud-only API. This means that 
the LIGHTIFY gateway is strongly tied to a homeowner's LIGHTIFY account; Osram does not 
document any local-only API for controlling devices using a gateway

Developer information [https://us.lightify-api.org]

### Evaluation

| Product     | Protocol | API Support | Developer Support | 
| ----------  | -------- | ----------- | ----------------- |
| LIGHTIFY    | ZigBee   | Cloud Only  | Limited           |
| Philips Hue | ZigBee   | Local Only  | Very good         |

-----------------------



3.10 Honeywell VisionPro Thermostat
-----------

### Description

The Honeywell VisionPro Thermostat is a regular programmable
thermostat without any *smart* features other than it is able
to be controlled through z-wave.

### Technical Overview

### Communication 

The thermostat communicates can be controlled through the
touch screen or through z-wave. 

### API

There is no API provided by Honeywell. The thermostat 
is controllable using the z-wave protocol.


### References 

[1]Honeywell. [Online]. Available: http://library.ademconet.com/MWT/fs2/5800ZBRIDGE/ZWSTAT-Dealer-Data-Sheet.pdf. Accessed: Oct. 26, 2016.

-----------------

3.12 Aeon Labs 
-----------------

### Description

Aeon Labs is a company that produces a large varity of Z-Wave devices. They also provide
the ability to create your own home automation hub.  


### Technical Overview

Aeon Labs produce a USB dongle that allows you to turn any computing device into a Z-Wave communication
hub. This hub allows the user to manually control any Z-Wave device on the Z-Wave network, and provides
the functinallity to add and remove devices to/from the network. To add a Z-Wave device, start by 
unplugging the dongle from the hub and pushing the button on it. Then walk to the new device and push the 
button on the device. The dongle must also be unplugged to remove a device from the network. To put it in 
removal mode, push and hold the button on the dongle. Then go to each device you wish to remove from the
network and push the button. The dongle can be bought for about $60.

They do not provide their own hub, which is ideal for out project. They simply allow the ability to turn
a computing device into a custom hub by providing the required RF signal to communicate with Z-Wave devices.
To begin development for Z-Wave devices, The list of Z-Wave devices from Aeon Labs alone is fairly extensive.
The list include but is not limited to: door sensors, window sensors, lights, energy meters, range extenders, 
etc. Most of these devices cost around $60 - $80. 

The specification for interacting with Z-Wave devices is public, and available at 
http://zwavepublic.com/specifications. There is also an open Z-Wave sdk available, to communicate from
the controller to devices.


### Evaluation

Aeon Labs is an ideal solution for our project. To start, there is an easy way to set up our own hub, instead
of being constrained to buying one. This allows us to implement the features we want, and add support for
protocols we want without restriction. Having access to an sdk is very important to us as well. It lets us
not be responsible for implementing the Z-Wave stack protocol, while also giving us the freedom to use the
information recieved by the devices in a unique way. Specifically, this will provide us with data for the
machine learning algorithm. 


### References

[1]	"Z-Stick 2E manual," Aeotec, Aeon Labs, 2012. [Online]. Available: http://aeotec.com/z-wave-usb-stick/913-z-stick-manual-instructions.html. Accessed: Oct. 13, 2016.

[2]	"Home automation products," in Aeotec, Aeon Labs, 2006. [Online]. Available: http://aeotec.com/homeautomation. Accessed: Oct. 13, 2016.

[3]	"OpenZWave library," in OpenZWave. [Online]. Available: http://www.openzwave.com/dev/index.html. Accessed: Oct. 13, 2016.

-----------------------

3.13 Spruce Irrigation
-----------------------

### Description

Spruce irrigation is a home plant watering automation system. The irrigation system can be used
outdoors for watering gardens, lawns or any other plant life. The Spruce system is ideal for
scheduling or automating plant watering cycles. The Spruce system also offers automation of water
based on weather conditions and soil moisture.

### Technical Overview

The Spruce irrigation system uses a combination of wireless sensors, smart sprinklers and a central
hub for controlling the watering levels of its plants. The irrigation system's central hub is
connected to each of the smart sprinklers to control the water flow. Smart sensors are then placed
in various locations on the property and communicate wirelessly to the central hub. The sensors are
placed in the ground and are battery powered.

The Spruce hub provides manual control of all the sprinklers in the system. The hub also provides a
user interface for scheduling sprinkler times and amounts. The Spruce system is also equip with
some learning software that uses weather predictions and moisture amount to optimize water use
for watering plants.

### Evaluation

The Spruce system provides integration to SmartThings but has no other public APIs. This means
that it is not accessible other systems for communication. The only option for controlling the
Spruce system would be to implement the SmartThings protocol or to attach an adapter to an
existing SmartThings Hub. This is likely onside of the scope of this project but could be
pursued if there was interest.

### References

[1] "Spruce - how it works,". [Online]. Available: http://spruceirrigation.com/How.
Accessed: Oct. 13, 2016.

[2] "Spruce irrigation controller & sensor," SmartThings Support. [Online]. Available:
https://support.smartthings.com/hc/en-us/articles/208053773-Spruce-Irrigation-Controller-Sensor.
Accessed: Oct. 13, 2016.

-----------------------

3.14 OSO PlantLink
-------------------

### Description

PlantLink is a indoor or outdoor plant monitoring and irrigation system. PlantLink uses a
simple monitoring system where sensors are placed it the target plant's soil for monitoring.
These sensors then report back to a mobile app for monitoring. PlantLink also offers an
automated valve for controlling water flow of a hose.

### Technical Overview

PlantLink sensors are low power, light weight units that can transmit data with a range of
100-300 ft. The sensor is water resistant and battery powered with an estimated one year battery
life. The sensors are used to check soil moisture of the plants they are monitoring. The sensors
then communicate to your mobile device using email, text or push notifications.

PlankLink also offers a smart valve system for controlling water flow of a hose. The valve system
is solar powered and can be controlled from the PlankLink mobile app. The valve can also
communicate directly to senors to automate the watering of plants. In this mode, if a sensor
reports that the soil is dry then the valve will open up and water the plants.


### Evaluation

PlantLink is compatible with other platforms but does not offer open source access to its APIs.
PlantLink can communicate with SmartThings, Iris, greenIQ and GRO automation systems. To be
able to integrate with this system we would need to interface through one of these other systems
as an intermediary. The PlantLink system may be outside of the scope of this system unless
there we plan on integrating with another smart system

### References

[1] "PlantLink," PlantLink, 2016. [Online]. Available: https://myplantlink.com/in-action.
Accessed: Oct. 13, 2016.

-----------------------


3.17 Summary of Evaluation
--------------------------

All of the evaluation grouped together

### Resources

[1] R. Crist, "Best smart home devices of 2016," CNET, 2016. [Online]. Available:
https://www.cnet.com/topics/smart-home/best-smart-home-devices/. Accessed: Oct. 6, 2016.

3.18 Conclusion
---------------

What did we decide upon? Why?
