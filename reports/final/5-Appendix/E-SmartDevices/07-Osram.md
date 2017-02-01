### E-7 Osram LIGHTIFY {- #E-7}

#### Description {-}

LIGHTIFY is a line of lighting products which are can be controlled using 
the LIGHTIFY mobile app. LIGHTIFY provides two separate product lines; LIGHTIFY Pro
and LIGHTIFY Home. LIGHTIFY Pro products are designed to be highly scalable for
office environments. This research focuses on the LIGHTIFY Home line of products.

The LIGHTIFY system consists of a gateway device which connects to all of the bulbs installed
in the home. Using the LIGHTIFY app, a homeowner can control connected lights from a 
mobile device.

#### Available Devices {-}

1. Surface Light TW
- Dimmable
- Adjustable colour temperature
- White only

2. Surface Light W
- Dimmable
- White only

3. Flex RGBW
- RGB colour control
- Adjustable colour temperature
- Dimmable

#### Technical Overview {-}

LIGHTIFY products use the ZigBee protocol for communication between the gateway and 
lighting products. The gateway connects to a local Wifi network, allowing the 
LIGHTIFY app to control the system over the Internet.

Due to the use of the open ZigBee protocol, LIGHTIFY products can be controlled using any 
ZigBee controller

The LIGHTIFY gateway also provides a RESTful API for controlling lights over internet. One
notable limitation of the LIGHTIFY API is that it is a cloud-only API. This means that 
the LIGHTIFY gateway is strongly tied to a homeowner's LIGHTIFY account; Osram does not 
document any local-only API for controlling devices using a gateway

#### Research Attributes {-}

| Inputs                    | Outputs            | Developer Support    | Protocol | API Restrictions                   |
| ------                    | -------            | -----------------    | -------- | ----------------                   |
| on/off                    | on/off             | REST API description | ZigBee   | REST API is Cloud Only             |
| colour                    | colour             | Sample Application   |          | REST API requires LIGHTIFY account |
| colour temperature        | colour temperature | No Official SDKs     |          | REST API requires a hub            |
| brightness                | brightness         |                      |          |                                    |
| saturation                | saturation         |                      |          |                                    |
| transition time (effects) | transition time    |                      |          |                                    |


