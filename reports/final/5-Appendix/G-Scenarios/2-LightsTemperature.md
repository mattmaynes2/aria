### G-2 Efficient Lights and Temperature {- #G-2}

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

The system will continue to pick up patterns as it learns. The system may begin to relate days
of the week to certain events and rely less on the motion sensors. If the user was to consistently
wake up at 7:00 AM and turn the lights on every Monday then the system may always turn the lights
on at that time on Monday regardless of motion. These other factors will need to be considered
while designing this system.


