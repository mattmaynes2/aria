## Accomplishments

##### Discovery of Devices {-}

The user is able to add devices to the system by connecting them to the network and following the 
discovery sequence. Discovery is different for different devices and protocols. The system is able 
to automatically discover Z-Wave devices using the OpenZWave library. Once a device is discovered it
is registered to the system.

##### Device Displayed in User Interface {-}

All devices that are registered in the system are visible from the user interface. The remote web 
client provides observability for the specific devices in the system as well as their currently
reported status. Some basic metadata including name, manufacturer and protocol is also displayed to 
the user.

##### Device Controlled through User Interface {-}

All devices that are visible in the user interface which have a controllable attribute, such as the
brightness level on a light bulb, can be controlled. The method for controlling these attributes 
depends on the type of the data being changed. For example, a binary value such as On/Off is
controlled with a toggle button, the volume of a speaker is controlled with a slider, and the colour
of a light bulb is controlled with a colour picking graphic.

##### Events Displayed in User Interface {-}

The user interface currently uses push notifications to receive events as they are logged in the 
system. These events are generated automatically by the devices connected to the system. These
events are then immediately displayed to the user in real time on a live updating event feed.

##### Discovery of Devices from User Interface {-}

The user interface provides a mechanism for launching an automated discovery probe. This
process kicks off discovery for any devices to be added to the system. If any new devices are
added to the system during this process, the user is notified and the user interface is updated.

##### Record Training Session {-}

The user is able to create a behaviour which it wants the system to learn. They are then able to 
start a training session for this new behaviour. While a training session is in progress, all device
events that occur are associated to that session. The result of this training is a model which can
be used to make a basic decision.


