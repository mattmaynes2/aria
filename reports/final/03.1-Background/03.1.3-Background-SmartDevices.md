# 3. Smart Devices

3.1 Background
--------------

In the context of this project, a smart device is a device that is capable of communicating over
a wireless computer network, such as WiFi or Z-Wave. Each device provides a set of inputs and outputs
which can be controlled and examined using some protocol.

3.2 Relation to System
----------------------

This section examines several commercial smart device products which are available off-the-shelf.
The goal of this research is to determine what types of devices are commercially available, and 
to compare alternative products which have similar functionality. By purchasing off-the-shelf smart
devices, the development time for the project can be focused on building the machine learning features
which differentiate our product from many existing automation systems. An awareness of existing 
smart devices will also allow us to select common technologies to support in the system. Support for 
support for commercial smart devices makes our system more appealing to the end user because they
are not limited to only using devices we create.

Where possible, research will focus on answering the following questions about a product or
line of products:

- What inputs and outputs does the device have? What type of information can the device provide to 
the machine learning algorithm, and what can be controlled?

- Which communication protocol(s) are supported by the device?

- Are the interfaces used to communicate with the device well-documented? Are there tutorials and SDKs
available?

- What restrictions does the device introduce to the system? For example, do users need to create an
account with another company in order to use the device with our system?

3.3 WeMo
--------

### Description

WeMo is a line of smart devices made by Belkin. WeMo devices can be controlled over a WiFi connection
using a smartphone app.

### Available Devices

1. Light switch
 - On/Off

2. Outlet switch
 - On/Off

3. Camera
 - On/Off
 - Motion detection

4. LED lights
 - On/Off
 - Dimming

5. Slow Cooker
 - On/Off
 - Temperature Control

6. Coffeemaker
 - On/Off
 - Brew status
 - Change filter

7. Air Purifier
 - Fan speed
 - Ionizing On/Off
 - Filter life
 
8. Humidifier 
 - Humidity level
 - Water status
 - Filter status

9. Heater
 - On/Off
 - Temperature
 - Power level

### Technical Overview


#### Communication Protocol

WeMo only supports WiFi for communicating with devices. No central hub is required in order to 
control WeMo devices, each device connects to a WiFi network directly.

WeMo uses Universal Plug And Play (UPnP) protocol for discovery and operating the devices.


#### Developing with WeMo

- *ouimeaux* is an Open source python API for controlling WeMo devices.
- WeMo devices can be controlled using UPnP. This allows us to implement one protocol and comunicate with 
all WeMo devices as well as any other smart devices from other vendors that use UPnP.

### Research Criteria

All WeMo Devices

| Inputs | Outputs | Developer Support | Protocol | API Restrictions    |
| ------ | ------- | ----------------- | -------- | ----------------    |
| On/Off | On/Off  | ouimeaux library  | WiFi     | Local Only          |
|        |         |                   | UPnP     | We need to Write it |


### References

<cite>
[1] B. International, "WeMo," WeMo, 2014. [Online]. Available:
<http://www.belkin.com/whatiswemo/>. Accessed: Oct. 6, 2016.
</cite>

<cite>
[2] "Ouimeaux 0.8: Python package index,". [Online]. Available:
<https://pypi.python.org/pypi/ouimeaux>. Accessed: Oct. 6, 2016.
</cite>

-----------------------

3.4 Nest Thermostat 
--------

### Description

The Nest thermostat is a smart learning thermostat. Over time  the thermostat learns the
homeowner's routine and adjusts the temperature accordingly. The thermostat also turns off
automatically when it detects that nobody is home, and can be remotely controlled using a
smartphone app.

### Technical Overview

Nest communicates using WiFi and a custom nest protocol called **Nest Weave**. Nest Weave uses
WiFi and the Thread protocol.

Nest provides API support through the nest cloud. The API is accessed as a RESTful service or
using Firebase.

### Evalutaion

The nest thermostat already has some machine learning on it. Trying to control it using our
algorithm could cause unexpected results. They also require the use of a cloud API to control
the thermostat and we are trying to avoid this and communicate locally with our devices. Due to
these resons it seems like the nest thermostat is not a great fit for our system and we should
not invest time into integrating with it.

### References

<cite>
[1] "Meet the nest learning thermostat," Nest Labs, 2016. [Online]. Available: 
<https://nest.com/ca/thermostat/meet-nest-thermostat/>. Accessed: Oct. 24, 2016.
</cite>

<cite>
[2] [Online]. Available:
<https://developers.nest.com/documentation/cloud/data-structure-and-access>.
Accessed: Oct. 24, 2016.
</cite>

-----------------------

3.5 Honeywell VisionPro Thermostat
-----------

### Description

The Honeywell VisionPro Thermostat is a smart programmable thermostat which can be controlled
using the Z-Wave protocol. Unlike the Nest thermostat, the VisionPro does not include learning
features.

### Technical Overview

### Communication 

The thermostat communicates can be controlled through the touch screen or through Z-Wave. 

### API

There is no API provided by Honeywell. The thermostat is controllable using the Z-Wave protocol.

### Evaluation

This is a simple thermostat that will be easy to control using Z-Wave and as it doesn't have any
learning on it, so there won't be any conflicts with our system.

### References 

<cite>
[1] Honeywell. [Online]. Available:
<http://library.ademconet.com/MWT/fs2/5800ZBRIDGE/ZWSTAT-Dealer-Data-Sheet.pdf>.
Accessed: Oct. 26, 2016.
</cite>

-----------------


3.6 Philips Hue
---------------

### Available Devices

1. White Bulbs
 - On/Off 
 - Dimming


2. White Ambiance Bulbs
 - On/Off
 - Dimming
 - Supports multiple shades of white

3. Colour Ambiance Bulbs
 - On/Off
 - Dimming
 - Configurable colour

4. Lightstrips
 - Adhesive strips of LED lights
 - Dimming
 - Configurable colours
 - Dynamic lighting/colour schemes
 - White light not supported

5. Lightstrip Plus
 - Adhesive strips of LED lights
 - Dimming
 - Configurable colours
 - Dynamic lighting/colour schemes
 - Supports white light
 - Brighter than regular Lightstrips (1600 Lumen)
 - Fine-grained fading control

6. Dimmer switch
 - Battery-powered
 - Doesn't require the Hue bridge
 - Can't use it with other AC devices, no electrical contact with bulbs

7. Tap Switch
 - Powered by touch - no battery or wires
 - Hue bridge and app required

8. Hue Motion Sensor
 - Detects motion in the vicinity of a PIR sensor
 - Includes an integrated daylight sensor


### Developing with Hue

- Devices use ZigBee Light Link

- The Hue bridge is a hub device that allows lights to be controlled using WiFi. It bridges 
  the ZigBee protocol used by lights to Wifi used by apps.

- Bridge works with most standard ZigBee lights

- Hue Bridge provides a RESTful API for controlling connected lights. API is only accessible 
  when you're on the same LAN as the bridge.

### Research Criteria

Inputs and outputs differ by device type; developer support, communication protocol, and API restrictions
are common to all Philips Hue devics.

**Hue Lights**

| Inputs             | Outputs            | Developer Support                | Protocol | API Restrictions        |
| ------             | -------            | -----------------                | -------- | ----------------        |
| On/Off             | On/Off             | Tutorials on Hue website         | ZigBee   | Local Only              |
| Brightness         | Brightness         | Android, Java, IOS Official SDKs |          | REST API requires a hub |
| Hue                | Hue                | Numerous 3rd party SDKs          |          |                         |
| Saturation         | Saturation         |                                  |          |                         |
| Colour Temperature | Colour Temperature |                                  |          |                         |
| Dynamic Effect     | Dynamic Effect     |                                  |          |                         |

**Hue Motion Sensor**

| Inputs             | Outputs             |
| ------             | -------             |
| sensitivity        | presence            |
|                    | light level         |

**Hue Dimmer Switch, Hue Tap**

| Inputs             | Outputs             |
| ------             | -------             |
|                    | button event        |

## References
<cite>
[1]	"Philips hue API," 2014. [Online]. Available: http://www.developers.meethue.com/philips-hue-api. Accessed: Oct. 29, 2016.
</cite>

<cite>
[2]	P. L. B, "Philips hue,". [Online]. Available: http://www2.meethue.com/en-ca/. Accessed: Oct. 29, 2016.
</cite>

3.7 Osram LIGHTIFY
------------------

### Description

LIGHTIFY is a line of lighting products which are can be controlled using 
the LIGHTIFY mobile app. LIGHTIFY provides two separate product lines; LIGHTIFY Pro
and LIGHTIFY Home. LIGHTIFY Pro products are designed to be highly scalable for
office environments. This research focuses on the LIGHTIFY Home line of products.

The LIGHTIFY system consists of a gateway device which connects to all of the bulbs installed
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

### Research Attributes

| Inputs                    | Outputs            | Developer Support    | Protocol | API Restrictions                   |
| ------                    | -------            | -----------------    | -------- | ----------------                   |
| on/off                    | on/off             | REST API description | ZigBee   | REST API is Cloud Only             |
| colour                    | colour             | Sample Application   |          | REST API requires LIGHTIFY account |
| colour temperature        | colour temperature | No Official SDKs     |          | REST API requires a hub            |
| brightness                | brightness         |                      |          |                                    |
| saturation                | saturation         |                      |          |                                    |
| transition time (effects) | transition time    |                      |          |                                    |

### References

<cite>
[1]	"OSRAM rest API," 2015. [Online]. Available: https://us.lightify-api.org. Accessed: Oct. 29, 2016.
</cite>

-----------------------

3.8 Aeotec Light Bulbs
----------------------

### Description

Aeotec sells light bulbswhich are compatible with the Z-Wave protocol. Aeotec products are compatible
with most Z-Wave hubs. Aeotec does not provide a proprietary API for their products.

### Available Devices

1. LED Bulb
- Dimmable
- Configurable Colour

2. LED Strip
- Dimmable
- Configurable Colour

### Research Attributes

| Inputs     | Outputs    | Developer Support   | Protocol | API Restrictions     |
| ------     | -------    | -----------------   | -------- | ----------------     |
| on/off     | on/off     | Not Aeotec Specific | Z-Wave   | None                 |
| colour     | colour     | Z-Wave Developer    |          |                      |
| brightness | brightness |                     |          |                      |

3.9 Aeon Labs
-----------------

### Description

Aeon Labs is a company that produces a large variety of Z-Wave devices. They also provide
the ability to create your own home automation hub.

### Technical Overview

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
<http://zwavepublic.com/specifications>. There is also an open Z-Wave sdk available, to communicate from
the controller to devices.


### Evaluation

Aeon Labs is an ideal solution for our project. To start, there is an easy way to set up our own
hub, instead of being constrained to buying one. This allows us to implement the features we want,
and add support for protocols we want without restriction. Having access to an sdk is very
important to us as well. It lets us not be responsible for implementing the Z-Wave stack protocol,
while also giving us the freedom to use the information received by the devices in a unique way.
Specifically, this will provide us with data for the machine learning algorithm.

### References

<cite>
[1]	"Z-Stick 2E manual," Aeotec, Aeon Labs, 2012. [Online]. Available:
<http://aeotec.com/Z-Wave-usb-stick/913-z-stick-manual-instructions.html>. Accessed: Oct. 13, 2016.
</cite>

<cite>
[2]	"Home automation products," in Aeotec, Aeon Labs, 2006. [Online]. Available:
<http://aeotec.com/homeautomation>. Accessed: Oct. 13, 2016.
</cite>

<cite>
[3]	"OpenZWave library," in OpenZWave. [Online]. Available:
<http://www.openzwave.com/dev/index.html>. Accessed: Oct. 13, 2016.
</cite>

-----------------------

3.10 Spruce Irrigation
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

<cite>
[1] "Spruce - how it works,". [Online]. Available: <http://spruceirrigation.com/How>.
Accessed: Oct. 13, 2016.
</cite>

<cite>
[2] "Spruce irrigation controller & sensor," SmartThings Support. [Online]. Available:
<https://support.smartthings.com/hc/en-us/articles/208053773-Spruce-Irrigation-Controller-Sensor>.
Accessed: Oct. 13, 2016.
</cite>

-----------------------

3.11 OSO PlantLink
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

<cite>
[1] "PlantLink," PlantLink, 2016. [Online]. Available: <https://myplantlink.com/in-action>.
Accessed: Oct. 13, 2016.
</cite>

-----------------------


3.12 Summary of Evaluation
--------------------------

Existing devices with an element of machine learning already incorporated in them are not
a good fit for our system, as they may cause unexpected results when introduced to our
custom machine learning algorithm. Similarly, devices that do not provide an API are also
not suitable for use in our system. Without being able to communicate with a device, there
is no way for us to control is from our hub or to retrieve data from it for the machine
learning algorithm. These aspects rule out devices such as the NEST thermostat and the irrigation
systems.

Third party Z-Wave devices are suitable for our system because they provide an easy method of
communication in a way that helps enable the machine learning rather than hinder it. Any device 
that has no special capabilities other than being Z-Wave ready are ideal, because they allow us
to use them with no unexpected behaviours. The Honeywell VisionPro Thermostat and devices from 
Aeon Labs are examples of this.

### Resources

<cite>
[1] R. Crist, "Best smart home devices of 2016," CNET, 2016. [Online]. Available:
<https://www.cnet.com/topics/smart-home/best-smart-home-devices/>.
Accessed: Oct. 6, 2016. 66
</cite>
