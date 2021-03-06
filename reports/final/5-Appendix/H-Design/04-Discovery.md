### H-4 Discovery {- #H-4}

#### Overview {-}

In order to add a device to the central exchange hub registry, the device must be added through
the discovery sequence. Until the device has been added, no communication can take place. Device
discovery can be initiated from external devices or from the hub itself. This section outlines the
discovery sequence in both scenarios.

#### User Driven Discovery {-}

User initiated discovery begins with the user requesting the server to send a discovery request.
The message then propagates through the system to the communication server which sends a broadcast
discovery message to find new devices. If a device receives a request to be discovered then it
begins the device driven discovery sequence

![][h-4]

#### Device Driven Discovery {-}

Device initiated discovery begins with an initial discovery request sent from the device. The
hub will receive a request for the discovery with device details. If the device has valid
information then the request is propagated to the web client. Once the web client receives a
notification that a new device is available, it prompts to user to add the device. The user can
then choose to accept or reject the device which will send a message to the device.

![][h-6]




