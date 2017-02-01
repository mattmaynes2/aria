### A-2 Wink {- #A-2}

#### Description {-}

Wink is a smart home automation system that prides itself on simplicity. This smart home system
that prides itself on simplicity and user experience. The Wink system provides standard smart
home features such as monitoring and controlling of devices, but also offers more advanced
features such as energy consumption monitoring [^A-2-1]. Wink uses a central hub architecture,
where all devices in the network communicate to a single "smart" hub. Additionally, Wink
provides a smart phone app for users to interact with the system [^A-2-1].

#### Technical Overview {-}

##### User Interaction {-}

User interaction in the Wink system begins with its smart hub. This hub is the central point
of communication for devices in the smart home. Once devices have been added to the smart hub,
the user can control the hub and all of its devices with the Wink smart phone app [^A-2-1].
The app provides a clean, simple interface for monitoring and controlling all devices on the
smart home network. 

Additionally to the app, the Wink platform offers a custom built touch screen remote control.
The remote controller allows the user to use all of the features of the smart home without
the use of a smart phone app [^A-2-2].

In order to offer a better user experience, Wink provides a "shortcuts" feature where a user
is given the ability to control multiple devices with one command [^A-2-1]. This feature
allows users to setup and configure related devices to perform desired tasks. When the user
invokes the shortcut, the system will apply all of the user's initial configurations [^A-2-1].
The shortcut feature certainly adds value to the Wink system but does require manual
configuration to setup the desired shortcut.

##### Device Discovery and Setup {-}

Wink does not offer any of its own smart home devices. Instead, it utilizes the vast market
of existing devices by supporting various different third party integrations. Supporting many
different manufacturers means that there are two  different ways for devices to connect
to the Wink Hub. Pressing a button on the Wink Hub broadcasts a pairing signal across the network
[^A-2-5]. Any new device that receives this signal will then appear on the network, and can be
viewed from the Wink app. The user then selects the new device and enters the device identifier
(located on the physical device) to add it to the automation system.

If the new device requires a setup through a third party app then new device must be added to
the home network using the app provided by the manufacturer. Once it has been added through
the manufacturers app, it will be visible using the Wink app. It can be added to the
automation system from here using the Wink app [^A-2-5].

##### Network Configuration {-}

Wink's central hub provides several communication protocols, all of which are wireless. In
order to communicate to the hub, the user must setup a WiFi connection. This can be done
initially by connecting a smart phone to the hub's internal WiFi network and then using
the smart phone app [^A-2-5]. Once the hub has been setup to connect to a local area
WiFi network, the smart phone app can be used to control the devices connected to the hub.
If the WiFi network contains an internet link then the smart phone app can be used outside
of the home to monitor and control the home [^A-2-2].

##### Supported Communication Protocol {-}

The Wink hub offers connections to multiple different communication protocols in order
to maximize its third party integrations. As a minimum, the hub must be connected to
WiFi so that the hub can connect to the Wink smart phone app. Beyond that, the Wink hub
offers connections for Bluetooth, Z-Wave, ZigBee, Lutron's Caseta, and Kidde protocols
[^A-2-4].

##### Application Programming Interfaces {-}

Wink provides a RESTful service through the Wink hub and a secondary partner PubNub. This
API can be accessed through the Wink web server for third party integrations. The service
offers basic smart home features including monitoring and controlling devices. Wink also
offers controls for creating groups of devices that can be used for shortcuts in their
service [^A-2-3].

##### Third Party Integrations {-}

Since Wink does not make any of their own smart devices, they rely heavily on
third party integrations. The table below lists all of the organizations that have
partnered with Wink to offer devices that are compatible with the Wink system.

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
any device a user can purchase, making them an attractive option to consumers. Their central hub
design allows them to be compatible with many third party devices as well as offer the user
a simple setup experience. Finally, Wink offers a simple, elegant user interface through their
smart phone app or smart remote controller. These features make Wink an appealing smart home
automation system for a non-technical user.

[^A-2-1]: "Wink | About Us". [Online]. Available <https://wink.com/about/>. Accessed: Feb. 1, 2017.
[^A-2-2]: "Wink | Products". [Online]. Available <https://wink.com/products/>. Accessed: Feb. 1, 2017.
[^A-2-3]: "Wink API · Apiary,". [Online]. Available: <http://docs.winkapiv2.apiary.io/>. Accessed: Feb. 1, 2016.
[^A-2-4]: "Wink FAQ - Wink@Home Wiki," 2015. [Online]. Available: <http://wiki.winkathome.net/Wink_FAQ>. Accessed: Oct. 6, 2016.
[^A-2-5]: "A simpler smart home," Wink, 2016. [Online]. Available: <http://www.wink.com/help/faq/>. Accessed: Oct. 8, 2016.


