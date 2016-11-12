### Deployment {#section-3-4-3}

![](./uml/SystemDeployment.png)

##### Smart Hub {-}

The central point of control of this smart home system is the smart hub. This hub is the central
point of communication for all devices in the smart home system. It houses all of the data
storage for events in the system and makes decisions using a smart learning algorithm. The hub
will provide a minimal hardware interface for starting the system and changing the system state
from training to normal to standby. The smart hub needs to be connected to a internet access
point in order for it to serve the web interface to a client's computing device.

##### Smart Device {-}

In this diagram, smart device refers to any smart device in the system. This could be a custom
built device or a third party device. There will be many of these devices within the system all
communicating to the central smart hub.

##### Web Client {-}

The web client is the end user's browser and will present a remote interface for controlling the
smart hub as well as all devices that are connected to the system. The web interface must be able
to render on various industry standard browsers (Chrome, Firefox, IE, Safari).


