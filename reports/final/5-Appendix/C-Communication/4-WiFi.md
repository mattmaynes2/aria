### C-4 WiFi {- #C-4}

#### Description {-}

WiFi is by far the most common communication protocol used in a home on a daily basis. Nearly every
other communication protocol is compatible with WiFi devices, and they tend to be easy to install.
There are several pros and cons associated with using WiFi for home automation, which are outlined
below.

#### Technical Overview {-}

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

