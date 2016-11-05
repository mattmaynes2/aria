### Effortless Home Lighting

#### Background {-}

A learning smart home should reduce the need to manually perform everyday environmental control 
tasks. The system should be able to take in information from multiple sensors and devices, and be
able to make adjustments to the home environment based on that information. 

The homeowner enters their home office on a bright afternoon, and the lights remain turned off. 
They continue working through the afternoon and into the evening. As the sun begins to set, the lights
in the room turn on at a low intensity to maintain the current level of brightness. The lights continue
to increase in brightness as the sun continues to set, without any interaction from the person in the
room. When the homeowner exits the room, the lights shut off.

At the same time the following day, the home owner re-enters the office. The weather outside is dark
and rainy. The lights turn on to a comfortable brightness level upon entry, and remain there as
the home owner works into the evening again. Upon exiting the room, the lights shut off again.

#### System Interaction {-}

The system is required to combine information about the external environment with information about
the homes internal environment. Simply tracking any one factor will not result in the system 
being able to perform this scenario, as the required device output does not correspond linerally to
any one input.

Having the external environment be a factor in this scenario makes it hard to train the system 
to specifically do this, as you cannot easily control the external light levels. However, assuming the
home owner keeps the light in the room at a certain level while the system is learning, the behaviour
should be able to to be learned.

#### System Requirements {-}

Two different sensors are needed for this scenario. A door/window sensor would be used to detect
when someone enters the room and later leaves the room. An ambient light sensor for inside the room
will also be needed.

| Sensor         | Usage                                                    |
| -------------- | -------------------------------------------------------- |
| Light          | Used to determine the amount of light in a room          |
| Window / Door  | Will provide information about the occupancy of a room   |

To enable this scenario, the system will need to be able to change the brightness level of lights.
The following is a list of the devices that will be needed and how they will be used in the system.

| Device                | Usage                                           |
| --------------------- | ----------------------------------------------- |
| Smart Lights          | Lights that can be controlled through an API    |
|
