### H-1 Hub Implementation {- #H-1}

![][h-1]

#### Adapters {-}

The adapter classes are used to discover devices and communicate with them. The adapters use 
an observer observable model to notify delegates when they receive a message or discover a device. 
Each adapter is responsible for creating a Device object that can be controlled by the system 
for each new device they discover. 

##### Aria Adapter {-}

The Aria Adapter is used to communicate between the Exchange and the gateway as well as it can
communicate with any custom device we create. It uses a UDP socket that listens on port 7600.
The Aria Adapter is also a delegate on the Exchange Object and is able to push events and newly
discovered devices to the gateway. 

##### Hub Adapter {-}

The Hub adapter is used to send and receive messages for the hub. The adapter translates
the message and calls the appropriate method on the Hub.

##### WeMo Adapter {-}

The WeMo adpater is responsable for communicating with the WeMo UPnP devices. The adapter is able
to discover new WeMo devices that are added to the system as well as create a python object from the
SOAP xml that the device provides to allow the system an easy way of controlling the device.

While trying to integrate with a WeMo switch we first looked at the python `ouimeaux` library.
This library looked very promising as it had discovery and created python objects for each
device that would notify using `pysignals` if the state of the device changed. The issue with this 
library is that at the time of writing this report there is a bug with processing signals that
exists when trying to run with python version 3.4 or higher. As we are using python 3.5 for
our hub this meant that this library was therefore incompatible. 

We then looked at the `netdisco` library that provides discovery for UPnP devices. Using this 
library we are able to discover our WeMo devices but we didn't have any objects that we could use 
to control the devices. In order to create objects from the discovered devices we used the 
`pywemo` library. This library also allowed us to register to events when the devices' state 
change so we get notified and are able to log an event.

#### Database {-}

The Database class is used to execute SQL on the sqlite database. The Database will create a 
new database if one doesn't currently exist when the Hub is started.

#### DatabaseTranslator {-}

The DatabaseTranslator translates event and request messages into sql and sends it to the database 
to be stored.

#### RequestTracker {-}

The RequestTracker listens to the Exchange and decorates the DatabaseTranslator,
filtering out all requests that have the Hub as the destination. These can be ignored because these 
request are for getting information about the system and don't need to be stored for machine 
learning. The RequestTracker also associates a request with an event so that any changes the request
 made can be tracked. If a device that can be controlled sends an event and there is there was no 
request to that device a request is created by the request tracker in order for the user action to 
be tracked.   

#### Retriever {-}

The Retriever class is used to query the database and retrieve events. Currently it is possible
to query for a list of all events or a list of all events for a specified device.

#### Delegate {-}

The delegate interface is  an Observer interface. The interface implements two methods; received 
and discovered.

#### Device {-}

A device is a representation of a device that is connected to the system and can provide input or 
be controlled.

#### DeviceType {-}

The Device type represents the different types of devices that are in the system. The device type
contains information about the manufacturer of the device the protocol the device speaks and the 
different attributes that the device has.

#### Attribute {-}

Attributes represent the different attributes of a device that can be viewed and/or changed

#### DataType {-}

Data type is an enum that is used to represent the data types of device attributes. The possible 
values of this enum are:

- 'binary' 
- 'int'
- 'float' 
- 'colour'
- 'enum'
- 'time'
- 'date'
- 'string'
- 'list'

#### CLI {-}

The CLI provides a command line interface for the user to issue command directly to the hub. 
Current commands are:

- help
- exit

#### Hub {-}

The Hub is a device that contains the current system state. The Hub has a list of all of the 
devices in the system, what mode the system is currently in and is able to query the database to 
get events.

#### Exchange {-}

The Exchange is used to route messages through the system. The exchange listens to all of the 
adapters and receives all the messages that are passed through the system.

#### HubMode {-}

HubMode is an enum that contains the fdifferent modes of operation of the hub. 
The following are the possible values:

- StandBy
- Normal
- Learning
