# 8. Requests

8.1 Introduction
----------------


8.2 Web Client
--------------
###User
The User actor represents an end user of the system, which is the Web Client in this case. The
user initiates all requests in the use case diagram for this system.

###SystemHub
The SystemHub actor represents the central hub of the ARIA system. The system hub is in charge
of relaying information of the system to the User through the Web Client.

###Device
The Device actor represents any device in the ARIA system. A device is responsible for relaying
its specific information to the User through the Web Client.

###ListDevices
Return a list of all devices currently known by the system to the User.

###ViewSystemEvents
Return a log of recent events that have occured in the system. An event is when the state of
a device changes.

###GetSystemStatus
Return the status of the system to the user. This includes information such as what mode is the
system currently operating in, current version number, number of connected devices, etc.

###SetSystemMode
Set the mode of the system. The different modes are: Standy(0x00), Normal(0x01), and Learning(0x02)

###AddNewDevice
Add a new device to the system. This allows the end user to connect a new device to be controlled
by the system and contribute to the machine learning.

###RemoveDevice
Remove a device from the system. This allows a user to remove a device and its information, no 
longer allowing it to be controlled by the system. If added back to the system, there will be no
stored information on it.

###GetDeviceState
Return the current state of a device to a user. The state information could include if it is on,
off, and other values depending on the device.

###SetDeviceState
Set the current state of a device. The state information could include if it is on, off, and other
values depending on the device.


8.3 Server Request
------------------

![](./ServerRequest.png)
The ServerRequest diagram shows the workflow that occurs when an end user wants to retrieve
information about the state of the communication server through the web client. 

8.4 Device Request
------------------

![](./DeviceRequest.png)
The DeviceRequest diagram shows the workflow that occurs when an end user wants to retrieve 
inform about a specific device in the system through the web client. 
