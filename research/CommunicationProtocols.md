Section Title
=============

### Background

  There are many different ways to connect devices accross a network. The every day example is WiFi, but that is not the
only option. There are different protocols available that specialize in different aspects of wireless communication.
To achieve a connected smart home environment, our devices need to communicate to each other and to the system. The goal 
of this section is to discover communication options, and to evaluate them against each other to determine which is most
appropriate for our system.

### Selection Criteria
  The available communication protocols will be evaluated based on the functional and non-functional requirements of our
system. For the protocols, this includes: battery life of devices, range, reliability, interoperability, data transmission rate,
number of concurrent connections, device discovery time, and cost.


ZigBee
------------

## Description

  ZigBee provides an alternative to WiFi. The goal of ZigBee is to provide simple transmission for a low amount of data, within
a limited range. The decrease in data transmission rates and range provides an increased battery life for components.

## Technical Overview

  ZigBee uses a mesh networking topology, as opposed to the star topology used by Wifi.  A mesh topology means that every node
in the network is connected. Each node transmitts it's own information, as well as assisting in relaying information received
from other nodes. Having every node connected allows for data to be transmitted between nodes simultaneously, and increases 
network stability be not relying on one central node. This increase in stability come at the cost of having potentially many
redundant connections in the network.

  ZigBee operates within three possible frequency bands: 868-870 MHz, 902-928 MHz, and 2.4-2.4835 GHz. The lowest band only
has one available channel, the middle band has ten available channels, and the highest band has 16 available channels. The
respective data transfer rates are 20Kbps, 40Kbps, and 250Kbps.

  The low power consumption of ZigBee devices when compared to WiFi leads to large power consumption and battery life gains.
A ZigBee decive can last for up to ten years.

  A ZigBee device can be added to the network in approximatly thirty milliseconds, and 256 devices can be connected to one
network in theory. However, in practice, the system performance tends to degrade at around thirty devices.

  One of the major drawbacks of ZigBee is that for it to be effective, it must operate in the 2.4 GHz frequency band. This 
would not be an issue, except for the fact that this is the same frequency band as WiFi. This can cause interference between 
the two networks, resulting in packet loss for both networks. The lost packets have to be retransmitted until they are recieved
by the intended endpoint, causing lag in both networks. ZigBee packets suffer more from this interference in practice, with the
level of interference rising as the number of nodes and the amount of traffic rises.

  A second potential drawback of ZigBee is the historical lack of official standard for communication protocols between devices.
This resulted in in different companies having their own protocols for ZigBee device communication, and not all devices could
be purchased and assumed to work together. This limited interoperability has been somewhat fixed with the introduction of the
ZigBee Alliance, but could present some legacy issues.

  

## Evaluation

How does this specific item do against our criteria?
-----------------------

## Citations
-- <cite>"What Technology?," in SMARTHOME® - Home Automation Superstore, 1995. [Online]. Available: http://www.smarthome.com/sc-what-technology. Accessed: Oct. 6, 2016. </cite>

Z-Wave
------------

## Description

Z-Wave was designed to be a successor to ZigBee.   

## Technical Overview

Technically speaking, what does this item do?

## Evaluation

How does this specific item do against our criteria?

-----------------------


### Summary of Evaluation

All of the evaluation grouped together

### Conclusion

What did we decide upon? Why?
