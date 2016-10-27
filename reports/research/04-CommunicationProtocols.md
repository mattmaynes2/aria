# 4. Communication Protocols

4.1 Background
--------------

There are many different ways to connect devices across a network. A familiar example is WiFi, but
other protocols are available that specialize in different aspects of wireless communication.
The goal of this section is to investigate the strengths and weaknesses of different communication protocols,
and evaluate them against each other.

### Selection Criteria

The criteria used for evaluating communication protocols are based on the non-functional requirements
identified for the system. The key requirements pertaining to communication protocols are: ease of integration with devices,
battery life of devices, range, interoperability, data transfer rate, number of concurrent connections.
Another important aspect of a communication protocol that will be evaluated is what frequency it operates on.

4.2 ZigBee
----------

### Description

The goal of the ZigBee protocol is to provide a means to transfer small amounts of data over a limited distance.
Relative to WiFi, The decreased in data transmission rates and range of ZigBee allows compatible 
devices to consume less power; this allows for increased battery life and energy efficiency. ZigBee shields
are available for many popular embedded communication devices, allowing them to communicate with ZigBee-compatible
smart devices. Many companies offer smart devices which are compatible with the ZigBee protocol, such as lights 
and light switches.

### Technical Overview

ZigBee uses a mesh networking topology, as opposed to the star topology used by WiFi. A mesh
topology means that every node in the network is connected. Each node transmits its own
information, as well as assisting in relaying information received from other nodes. Having every
node connected allows for data to be transmitted between nodes simultaneously, and increases network
stability be not relying on one central node. This increase in stability comes at the cost of having
potentially many redundant connections in the network. ZigBee devices use the mesh topology to send
messages using message routing. This means that if the endpoint device is out of range of the
initial device, intermediate devices will relay the message through the mesh until it reaches its
endpoint.

ZigBee operates within three possible frequency bands: 868-870 MHz, 902-928 MHz, and 2.4-2.4835 GHz.
The lowest band only has one available channel, the middle band has ten available channels, and the
highest band has 16 available channels. The respective data transfer rates are 20Kbps, 40Kbps, and
250Kbps. It should be noted that devices on different frequency bands cannot communicate with each
other, and generally only devices using the 2.4 Ghz range are commercially available.

The low power consumption of ZigBee devices when compared to WiFi leads to large energy efficiency
and battery life gains.  A ZigBee device can last for up to ten years.

A device can be added to a ZigBee network in approximately thirty millisecondss. Theoretically, up to
256 devices can be connected to one network. However, in practise, the system performance tends to
degrade at around thirty devices.

One of the major drawbacks of ZigBee is that for it to be effective, it must operate in the 2.4 GHz
frequency band. This would not be an issue, except for the fact that this is the same frequency band
as WiFi. This can cause interference between the two networks, resulting in packet loss for both
networks. The lost packets have to be retransmitted until they are received by the intended
endpoint, causing lag in both networks. ZigBee packets suffer more from this interference in
practice, with the level of interference rising as the number of nodes and the amount of traffic
rises.

A second potential drawback of ZigBee is the historical lack of official standards for application-level
protocols for ZigBee devices. While ZigBee devices all communicate using the same physical layer 
protocol, each device may use a different high-level protocol for device control.The result of this lack 
of standardization is that different companies have their own protocols for ZigBee device communication, 
so devices from different companies cannot be assumed to be compatible. The limited interoperability has
been somewhat fixed with the introduction of the ZigBee Alliance, but could present some legacy issues.


### References

[1] "What Technology?," in SMARTHOME® - Home Automation Superstore, 1995. [Online].  Available:
http://www.smarthome.com/sc-what-technology. Accessed: Oct. 6, 2016.

[2] L. LABS, "Z-Wave vs. Zigbee," in Wireless Technology, Link Labs, 2015. [Online].  Available:
http://www.link-labs.com/z-wave-vs-zigbee/. Accessed: Oct. 6, 2016.

[3] L. LABS, "The ZigBee vs WiFi battle for M2M communication," in IOT Networks, Link Labs, 2015.
[Online]. Available: http://www.link-labs.com/zigbee-vs-wifi-802-11ah/. Accessed: Oct.  6, 2016.

[4] P. Sparrow, "Mesh Topology: Advantages and disadvantages," in I Answer 4 U. [Online].
Available: http://www.ianswer4u.com/2011/05/mesh-topology-advantages-and.html#axzz4MJR54MC7.
Accessed: Oct. 6, 2016.

[5] J. Gracia Castro and Ó. Pérez Domínguez, "ZigBee: IEEE 802.15.4," in Tampere University of
Engineering, 2007. [Online]. Available:
https://www.cs.tut.fi/kurssit/TLT-6556/Slides/4-802.15ZigBee.pdf. Accessed: Oct. 6, 2016.

[6] W. Mardini, Y. Khamayseh, R. Jaradatand, and R. Hijjawi, "Interference Problem between ZigBee
and WiFi," 2012. [Online]. Available: http://www.ipcsit.com/vol30/024-ICNCS2012-G3061.pdf. Accessed:
Oct. 6, 2016.


4.3 Z-Wave
----------

### Description

Z-Wave is a very similar option to ZigBee, except it uses a proprietary radio design. This slightly
limits the number of devices available for it, as chips are mostly produced by Sigma Designs. The
advantage to this is that because the chips are made largely by one manufacturer, there is a high
level of interoperability. In addition, the Z-Wave protocol includes high-level commands for 
controlling certain classes of devices, which further increases interoperability of Z-Wave systems. 

### Technical Overview

One area where Z-Wave differs from ZigBee is the frequency range of operation. It operates at 908.42
MHz instead of at 2.4 GHz, which avoids the issue of conflicting with WiFi signals. In terms of
device limits, it is very similar, being able to handle between 30 and 40 devices before issues
start to occur. Z-Wave is similar to ZigBee in terms of device range and power consumption.

### References

[1] "What is Z-Wave," in SMARTHOME® - Home Automation Superstore, 1995. [Online].  Available:
http://www.smarthome.com/sc-what-is-zwave-home-automation. Accessed: Oct. 6, 2016.

[2] "Z-Wave vs. Zigbee," in Link Labs, Link Labs, 2015. [Online]. Available:
http://www.link-labs.com/z-wave-vs-zigbee/. Accessed: Oct. 6, 2016.

[3] L. Frenzel, "What’s the difference between ZigBee and Z-Wave?," in Electronic Design, 2012.
[Online]. Available:
http://electronicdesign.com/communications/what-s-difference-between-zigbee-and-z-wave. Accessed:
Oct. 6, 2016.



4.4 INSTEON
-----------

### Description

INSTEON is substantially different from the two above protocols.

### Technical Overview

INSTEON uses a similar mesh topology to the above protocols, but it is not limited to radio
frequencies. It utilizes a dual-mesh system to increase overall stability. The dual-mesh system is a
combination of radio frequencies at 915 MHz (in the US), and powerline layer operating at 131.65
KHz.Powerline communication is a technology that uses a home's electrical wiring to transfer data.  
When the radio frequencies encounter interference, the powerline layer makes sure the message
gets broadcasted to the appropriate destination. INSTEON also uses a different message delivery 
system compared to ZigBee and Z-Wave. Instead of sending a message from one device and routing it
through other devices, it takes advantage of simulcasting. This is the process of having multiple
devices broadcasting the same message, so the intended recipient gets the message faster and more
reliably. This method is not feasible for high data rates, but INSTEON shares it's low data rates
with ZigBee and Z-Wave. Simulcasting is also a result of the fact that an INSTEON network does not
have a master/slave relationship. Every node has the ability to send and receive messages without
having a controller. This makes it possible to have any number of devices in a network without being
restricted by a maximum number of connections to a controlling device.

One thing INSTEON is lacking compared to ZigBee and Z-Wave is third party support for their devices.
They manufacture almost all of their own devices, which leads to a limited amount of choice in terms
of different types of devices designed for the same task.

A unique advantage of INSTEON is its ability to interface with devices following the X10 protocol.
The X10 protocol was one of the original protocols designed to work using only powerlines. It is
outdated now in terms of being a reasonable choice for a new system, as it was designed over 30
years ago. This means that there is no wireless communication involved, which is essential for a
modern day smart home communication protocol. That said, there are many legacy automation systems in
place which still use X10 devices. If this were the case, then INSTEON would be an ideal choice for
a communication protocol.

### References

[1] "WHITEPAPER: Compared," in INSTEON. [Online]. Available:
http://cache.insteon.com/pdf/INSTEONCompared.pdf. Accessed: Oct. 6, 2016.

[2] "X10," in Build Your Smarthome, 2014. [Online]. Available:
http://buildyoursmarthome.co/home-automation/protocols/x10/. Accessed: Oct. 8, 2016.

[3] "What home automation protocol should I choose?," in Intellihome, 2015. [Online].  Available:
https://www.intellihome.be/en/kbase/INSTEON/What_home_automation_protocol_should_I_choose\_-2.html.
Accessed: Oct. 8, 2016.




4.5 WiFi
---------

### Description

WiFi is by far the most common communication protocol used in a home on a daily basis. Nearly every
other communication protocol is compatible with WiFi devices, and they tend to be easy to install.
There are several pros and cons associated with using WiFi for home automation, which are outlined
below.

### Technical Overview

WiFi operates using a star network topology. Every node is connected to a central server node. All
communications go from the source node, through the central server node, and arrive at the
destination node. This means that if the central server goes down, no messages can be passed,
leading to potential stability issues. Because messages cannot be routed through intermediate nodes,
the communication range must generally be much larger than in a mesh network.  WiFi also boasts
substantially higher data transmission rates than the communication protocols discussed previously.
A WiFi (802.11b) connection can transfer data at a rate of 54 Mbps at a range of 100 meters. As
stated earlier, WiFi typically operates at a frequency of 2.4 GHz.

The biggest advantage of using WiFi for home automation is the simplicity. There is virtually no
limit to the number of devices that are WiFi compatible, as devices using nearly every other big
communication protocol for home automation are also compatible with WiFi. It also requires no extra
hardware to communicate with WiFi, which reduces the complexity of setting up hardware.
Non-technical users are still generally familiar with WiFi, making the setup process easier.

An issue with using WiFi for home automation is that in terms of required range and data transfer
specifications, it is overkill. WiFi is designed with high intensive data transfer in mind, which
home automation systems do not take advantage of. A WiFi device needs to provide enough power to
operates with these specifications, leading to a large increase in power consumption. If the device
is battery powered, it will drain much more quickly than if it were using one of the above
protocols.

Another issue stems directly from the prevalence of WiFi. Having a smart home network sharing a WiFi
network with regular household uses can cause the network as a whole to slow, due to the bandwidth
being shared across so many devices.

### References

[1] "Introduction to Wi-Fi (802.11 or WiFi)," in CCM Benchmark, CCM, 2016. [Online].  Available:
http://ccm.net/contents/802-introduction-to-wi-fi-802-11-or-wifi. Accessed: Oct. 8, 2016.

[2] E. Contributor, "Home Automation Protocols: A Round-Up," in Electronic House, Electronic
House, 2016. [Online]. Available:
https://www.electronichouse.com/smart-home/home-automation-protocols-what-technology-is-right-for-you/.
Accessed: Oct. 8, 2016.



4.6 Bluetooth
---------

### Description
Bluetooth is the most similar to WiFi of the alternative options. It is fairly common in households, 
and non-technical users are more likely to be familiar with it than other protocols. There are 
two main classifications of Bluetooth when it comes to home automation, both of which will be 
discussed below.

### Technical Overview
Bluetooth operates in the 2.4 GHz frequency band, alongside WiFi and ZigBee. Bluetooth also shares
the star network topology with WiFi, where there needs to be designated master and slave devices. 
This can lead to the same interferece problems as discussed in the WiFi and ZigBee secions. As the 
number of devices on the same radio frequency increases, the competition for bandwidth also increases,
causing potential lag and interference. The range and data transfer rate for Bluetooth ranges
from 1 Mbps and 10 meters to 24 Mbps and 100 meters. All of these data transfer rates are acceptable, 
if not overkill, for a smarthome system. The range on the earlier versions of Bluetooth is potentially 
very restricting. Bluetooth is somewhere between WiFi devices and ZigBee/Z-Wave devices in terms of
power consumption.

There is another choice for Bluetooth that addresses some of the issues above. Bluetooth version 4.0,
also branded as Bluetooth Low Energy (BLE). This is a direct competitor with ZigBee and Z-Wave. The range
for a BLE device is 50 meters, but BLE is able to take advantage of a mesh network topology. The maximum 
data transfer rate 1 Mbps in theory, but it is generally much lower than that in practise. BLE splits the
2.4 GHz channel into smaller sub-channels to help avoid interference with WiFi channels. 

One of the goals of BLE is to make devices that do not require constant data transmission more efficient.
It accomplishes this by not keeping connections active while there is no data being transferred. Once 
data needs to be transferred, it reestablishes the necessary connection, completes the transfer, and closes
the connection again.

### References

[1] Jim, "Bluetooth basics," in sparkfun. [Online]. Available: 
https://learn.sparkfun.com/tutorials/bluetooth-basics/common-versions. Accessed: Oct. 9, 2016.

[2] "Data rates using BLE," in Anaren atmosphere. [Online]. Available:
https://atmosphere.anaren.com/wiki/Data_rates_using_BLE. Accessed: Oct. 9, 2016.

[3] "Bluetooth low energy," in CSR. [Online]. Available: 
https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=227336. Accessed: Oct. 9, 2016.



4.7 Summary of Evaluation
-------------------------

###Evaluation Criteria

| Protocol | Transfer Rate | Battery Life | Interoperability | # of Connections | Frequency | Range   | Topology |
| ---------| ------------  | ------------ | ---------------- | ---------------- | --------- | ------- | -------- |   
| ZigBee   | 250 Kbps      |  good        |  good            |    256           |  2.4 GHz  | 35 ft   |  Mesh    |           
| Z-Wave   | 40 Kbps       |  great       |  great           |    232           |  915 MHz  | 100 ft  |  Mesh    |          
| INSTEON  | 13 Kbps       |  good        |  bad             |    N/A           |  915 MHz  | 150 ft  |  Mesh    |           
| WiFi     | 54 Mbps       |  bad         |  great           |    256           |  2.4 GHz  | 105 ft  |  Star    |             
| BLE      | 10 Kbps       |  good        |  great           |     9            |  2.4 GHz  | 200 ft  |  Star    |
 
As stated above, the goal of this research was to pick an appropriate protocol for our system.
One of the differing attributes between the protocols is the data transfer rates. 
The required data rate for most smart home devices is minimal, and a higher data rate demands more power. 
The data rate provided by WiFi is clearly overkill for our project, so it will not be the primary communication protocol used. 
That being said, WiFi compatibility is important to this project because of its prevalence in homes, and because of the
enormous amount of devices that communicate over WiFi.

Having as inclusive device support as possible is a key aspect to our project, as it allows a
user to have whatever functionality they desire. This heavily influenced us in deciding not
to use INSTEON as our primary protocol, as the backwards compatibility with X10 is not something
we require.

ZigBee and Z-Wave are very similar, with the key difference in our eyes being the consistent 
interface that Z-Wave devices provide for controlling them. In additionally, avoiding  conflicts
between the WiFi already assumed to be in the house and the home automation system is a clear benefit.
Z-Wave operates in the less used 900 MHz frequency band, avoiding any potential conflicts.

A mesh network topology makes more sense than a star topology for home automation. The stability
offered by a mesh topology is substantial, and the amount of data transmission is low enough that
the redundant connections are not costly. This made Z-Wave a more attractive option to us over 
Bluetooth Low Energy.

Overall, we decided that using Z-Wave as our primary communication protocol was the best choice
for this project, while supporting WiFi devices as well.


4.8 Z-Wave Implementation Specifics
-----------------------------------

Any processing unit with USB support can be easily turned into a Z-Wave master, using a Z-Wave 
USB stick. Converting an Arduino into a Z-Wave slave is not simple. There are specialized 
Arduino boards that have the Z-Wave protocol built in. Another option is to attach a radio
frequency device to an Arduino, and to implement the Z-Wave stack protocol manually. The easiest
way to have Z-Wave slave devices is simply not to make them, but to buy them.

