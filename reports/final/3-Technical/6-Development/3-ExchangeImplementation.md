### Exchange Implementation {#section-3-6-3}

![](./uml/EchangeClassDiagram)

#### Adapters {-}

The adapter classes are used to discover devices and communicate with them. The adapters use 
an observer observable model to notify delegates when they receive a message or discover a device. 
Each adpater is responsable for creating a Device object that can be controlled by the system 
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

The WeMo adpater is responsable for comunicating with the WeMo UPnP devices. The adapter is able
to discover new WeMo devices that are added to the system as well as create a python object from the
SOAP xml that the device provides to allow the system an  easy way of controlling the device.

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

The Database class is used to excute SQL on the sqlite database. The Database will create a 
new database if one doesn't currently exist when the Hub is started.

#### DatabaseTranslator {-}

The DatabaseTranslator transaltes evnet and request messaeges into sql and sends it to the database 
to be stored.

#### RequestTracker {-}

The RequestTracker decorates the DatabaseTranslator and filters out all requests that have the Hub 
as the destination. These can be ignored because these request are for getting information about the
system and don't need to be stored for machine learning. The RequestTracker also assosiates a request
with an event so that any changes the request made can be tracked. If a device that can be 
controlled sends   

#### Device {-}

#### DeviceType {-}

#### Attribute {-}
