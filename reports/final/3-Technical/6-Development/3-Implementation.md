### Implementation {#section-3-6-3}

#### WeMo Adapter

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
