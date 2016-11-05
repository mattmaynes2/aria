### Requests

> Author: Peter Mark
>
> Editor: Matthew Maynes
>
> Updated: October 30, 2016

#### Introduction {-}

The purpose of this section is to provide an understanding of the interactions between an end
user and the system for different types of requests.

#### Web Client {-}

##### User {-}

The User actor represents an end user of the system, which is the Web Client in this case. The
user initiates all requests in the use case diagram for this system.

##### System Hub {-}

The SystemHub actor represents the central hub of the ARIA system. The system hub is in charge
of relaying information of the system to the User through the Web Client.

##### Device {-}

The Device actor represents any device in the ARIA system. A device is responsible for relaying
its specific information to the User through the Web Client.

##### List Devices {-}
Return a list of all devices currently known by the system to the User.

##### View System Events {-}

Return a log of recent events that have occurred in the system. An event is when the state of
a device changes.

##### Get System Status {-}

Return the status of the system to the user. This includes information such as what mode is the
system currently operating in, current version number, number of connected devices, etc.

##### Set System Mode {-}

Set the mode of the system. The different modes are: Standy(0x00), Normal(0x01), and Learning(0x02)

##### Add New Device {-}

Add a new device to the system. This allows the end user to connect a new device to be controlled
by the system and contribute to the machine learning. 

##### Remove Device {-}

Remove a device from the system. This allows a user to remove a device and its information, no 
longer allowing it to be controlled by the system. If added back to the system, there will be no
stored information on it.

##### Get Device State {-}

Return the current state of a device to a user. The state information could include if it is on,
off, and other values depending on the device.

##### Set Device State {-}

Set the current state of a device. The state information could include if it is on, off, and other
values depending on the device.


#### Server Request {-}

![](./uml/ServerRequest.png)

The Server Request diagram shows the workflow that occurs when an end user wants to retrieve
information about the state of the communication server through the web client.

#### Device Request {-}

![](./uml/DeviceRequest.png)

The Device Request diagram shows the workflow that occurs when an end user wants to retrieve 
inform about a specific device in the system through the web client. 
