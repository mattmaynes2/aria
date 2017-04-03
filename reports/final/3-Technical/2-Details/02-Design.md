### System Design

![][product-design]

This diagram illustrates at a high level the communication between physical devices in the Aria 
system. The smart hub will be the main point of communication for all smart devices in the network.
The user will use the web interface to send commands to the smart hub. The smart hub will determine 
how to relay these commands to smart devices if required.

The design for this system will need to consider the requirement that multiple devices will need
to connect to a single smart hub. The hub will also need to support concurrent connections in order 
to allow multiple users to have access at any given time. These features present some
hardware requirements that must be satisfied. The physical smart hub must have external interfaces
for communicating to multiple devices and must support concurrent processes. The communication
protocol used to interface with the smart devices themselves must also be considered as it must
work on low power embedded devices with short to medium range connections. Fortunately, the
data transfer rate requirements for this system will be minimal as only small state transfers
of sensor readings or device commands must be communicated.

The smart hub's requirements limits the devices that can be utilized for its purpose. A
comprehensive breakdown of the specifications of considered devices can be viewed in [Appendix B](#B).
The research compares a number of computing devices for the role of the smart hub
including various Arduinos, Raspberry Pis and Beagle Bones. Due to the requirement of concurrent
processes, a number of the computing devices were eliminated. The eliminated computing devices
were all embedded machines that only offered a single core processor with no operating system
or concurrency mechanisms. It would only be fair to call the remaining devices miniature
computers as they all support light weight operating systems with concurrency. Of these devices,
the Raspberry Pi 3 Model B has the greatest performance specifications and would be able to
perform the required tasks for the smart hub.

When considering the communication protocols to support for the smart home system, efficiency,
range and interoperability must be considered. Leading industry communication protocols
including WiFi, Bluetooth, ZigBee, Z-Wave and Insteon were examined for these requirements.
The full details of the research of these communication protocols can be seen in [Appendix C](#C).
While the Aria system is designed to support many protocols, a single one needed to be chosen
as an initial, prototype protocol. For this task, Z-Wave was chosen as it provides the most
standardized method for device communication of any of the protocols. Z-Wave is both a
hardware and software level specification that integrates a wide spectrum of devices over
a single, standard interface. For this reason, it was selected as the primary device
communication for the Aria system.

The remainder of the technical section outlines the details of the software development and
implementation of the smart hub. Included in this analysis is the details of the remote client
interface for controlling the smart hub and its connected devices.




