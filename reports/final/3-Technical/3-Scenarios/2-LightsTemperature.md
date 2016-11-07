### Efficient Lights and Temperature {#section-3-3-2}

#### Background {-}

A smart home should reduce your energy bills and keep you comfy. During your work week, your home
is left to cool during the day when no one is home. In the evening, before you arrive, the
system heats the house to a comfortable temperature. As you arrive home, the lights automatically
turn on in the rooms that you will enter. Later in the evening, the system cools the house to a
comfortable sleeping temperature and dims the lights.

On the weekend, the house remains warm during the day while you are home. If you leave then
to go to a store, the system turns off all the lights and lowers the temperature. When your
arrive home again the system turns the lights back on and raises the temperature.

In the summer months, when it is more light outside, the system does not turn the home's lights
on until later. In the winter months, the home turns the lights on earlier.


#### System Interaction {-}

The system will need to interact with multiple sensors as well as light and temperature
controllers. The remote interface will need to be able to display the state of all the sensors
in the system. The remote will also need to offer control of the other devices in the system.

The system will also be able to be trained to obtain the desired output. To be able to have the
lights turn off when the user leaves the room, the user could enter training mode with the
lights on, leave the room and then turn off the lights. If this interaction was repeated then the
system might learn this behaviour.

For the system to learn the desired temperature that the user desired, the learning process may
be much longer. At different times of day the user will change the temperature. As environmental
factors changes, the system will make these observations and use them to decide what the should
be set to.

#### System Requirements {-}

To enable light and temperature control, sensors will be needed to observe the system. The
sensors will be needed to observe the ambient light and temperature of the home. There
will also need to be sensors to determine the occupancy of the home. The following is a list of
sensors that will be needed for this scenario.

| Sensor             | Usage                                                    |
| ------------------ | -------------------------------------------------------- |
| Light Sensor       | Used to determine the amount of light in the home        |
| Temperature Sensor | Need to observe the temperature of the home              |
| Motion Sensor      | Will provide information about the occupancy of the home |

To enable this scenario, the system will need to be able to control a number of devices. The system
will need to have control of the home's lights and thermostat. In addition to having the devices in
the system, the system's user interface will need to provide control mechanisms for the device.
The following is a list of the devices that will be needed and how they will be used in the system.

| Device                | Usage                                                    |
| --------------------- | -------------------------------------------------------- |
| Smart Lights          | Lights that can be controlled through an API             |
| Thermostat Controller | A device that can control the temperature through an API |

#### Sample Sequence {-}

###### Setup {-}

The home is setup with multiple smart lights (SmartLights) for each room and a smart thermostat
(SmartThermostat). Motion sensors are added to the main rooms (MotionBedroom, MotionKitchen,
MotionDen) in the home to detect presence. Finally, to detect the ambient light per room, light
sensors are added in conjunction with the motion sensors (LightBedroom, LightKitchen, LightDen).

###### Training Sequence {-}

The user starts the day by turning on the lights in the bedroom at 7:00:00 AM. LightBedroom sends
a notification to the central hub that the light levels have changed in the room and MotionBedroom
sends a motion message to the hub. The hub logs these interactions at 7:00:25 AM.

The user then goes to the den to change the temperature to 22°C at 7:12:00 AM. On the way, the
user turns on the den lights. MotionBedroom and MotionDen track the movement and send it to the
hub. LightDen sends a message to the hub that it has been turned on and SmartTemperature sends
the user's input to the hub as well. The hub receives the motion messages at 7:11:40 AM and
7:11:50 AM followed by the den lights at 7:12:05 AM and the temperature change at 7:12:25 AM.

The user then returns to the bedroom and prepares to leave for the day. MotionBedroom again
sends a notification that the user is moving in the bedroom from 7:14:00 AM to 7:30:00 AM.
The user then leaves the bedroom and turn the light off on the way out. MotionBedroom stops
sending motion requests and LightBedroom sends a message that it has been turned off.
The user then heads to the kitchen and turns on the lights to make breakfast. MotionKitchen
and LightKitchen send messages to the hub that they have been activated at 7:30:25 AM and
7:30:40 AM. MotionKitchen continues to send motion events from 7:31:00 AM to 7:45:00 AM.

Once the user is done breakfast they are ready to leave for the day. The user turns off the
lights in the kitchen and walks to the den. MotionKitchen stops sending messages and
LightKitchen signals that it has been turned off. In the den, the user lowers the temperature
back to 20°C and turns off the den lights before leaving. MotionDen beings sending messages
at 7:45:25 AM while SmartThermostat notifies that it has been changed. As the user leaves,
MotionDen stops sending motion notifications and LightDen indicates that it has been turned off.

##### Alternate Sequence {-}

The user has the option to program all of the smart devices through the web user interface on
a predefined schedule. They can choose to select the desired temperatures throughout the day
as well as when the lights should turn off and on. Optionally, the user can manually set values
through the web UI in real-time without a pre-configured schedule. These events will be logged
as if the user was manually interacting with the physical device.

##### Expected Inputs {-}

The log for this scenario is shown below. This log demonstrates the interactions that would
be logged. Please not that duplicate messages have been omitted and replaced with `...`.

```
2016-10-08 7:00:00 MotionBedroom: Motion Detected
2016-10-08 7:00:25 LightBedroom: Light On
2016-10-08 7:11:40 MotionBedroom: Motion Detected
2016-10-08 7:11:50 MotionDen: Motion Detcted
2016-10-08 7:12:05 LightDen: Light On
2016-10-08 7:12:25 SmartThermostat: Change Temperature 22°C
2016-10-08 7:14:00 MotionBedroom: Motion Detected
...
2016-10-08 7:29:50 MotionBedroom: Motion Detected
2016-10-08 7:29:55 LightBedroom: Light Off
2016-10-08 7:30:00 MotionBedroom: Motion Detected
2016-10-08 7:30:25 MotionKitchen: Motion Detected
2016-10-08 7:30:40 LightKitchen: Light On
2016-10-08 7:31:00 MotionKitchen: Motion Detected
...
2016-10-08 7:44:50 MotionKitchen: Motion Detected
2016-10-08 7:44:55 LightKitchen: Light Off
2016-10-08 7:45:00 MotionKitchen: Motion Detected
2016-10-08 7:45:10 MotionDen: Motion Detected
2016-10-08 7:45:25 SmartThemostate: Change Temperature 22°C
2016-10-08 7:45:30 MotionDen: Motion Detected
2016-10-08 7:45:40 LightDen: Light Off
2016-10-08 7:45:45 MotionDen: Motion Detected
```


##### Expected Behaviour {-}

The user wakes up and gets out of bed at 7:10:00 AM. MotionBedroom detects this motion and the
hub notifies the LightBedroom turns on at 7:10:05 AM. The hub also notifies the SmartThermostat
to change its temperature to 22°C at 7:10:10 AM. The user then gets ready for the day and
leaves the bedroom at 7:38:00 AM and heads to the kitchen. MotionBedroom stops sending
movement notifications at 7:38:00 AM and MotionKitchen starts at 7:38:15 AM. The hub notifies
LightBedroom to turn off at 7:40:00 AM and LightKitchen to turn on at 7:38:20 AM.

The user makes and eats breakfast and leaves at 7:48:00 AM. All motion sensors stop logging
motion. The hub turns off LightKitchen and sets the SmartThermostat to 20°C at 7:50:00 AM.

![][scenario-light-temperature-sequence]

The system will continue to pick up patterns as it learns. The system may begin to relate days
of the week to certain events and rely less on the motion sensors. If the user was to consistently
wake up at 7:00 AM and turn the lights on every Monday then the system may always turn the lights
on at that time on Monday regardless of motion. These other factors will need to be considered
while designing this system.


