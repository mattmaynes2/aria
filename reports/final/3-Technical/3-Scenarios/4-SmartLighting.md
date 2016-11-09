### Effortless Home Lighting {#section-3-3-4}

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

Two different sensors are needed for this scenario. A passive infrared sensor would be used to detect
when there is someone present in a room. An ambient light sensor for inside the room will also be
needed.

| Sensor         | Usage                                                    |
| -------------- | -------------------------------------------------------- |
| Light          | Used to determine the amount of light in a room          |
| PIR            | Will provide information about the occupancy of a room   |

To enable this scenario, the system will need to be able to change the brightness level of lights.
The following is a list of the devices that will be needed and how they will be used in the system.

| Device                | Usage                                           |
| --------------------- | ----------------------------------------------- |
| Smart Lights          | Lights that can be controlled through an API    |


#### Sample Sequence {-}

###### Setup {-}

The home is setup with a PIR in the home owner's office (PIROffice), a light sensor in the office 
(LightOffice), and dimmable smart lights in the office (SmartLights).

###### Training Sequence {-}

The user enters their office at 2:30:00 PM on Wednesday afternoon. PIROffice sends a motion detected 
message to the hub. The hub logs that PIROffice detected motion at 2:30:00 PM. It is a sunny afternoon,
so the home owner does not turn on the lights. The owner continues working uninterrupted until 
7:45:00 PM, when the sun begins to set. The hub logs that LightOffice is reading a lower value due to
the drop in light in the office. The owner turns the lights on dimly, to maintain the previous light
level of the room, causing the hub to log that SmartLights turned on. As the light level of the room
continues to drop in the room, the owner continues to raise the brightness of the lights. The hub
continues to log this interaction. Eventually, it is dark outside and the lights are at full 
brightness in the room. 

When the owner is done working, they get up, turn off the lights, and leave the room. The hub logs
that PIROffice detected motion at 9:00:00, and logs that SmartLights turned off at 9:00:03.
  

##### Alternate Sequences {-}

The light level of a room will not always be the same at a given time of day. The owner could enter
their office at 2:30:00 PM on Wednesday afternoon, and turn the lights on immediately because it is
rainy outside. The hub would log motion detected by PIROffice at 2:30:00, and then the value of
LightOffice increasing to the desired value immediately following. This sequence would end the same
way as the primary training sequence. 

##### Expected Inputs {-}

The logs for the training scenario would look like the following:

```
Initial Sensor States
2016-11-06 14:30:02 LightOffice: 10
2016-11-06 14:30:02 SmartLights: 0
```
```
2016-11-06 14:30:00 PIROffice: Motion Detected
2016-11-06 19:39:00 LightOffice: 9
2016-11-06 19:42:00 LightOffice: 8
2016-11-06 19:45:00 LightOffice: 7
2016-11-06 19:45:10 SmartLights: 3
2016-11-06 19:45:12 LightOffice: 10
2016-11-06 19:48:00 LightOffice: 9
2016-11-06 19:51:00 LightOffice: 8
2016-11-06 19:55:00 LightOffice: 7
2016-11-06 19:55:10 SmartLights: 6
2016-11-06 19:55:12 LightOffice: 10
2016-11-06 19:58:00 LightOffice: 9
2016-11-06 20:01:00 LightOffice: 8
2016-11-06 20:05:00 LightOffice: 7
2016-11-06 20:05:10 SmartLights: 10
2016-11-06 20:05:12 LightOffice: 10
2016-11-06 21:00:00 PIROffice: MotionDetected
2016-11-06 21:00:07 SmartLights: 0
2016-11-06 21:00:08 LightOffice: 0
```

The alternate sequence could look like this:

```
Initial Sensor States
2016-11-06 14:30:02 LightOffice: 0
2016-11-06 14:30:02 SmartLights: 0
```
```
2016-11-06 14:30:00 PIROffice: Motion Detected
2016-11-06 14:30:03 SmartLights: 10
2016-11-06 14:30:06 LightOffice: 10
2016-11-06 21:00:00 PIROffice: MotionDetected
2016-11-06 21:00:07 SmartLights: 0
2016-11-06 21:00:08 LightOffice: 0
```

##### Expected Behaviour {-}

From the logs the Aria system should be able to tell that the desired light level of the owners 
office when occupied is 10. The system should automatically adjust the brightness level of the Smart
Lights to achieve this level of brightness while the home owner is in the office. Upon the owner
leaving the office, the system should recognize that the lights must be turned off. 
