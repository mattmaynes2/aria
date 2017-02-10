### A-3 SmartThings {- #A-3}

#### Description {-}

SmartThings is Samsung's home automation system. Similar to  Wink, they provide their own app
allowing a user to control devices using scheduling or IFTTT.

#### Technical Overview {-}

##### Communication Protocols {-}

SmartThings supports devices that communicate using the Z-Wave, ZigBee, or WiFi communication
protocols

##### Device Discovery and Setup {-}

Adding a new device is done through the app. A user will click "find device", prompting the hub
to search for any new Z-Wave, ZigBee, or WiFi devices. When the device is found the user adds 
it to a room and names the device.

##### Network {-}

SmartThings uses a central Hub to connect all of the smart devices. The SmartThings app talks with
the SmartThings Cloud which talks to the Hub which then controls the devices.

##### API {-}

SmartThings provides a Groovy API to create SmartApps that allow control of devices.

| Feature                               | Supported |
| ---------                             | --------  |
| List all devices                      | Y         |
| Receive update on device state change | Y         |
| Modify device state                   | Y         |


##### Limitations {-}

Requires a SmartThings hub and connection to the SmartThings cloud.

##### Third Party Integrations {-}

|            |                     |                |                 |                    |
| ---        | ---                 | ---            | ---             | ---                |
| 2Gig       | Aeon Labs           | Amazon         | Belkin          | Bose               |
| Cree       | ecobee              | Ecolink        | EcoNet Controls | Enerwave           |
| Everspring | Fibaro              | Fidure         | First Alert     | FortrezZ           |
| GE         | Google              | Honeywell      | iHome           | Keen Home          |
| Kwikset    | Leak Intelligence   | Leviton        | LiFi Labs       | Linear             |
| Netgear    | OSO Technologies    | OSRAM LIGHTIFY | Philips Hue     | Remotec Technology |
| Samsung    | Samsung SmartThings | Schlage        | Sengled         | Skybell            |
| Spruce     | Yale                | Zen            |                 |                    |

#### Summary {-}

The Samsung home automation system provides a reasonable level of support for
different communication protocols, giving it a healthy amount of third party support.
This is something that we will be striving for in out project. The dependency on the 
connection to a cloud service is something that we would like to avoid for our project.


[^A-3-1]: "Samsung SmartThings hub FAQ — SmartThings developer documentation," 2016. [Online]. Available: <http://docs.smartthings.com/en/latest/sept-2015-faq.html>. Accessed: Oct. 6, 2016.
[^A-3-2]: "How it works," SmartThings, 2016. [Online]. Available: <https://www.smartthings.com/how-it-works>. Accessed: Oct. 10, 2016.
[^A-3-3]: "Use the home app on your iPhone, iPad, and iPod touch," Apple Support, 2016. [Online]. Available: <https://support.apple.com/en-ca/HT204893>. Accessed: Oct. 10, 2016.



