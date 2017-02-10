### C-1 ZigBee {- #C-1}

#### Description {-}

The goal of the ZigBee protocol is to provide an efficient way to transfer small amounts of data over a
limited distance. Relative to WiFi, the decreased data transmission rate and range of ZigBee
allows compatible devices to consume less power allowing for increased battery life and energy
efficiency. ZigBee shields are available for many popular embedded communication devices, allowing
them to communicate with ZigBee compatible smart devices. Many companies offer smart devices which
are compatible with the ZigBee protocol, such as lights and light switches.

#### Technical Overview {-}

ZigBee uses a mesh networking topology, as opposed to the star topology used by WiFi [^C-1-1]. A mesh
topology means that every node in the network is connected. Each node transmits its own
information, as well as assisting in relaying information received from other nodes. Having every
node connected allows for data to be transmitted between nodes simultaneously, and increases network
stability on not relying on one central node. This increase in stability comes at the cost of having
potentially many redundant connections in the network. ZigBee devices use the mesh topology to send
messages using message routing. This means that if the endpoint device is out of range of the
initial device. Intermediate devices will relay the message through the mesh until it reaches its
endpoint.

ZigBee operates within three possible frequency bands: 868-870 MHz, 902-928 MHz, and 2.4-2.4835 GHz [^C-1-2].
The lowest band only has one available channel, the middle band has ten available channels, and the
highest band has 16 available channels. The respective data transfer rates are 20 kbps, 40 kbps, and
250 kbps. It should be noted that devices on different frequency bands cannot communicate with each
other, and generally only devices using the 2.4 GHz range are commercially available.

The low power consumption of ZigBee devices when compared to WiFi leads to better energy efficiency
and a longer batter life [^C-1-3].

Theoretically, up to 256 devices can be connected to one network. However, in practise, the system performance
tends to degrade at around thirty devices [^C-1-4].

One of the major drawbacks of ZigBee is that for it to be effective, it must operate in the 2.4 GHz
frequency band. This would not be an issue, except for the fact that this is the same frequency
band as older versions of WiFi. This can cause interference between the two networks, resulting in
packet loss for both networks. The lost packets have to be retransmitted until they are received by
the intended endpoint, causing lag in both networks. ZigBee packets suffer more from this
interference in practice, with the level of interference rising as the number of nodes and the
amount of traffic rises. Fortunately, newer WiFi networks operate on the 5 GHz channel which would
eliminate this interference [^C-1-5].

A second potential drawback of ZigBee is the historical lack of official standards for
application-level protocols for ZigBee devices. While ZigBee devices all communicate using the same
physical layer protocol, each device may use a different high-level protocol for device control.
The result of this lack of standardization is that different companies have their own protocols for
ZigBee device communication, so devices from different companies cannot be assumed to be
compatible. The limited interoperability has been somewhat fixed with the introduction of the ZigBee
Alliance, but could present some legacy issues [^C-1-6].

[^C-1-1] L. LABS, "Z-Wave vs. Zigbee," in Wireless Technology, Link Labs, 2015. [Online]. Available: http://www.link-labs.com/z-wave-vs-zigbee/. Accessed: Oct. 6, 2016.

[^C-1-2] J. Gracia Castro and Ó. Pérez Domínguez, "ZigBee: IEEE 802.15.4," in Tampere University of Engineering, 2007. [Online]. Available: https://www.cs.tut.fi/kurssit/TLT-6556/Slides/4-802.15ZigBee.pdf. Accessed: Oct. 6, 2016.

[^C-1-3] L. LABS, "The ZigBee vs WiFi battle for M2M communication," in IOT Networks, Link Labs, 2015. [Online]. Available: http://www.link-labs.com/zigbee-vs-wifi-802-11ah/. Accessed: Oct. 6, 2016.

[^C-1-4] "What Technology?," in SMARTHOME® - Home Automation Superstore, 1995. [Online]. Available: http://www.smarthome.com/sc-what-technology. Accessed: Oct. 6, 2016.

[^C-1-5] W. Mardini, Y. Khamayseh, R. Jaradatand, and R. Hijjawi, "Interference Problem between ZigBee and WiFi," 2012. [Online]. Available: http://www.ipcsit.com/vol30/024-ICNCS2012-G3061.pdf. Accessed: Oct. 6, 2016.

[^C-1-6]J. Kastrenakes, "The dumb state of the smart home," in The Verge, The Verge, 2014. [Online]. Available: http://www.theverge.com/2014/1/24/5336104/smart-home-standard-are-a-mess-zigbee-z-wave. Accessed: Feb. 10, 2017.





