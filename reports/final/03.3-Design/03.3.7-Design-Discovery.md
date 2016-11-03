## 7. Discovery

### 7.1 Overview

In order to add a device to the central exchange hub registry, the device must be added through
the discovery sequence. Until the device has been added, no communication can take place. Device
discovery can be initiated from external devices or from the hub itself. This section outlines the
discovery sequence in both scenarios.

### 7.2 User Driven Discovery

User initiated discovery begins with the user requesting the server to send a discovery request.
The message then propagates through the system to the communication server which sends a broadcast
discovery message to find new devices. If a device receives a request to be discovered then it
begins the device [driven discovery sequence](#7.3-Device-Driven-Discovery)

![](./UserDrivenDiscovery.png)

### 7.3 Device Driven Discovery

Device initiated discovery begins with an initial discovery request sent from the device. The
hub will receive a request for the discovery with device details. If the device has valid
information then the request is propagated to the web client. Once the web client receives a
notification that a new device is available, it prompts to user to add the device. The user can
then choose to accept or reject the device which will send a message to the device.

![](./DeviceDrivenDiscovery.png)




