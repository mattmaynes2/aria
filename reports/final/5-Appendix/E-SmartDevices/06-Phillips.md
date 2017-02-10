### E-6 Philips Hue {- #E-6}

#### Available Devices {-}

1. White Bulbs
 - On/Off 
 - Dimming

2. White Ambiance Bulbs
 - On/Off
 - Dimming
 - Supports multiple shades of white

3. Colour Ambiance Bulbs
 - On/Off
 - Dimming
 - Configurable colour

4. Lightstrips
 - Adhesive strips of LED lights
 - Dimming
 - Configurable colours
 - Dynamic lighting/colour schemes
 - White light not supported

5. Lightstrip Plus
 - Adhesive strips of LED lights
 - Dimming
 - Configurable colours
 - Dynamic lighting/colour schemes
 - Supports white light
 - Brighter than regular Lightstrips (1600 Lumen)
 - Fine-grained fading control

6. Dimmer switch
 - Battery-powered
 - Doesn't require the Hue bridge
 - Can't use it with other AC devices, no electrical contact with bulbs

7. Tap Switch
 - Powered by touch - no battery or wires
 - Hue bridge and app required

8. Hue Motion Sensor
 - Detects motion in the vicinity of a PIR sensor
 - Includes an integrated daylight sensor

#### Developing with Hue {-}

- Devices use ZigBee Light Link

- The Hue bridge is a hub device that allows lights to be controlled using WiFi. It bridges 
  the ZigBee protocol used by lights to Wifi used by apps.

- Bridge works with most standard ZigBee lights

- Hue Bridge provides a RESTful API for controlling connected lights. API is only accessible 
  when you're on the same LAN as the bridge.

#### Research Criteria {-}

Inputs and outputs differ by device type; developer support, communication protocol, and API restrictions
are common to all Philips Hue devics.

**Hue Lights**

| Inputs             | Outputs            | Developer Support                | Protocol | API Restrictions        |
| ------             | -------            | -----------------                | -------- | ----------------        |
| On/Off             | On/Off             | Tutorials on Hue website         | ZigBee   | Local Only              |
| Brightness         | Brightness         | Android, Java, IOS Official SDKs |          | REST API requires a hub |
| Hue                | Hue                | Numerous 3rd party SDKs          |          |                         |
| Saturation         | Saturation         |                                  |          |                         |
| Colour Temperature | Colour Temperature |                                  |          |                         |
| Dynamic Effect     | Dynamic Effect     |                                  |          |                         |

**Hue Motion Sensor**

| Inputs             | Outputs             |
| ------             | -------             |
| sensitivity        | presence            |
|                    | light level         |

**Hue Dimmer Switch, Hue Tap**

| Inputs             | Outputs             |
| ------             | -------             |
|                    | button event        |

