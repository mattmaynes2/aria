### A-4 Apple HomeKit {- #A-4}

#### Description {-}

Apple HomeKit allows users to control their smart devices using their iPad or iPhone. Apple HomeKit
does not require any central hub to control the devices, but does require there to be Apple device
connected to the network at all times. If a user wants to control devices with an iPhone while not
at home, the devices must be connected to an Apple product that is connected to the network, such
as an iPad or Apple TV.

#### Technical Overview {-}

The smart devices are able to be scheduled and controlled in groups from the app.

##### Communication Protocol {-}

Apple HomeKit uses WiFi as the only communication protocol.

##### Device Discovery and Setup {-}

Adding new devices is done through the app. Once a device is connected to the network
it can be added to the home through Apple's app, some devices require some configuration
in their manufacturers apps.

##### Network {-}

HomeKit uses the homes WiFi network to connect devices and all devices on the network are 
able to communicate with one another.

##### API {-}

| Feature                               | Supported |
| ---------                             | --------  |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |

#### Summary {-}

There are a few aspects of the Apple HomeKit that are not ideal for incorporation into our project.
First, it is Apple exclusive, which goes against the goal of having many third party support
options. The lack of a central hub also makes it difficult to having support for many different
types of devices. The level of communication between devices that is offered by the Apple solution
is a desirable feature, but will be difficult to achieve while maintaining diverse third party
support.



[^A-4-1]: "Use the home app on your iPhone, iPad, and iPod touch," Apple Support, 2016. [Online]. Available: <https://support.apple.com/en-ca/HT204893>. Accessed: Oct. 10, 2016.



