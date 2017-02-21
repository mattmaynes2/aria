### C-4 WiFi {- #C-4}

#### Description {-}

WiFi is by far the most common communication protocol used in a home on a daily basis. Nearly every
other communication protocol is compatible with WiFi devices, and they tend to be easy to install.
There are several pros and cons associated with using WiFi for home automation, which are outlined
below.

#### Technical Overview {-}

WiFi operates using a star network topology [^C-4-3]. Every node is connected to a central server node. All
communications go from the source node, through the central server node, and arrive at the
destination node. This means that if the central server goes down, no messages can be passed,
leading to potential stability issues. Because messages cannot be routed through intermediate nodes,
the communication range must generally be much larger than in a mesh network.  WiFi also boasts
substantially higher data transmission rates than the communication protocols discussed previously.
A WiFi (802.11b) connection can transfer data at a rate of 54 Mbps at a range of 100 meters [^C-4-1]. As
stated earlier, WiFi typically operates at a frequency of 2.4 GHz.

The biggest advantage of using WiFi for home automation is the simplicity. There is virtually no
limit to the number of devices that are WiFi compatible, as devices using nearly every other big
communication protocol for home automation are also compatible with WiFi. It also requires no extra
hardware to communicate with WiFi, which reduces the complexity of setting up hardware.
Non-technical users are still generally familiar with WiFi, making the setup process easier.

An issue with using WiFi for home automation is that in terms of required range and data transfer
specifications, it is overkill [^C-4-2]. WiFi is designed with high intensive data transfer in mind, which
home automation systems do not take advantage of. A WiFi device needs to provide enough power to
operates with these specifications, leading to a large increase in power consumption. If the device
is battery powered, it will drain much more quickly than if it were using one of the above
protocols.

Another issue stems directly from the prevalence of WiFi. Having a smart home network sharing a WiFi
network with regular household uses can cause the network as a whole to slow, due to the bandwidth
being shared across so many devices [^C-4-4].

[^C-4-1] "Introduction to Wi-Fi (802.11 or WiFi)," in CCM Benchmark, CCM, 2016. [Online]. Available: http://ccm.net/contents/802-introduction-to-wi-fi-802-11-or-wifi. Accessed: Oct. 8, 2016.

[^C-4-2] L. LABS, "The ZigBee vs WiFi battle for M2M communication," in IOT Networks, Link Labs, 2015. [Online]. Available: http://www.link-labs.com/zigbee-vs-wifi-802-11ah/. Accessed: Oct. 6, 2016.

[^C-4-3] "What Technology?," in SMARTHOME® - Home Automation Superstore, 1995. [Online]. Available: http://www.smarthome.com/sc-what-technology. Accessed: Oct. 6, 2016.

[^C-4-4] W. Mardini, Y. Khamayseh, R. Jaradatand, and R. Hijjawi, "Interference Problem between ZigBee and WiFi," 2012. [Online]. Available: http://www.ipcsit.com/vol30/024-ICNCS2012-G3061.pdf. Accessed: Oct. 6, 2016.








