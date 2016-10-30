# 7. Discovery

## 7.1 Overview

In order to add a device to the central exchange hub registry, the device must be added through
the discovery sequence. Until the device has been added, no communication can take place. Device
discovery can be initiated from external devices or from the hub itself. This section outlines the
discovery sequence in both scenarios.

## 7.2 Device Initiation

Device initiated discovery begins with an initial discovery request sent from the device. The
hub will receive a request for the discovery with device details. If the device has valid
information then it can be added to the hub. The hub will then respond to the device with an
acknowledgement of the discovery.

![](./DiscoverySequence.png)




