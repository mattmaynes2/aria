# Existing Home Automation Systems

This section describes the outcomes of our research into existing home automation systems.
The goal of the research was to determine the feasibility of using  existing 
home automation systems and smart devices the project.

## Nest

Nest offers many smart devices for use with their home automation system. If it were 
possible to use some of these devices with a custom home automation system, we wouldn't 
need to worry about creating hardware components for this project.

Nest provides an API which can be used to control the Nest devices installed in a home.
The API does not allow software to communicate directly with a device. In order to control
a device, the device must be installed into a user's Nest system and set up through the 
Nest app. Our home automation system could then communicate with Nest's cloud services
to control the device.

Use of the Nest API also requires registration in Nest's developer program, which
would subject the project to several restrictions.

While use of Nest's smart devices would allow us to focus on the software aspects of 
the project, it appears that any software that uses Nest devices must be integrated 
with the entire Nest smart home system, which adds a level of complexity that is 
unnecessary for this project.

## ZigBee

ZigBee provides an alternative to WiFi for device to device communication.  It operates
with a lower power consumption, leading to a much longer device battery time when compared
to WiFi. Once a set-top box is set up, it provides a cloud connection for all the Zigbee 
devices in your home.

ZigBee can interface with an arduinos simple by using an Xbee shield. Two arduinos with ZigBee
shields communicate with each other 

In order to develop commercial products with ZigBee, one must join the ZigBee Alliance. The
lowest level of entry is the Alliance level, costing $4000 USD/year. However, for non-commercial
purposes, access to the specification is free. This makes it a viable option for this project,
but would have to be considered differently if it were to turn into a commercial project.
