Section Title
=============

### Background

  There are many different ways to connect devices accross a network. The every day example is WiFi, but that is not the
only option. There are different protocols available that specialize in different aspects of wireless communication.
To achieve a connected smart home environment, our devices need to communicate to each other and to the system. The goal 
of this section is to discover communication options, and to evaluate them against each other to determine which is most
appropriate for our system.

### Selection Criteria
  The available communication protocols will be evaluated based largly on the non-functional requirements of our
system. For the protocols, this includes: ease of integration with devices, battery life of devices, range, reliability, interoperability, data transmission rate, number of concurrent connections, device discovery time, and cost.



ZigBee
------------

## Description

  ZigBee provides an alternative to WiFi. The goal of ZigBee is to provide simple transmission for a low amount of data, within
a limited range. The decrease in data transmission rates and range provides an increased battery life for components. A computing device can be turned into a ZigBee device with the appropriate shield, and some ZigBee devices, such as a lightswitch, can be purchased. 

## Technical Overview

  ZigBee uses a mesh networking topology, as opposed to the star topology used by Wifi.  A mesh topology means that every node
in the network is connected. Each node transmitts it's own information, as well as assisting in relaying information received
from other nodes. Having every node connected allows for data to be transmitted between nodes simultaneously, and increases 
network stability be not relying on one central node. This increase in stability come at the cost of having potentially many
redundant connections in the network. Zigbee devices use the mesh topology to send messages using message routing. This means that if the endpoint device is out of range of the initial device, intermediate devices will relay the message through the mesh until it reaches it's endpoint.

  ZigBee operates within three possible frequency bands: 868-870 MHz, 902-928 MHz, and 2.4-2.4835 GHz. The lowest band only
has one available channel, the middle band has ten available channels, and the highest band has 16 available channels. The
respective data transfer rates are 20Kbps, 40Kbps, and 250Kbps. It should be noted that devices on different frequency bands cannot communicate with each other, and generally only devices using the 2.4 Ghz range are produced.

  The low power consumption of ZigBee devices when compared to WiFi leads to large power consumption and battery life gains.
A ZigBee decive can last for up to ten years.

  A ZigBee device can be added to the network in approximatly thirty milliseconds, and 256 devices can be connected to one
network in theory. However, in practice, the system performance tends to degrade at around thirty devices. 

  One of the major drawbacks of ZigBee is that for it to be effective, it must operate in the 2.4 GHz frequency band. This 
would not be an issue, except for the fact that this is the same frequency band as WiFi. This can cause interference between the two networks, resulting in packet loss for both networks. The lost packets have to be retransmitted until they are recieved
by the intended endpoint, causing lag in both networks. ZigBee packets suffer more from this interference in practice, with the
level of interference rising as the number of nodes and the amount of traffic rises.

  A second potential drawback of ZigBee is the historical lack of official standard for communication protocols between devices.
This resulted in in different companies having their own protocols for ZigBee device communication, and not all devices could
be purchased and assumed to work together. This limited interoperability has been somewhat fixed with the introduction of the
ZigBee Alliance, but could present some legacy issues.


## Citations

&mdash; <cite>"What Technology?," in SMARTHOME® - Home Automation Superstore, 1995. [Online]. Available: http://www.smarthome.com/sc-what-technology. Accessed: Oct. 6, 2016. </cite>

&mdash; <cite>L. LABS, "Z-Wave vs. Zigbee," in Wireless Technology, Link Labs, 2015. [Online]. Available: http://www.link-labs.com/z-wave-vs-zigbee/. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite>L. LABS, "The ZigBee vs WiFi battle for M2M communication," in IOT Networks, Link Labs, 2015. [Online]. Available: http://www.link-labs.com/zigbee-vs-wifi-802-11ah/. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite>P. Sparrow, "Mesh Topology: Advantages and disadvantages," in I Answer 4 U. [Online]. Available: http://www.ianswer4u.com/2011/05/mesh-topology-advantages-and.html#axzz4MJR54MC7. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite>	J. Gracia Castro and Ó. Pérez Domínguez, "ZigBee: IEEE 802.15.4," in Tampere University of Engineering, 2007. [Online]. Available: https://www.cs.tut.fi/kurssit/TLT-6556/Slides/4-802.15ZigBee.pdf. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite>	W. Mardini, Y. Khamayseh, R. Jaradatand, and R. Hijjawi, "Interference Problem between ZigBee and WiFi," 2012. [Online]. Available: http://www.ipcsit.com/vol30/024-ICNCS2012-G3061.pdf. Accessed: Oct. 6, 2016.</cite>



Z-Wave
------------

## Description

Z-Wave is a very similar option to ZigBee, except it uses a proprietary radio design. This slightly limits the number of devices available for it, as chips are mostly produced by Sigma Designs. The advantage to this is that because the chips are made largely by one manufacturer, there is a high level of interoperation.

## Technical Overview

One area where Z-Wave differs from ZigBee is the frequency range of operation. It operates at 908.42 MHz instead of at 2.4 GHz, which avoids the issue of conflicting with WiFi signals. In terms of device limits, it is very similar, being able to handle between 30 and 40 devices before issues start to occur. Z-Wave is similar to ZigBee in terms of device range and power consumption. 

## Citations
&mdash; <cite>"What is Z-Wave," in SMARTHOME® - Home Automation Superstore, 1995. [Online]. Available: http://www.smarthome.com/sc-what-is-zwave-home-automation. Accessed: Oct. 6, 2016. </cite>

&mdash; <cite>"Z-Wave vs. Zigbee," in Link Labs, Link Labs, 2015. [Online]. Available: http://www.link-labs.com/z-wave-vs-zigbee/. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite>	L. Frenzel, "What’s the difference between ZigBee and Z-Wave?," in Electronic Design, 2012. [Online]. Available: http://electronicdesign.com/communications/what-s-difference-between-zigbee-and-z-wave. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite></cite>

INSTEON
------------

## Description

INSTEON is substatially different from the two above protocols.

## Technical Overview

INSTEON uses a similar mesh topology as the above protocols, but it is not limited to radio frequencies. It utalizes a dual-mesh system to increase overall stability. The dual-mesh system is a combination of radio frequencies at 915 MHz (in the US), and powerline layer operating at 131.65 KHz. When the radio frequencies encounter interference, the powerline layer makes sure the message gets broadcasted to the appropriate destination. INSTEON also uses a different message devilvery system compared to ZigBee and Z-Wave. Instead of sending a message from one device and routing it through other devices, it takes advantage of simucasting. This is the process of having multiple devices broadcasting the same message, so the intended recipient gets the message faster and more reliably. This method is not feasible for high data rates, but INSTEON shares it's low data rates with ZigBee and Z-Wave.

One thing INSTEON is lacking compared to ZigBee and Z-Wave is third part support for their devices. They manufacture almost all of their own devices, which leads to a limited amount of choice in terms of different types of devices designed for the same task. 

A unique advantage of INSTEON is its ability to interface with devices following the X10 protocol. The X10 protocol was one of the origional protocols designed to work using only powerlines. It is outdated now in terms of being a reasonable choice for a new system, as it was designed over 30 years ago. This means that there is no wireless communication involved, which is essential for a modern day smart home communication protocol. That said, there are many legacy automation systems in place which still use X10 devices. If this were the case, then INSTEON would be an ideal choice for a communication protocol.

## Citations
-----------------------

&mdash; <cite>"WHITEPAPER: Compared," in INSTEON. [Online]. Available: http://cache.insteon.com/pdf/INSTEONCompared.pdf. Accessed: Oct. 6, 2016.</cite>

&mdash; <cite>"X10," in Build Your Smarthome, 2014. [Online]. Available: http://buildyoursmarthome.co/home-automation/protocols/x10/. Accessed: Oct. 8, 2016.
</cite>

&mdash; <cite>"What home automation protocol should I choose?," in Intellihome, 2015. [Online]. Available: https://www.intellihome.be/en/kbase/INSTEON/What_home_automation_protocol_should_I_choose_-2.html. Accessed: Oct. 8, 2016.
</cite>


### Summary of Evaluation

All of the evaluation grouped together

### Conclusion

What did we decide upon? Why?
