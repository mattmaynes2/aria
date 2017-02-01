### A-2 Wink {- #A-2}

#### Description {-}

Wink Hub is a hub that specializes in allowing communication between many different smart devices.
Wink supports control of devices using scheduling and IFTTT.

#### Technical Overview {-}

Wink is a central hub that supports most of the popular communication protocols for home automation,
giving users the freedom of connecting and controlling a variety of smart devices in one system.

##### Communication Protocol {-}

Wink Hub supports the following communication protocols:

- WiFi
- Bluetooth smart (BLE)
- Z-Wave Plus
- ZigBee
- Lutron's Caseta
- Kidde

##### Device Discovery and Setup {-}

Supporting many different manufacturers means that there are a variety of different ways for
devices to connect to the Wink Hub. The two most common ways are:

##### 1) Button Pressing {-}

Pressing a button on the Wink Hub broadcasts a pairing signal across the network. Any new device
that receives this signal will then appear on the network, and can be viewed from the Wink app. The
user then selects the new device and enters the device ID (located on the physical device) to add
it to the automation system. 

##### 2) Manufacturer Setup {-}

The new device must be added to the home network using the app provided by the manufacturer. Once
it has been added through the manufacturers app, it will be visible using the Wink app. It can be
added to the automation system from here using the Wink app.

##### Network {-}

The Wink system uses a central hub to connects different devices. Devices communicate only with the
central hub.

##### API {-}

Wink provides a RESTful service through the Wink hub and a secondary partner PubNub.

| Feature                               | Supported |
| ---------                             | --------  |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |

##### Third Party Integrations {-}

Wink has support for the following manufacturers:

|           |             |                     |             |         |
| ---       | ---         | ---                 | ---         | ---     |
| Nest      | Philips     | GE                  | Leviton     | Rheem   |
| Honeywell | TCP         | Kidde               | Kwiset      | Lutron  |
| Rachio    | Bali        | Amazon              | Andersen    | Canary  |
| Carrier   | Chamberlain | Commercial Electric | Cree        | Dropcam |
| Ecobee    | Emerson     | GoControl           | Hampton Bay | IHome   |
| Leaksmart | Osram       |                     |             |         |

#### Summary {-}

Providing support for the most popular communication protocols allows Wink to connect with almost
any device a user can purchase, making them an attractive option to consumers. This is a feature
that we hope to mimic, although not to the full extent of Wink. Specifically, the methods of
connecting devices from any manufacturer will likely be useful to us for this project.


[^A-2-1]: "Wink API · Apiary,". [Online]. Available: <http://docs.winkapiv2.apiary.io/#reference/oauth/obtain-access-token>. Accessed: Oct. 9, 2016.
[^A-2-2]: "Wink FAQ - Wink@Home Wiki," 2015. [Online]. Available: <http://wiki.winkathome.net/Wink_FAQ>. Accessed: Oct. 6, 2016.
[^A-2-3]: "A simpler smart home," Wink, 2016. [Online]. Available: <http://www.wink.com/help/faq/>. Accessed: Oct. 8, 2016.


