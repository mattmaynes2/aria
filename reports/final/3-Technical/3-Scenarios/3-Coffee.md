### Coffee Automation {#3-3-3}

#### Background {-}

Routine tasks done on a periodic schedule and can be automated by a smart process. Every morning
you wake up and make a pot of coffee before you go about your day. Making a pot of coffee is a
task that can be handled automatically by the smart home system. The system should learn when
you wake up and make your coffee for you.

Let's imagine that on the weekend you don't make any morning coffee, the system should learn this
behaviour and adapt during the days of the week. On a day that you are not at home, the system
should not make any coffee either.

#### System Interaction {-}

The system will need to be able to interact with a number of sensors to detect the user's
presence. The system will also need to be able to communicate to a smart coffee maker so that it
can observe when it is running as well as turn it off and on. The system will also need to be
able to differentiate between the different days of the week and the time of day.

In order to train the system, the user could put the system into training mode and then get
into bed. The user could then get out of bed and go directly to the kitchen and make a pot
of coffee. The system could observe the user's leaving the bed with motion sensors and track
that they are making coffee in a smart coffee maker.

#### System Requirements {-}

To track the user's motion in the home, the system will need motion sensors. To be able to
differentiate between the days of the week and time, the system will also need access to a
clock and a calendar. The following is a list of sensors that will be required for this
interaction.

| Sensor         | Usage                                                        |
| -------------- | ------------------------------------------------------------ |
| Motion Sensors | Used to track user movement throughout the home              |
| Clock          | Used to determine the time of day that the user makes coffee |
| Calendar       | Used to determine what day of the week the user makes coffee |

To be able to actually make the coffee, a smart coffee maker will be needed. This is the only
smart device that will be required to automate this scenario.

#### Sample Sequence {-}

###### Setup {-}

The home is setup with a motion sensor outside the user's bedroom (MotionBedroom), a motion sensor
outside the bathroom (MotionBathroom), a motion sensor outside the kitchen (MotionKitchen)
and, a smart coffee machine in the kitchen (SmartCoffee).

###### Training Sequence {-}

The user wakes leaves their bedroom and heads towards the bathroom at 7:00:00 AM. MotionBedroom
sends a motion detected message to the hub. The hub logs that MotionBedroom detected motion
at 7:00:00 AM. MotionBathroom then sends a motion detected message to the hub. The hub then
logs that MotionBathroom detected motion at 7:00:25 AM.

The user then leaves the bathroom and heads back to their bedroom. MotionBathroom sends a motion
detected message to the hub. The hub logs MotionBathroom detected motion at 7:15:00 AM.
MotionBedroom then sends a motion detected message to the hub. The hub logs MotionBedroom detected
motion at 7:15:25 AM.

The user then heads from their bedroom to the kitchen. MotionBedroom sends a motion detected
message to the hub. The hub logs MotionBedroom detected motion at 7:20:00 AM. MotionKitchen
sends a motion detected message to the hub and the hub logs MotionKitchen detected motion at
7:21:00 AM. The user then turns on the coffee maker. Coffee sends a start brewing message to
the hub at 7:21:30 AM. When the coffee is done, SmartCoffee sends a done message to the hub.
The hub logs that SmartCoffee finished at 7:27:30 AM.
  

##### Alternate Sequences {-}

There are a few different ways that the coffee maker could be setup to make coffee instead of
being turned on manually. It could be scheduled to start at a specific time or it could be started
by the user when they get up through the web UI. The difference in the logs for both these cases
is simply when the log for the coffee starting and coffee done appear.

##### Expected Inputs {-}

The logs for the training scenario would look like the following:

```
2016-11-04 7:00:00 MotionBedroom: Motion Detected
2016-11-04 7:00:25 MotionBathroom: Motion Detected
2016-11-04 7:15:00 MotionBathroom: Motion Detected
2016-11-04 7:15:25 MotionBedroom: Motion Detected
2016-11-04 7:20:00 MotionBedroom: Motion Detected
2016-11-04 7:21:00 MotionKitchen: Motion Detected
2016-11-04 7:21:30 SmartCoffee: Starting
2016-11-04 7:27:30 SmartCoffee: Done
```

This sequence would occur every weekday possibly with the coffee maker being scheduled on one day
and the user starting the coffee maker from the web UI. A sample 5 days of logs could look like the
following:

```
2016-11-07 7:00:00 MotionBedroom: Motion Detected
2016-11-07 7:00:25 MotionBathroom: Motion Detected
2016-11-07 7:15:00 MotionBathroom: Motion Detected
2016-11-07 7:15:25 MotionBedroom: Motion Detected
2016-11-07 7:20:00 MotionBedroom: Motion Detected
2016-11-07 7:21:00 MotionKitchen: Motion Detected
2016-11-07 7:21:30 SmartCoffee: Starting
2016-11-07 7:27:30 SmartCoffee: Done

2016-11-08 7:05:00 MotionBedroom: Motion Detected
2016-11-08 7:05:30 MotionBathroom: Motion Detected
2016-11-08 7:20:00 MotionBathroom: Motion Detected
2016-11-08 7:20:25 MotionBedroom: Motion Detected
2016-11-08-7:23:00 WebUI: Start Coffee requested
2016-11-08-7:23:10 SmartCoffee: Starting
2016-11-08 7:29:30 SmartCoffee: Done
2016-11-08 7:30:00 MotionBedroom: Motion Detected
2016-11-08 7:31:00 MotionKitchen: Motion Detected

2016-11-09 7:02:00 MotionBedroom: Motion Detected
2016-11-09 7:02:30 MotionBathroom: Motion Detected
2016-11-09 7:12:00 MotionBathroom: Motion Detected
2016-11-09 7:12:25 MotionBedroom: Motion Detected
2016-11-09 7:15:00 MotionBedroom: Motion Detected
2016-11-09 7:16:00 MotionKitchen: Motion Detected
2016-11-09 7:16:30 SmartCoffee: Starting
2016-11-09 7:22:30 SmartCoffee: Done

2016-11-10 7:00:00 MotionBedroom: Motion Detected
2016-11-10 7:00:30 MotionBathroom: Motion Detected
2016-11-10 7:12:00 Hub: Starting Scheduled Coffee
2016-11-10 7:12:02 SmartCoffee: Starting
2016-11-10 7:16:00 MotionBathroom: Motion Detected
2016-11-10 7:16:25 MotionBedroom: Motion Detected
2016-11-10 7:18:00 SmartCoffee: Done
2016-11-10 7:20:00 MotionBedroom: Motion Detected
2016-11-10 7:21:00 MotionKitchen: Motion Detected

2016-11-11 7:02:00 MotionBedroom: Motion Detected
2016-11-11 7:02:30 MotionBathroom: Motion Detected
2016-11-11 7:20:00 MotionBathroom: Motion Detected
2016-11-11 7:20:25 MotionBedroom: Motion Detected
2016-11-11 7:15:00 MotionBedroom: Motion Detected
2016-11-11 7:16:00 MotionKitchen: Motion Detected
2016-11-11 7:16:30 SmartCoffee: Starting
2016-11-11 7:22:30 SmartCoffee: Done
```

##### Expected Behaviour {-}

From the logs the Aria system should be able to tell that the user's morning consists of
going to the bathroom, going back to their room then going to the kitchen and having coffee.
The system can determine that the average time it takes the user for waking up until they get to
the kitchen is 19 minutes and a pot of coffee takes 6 minutes to make. Therefore it is expected when
the system is in playback mode that it would start the coffee maker 13 minutes after it sees that
MotionBedroom and MotionBathroom have been triggered if it is around 7:00 AM.

![][scenario-coffee-sequence]

As the system gains more and more information there could be some other patterns that the system
notices. For example it could be more accurate to only consider other mornings for the current
day of the week when calculating the average time to kitchen. For example Wednesdays the user
takes less time in the bathroom so there average time to kitchen on Wednesdays is closer to 15
minutes. The system should then on Wednesdays start the coffee maker 9 minutes after the user gets
up. There could also be factors from time of year. The users routine could change depending on the
month/season these are factors we need to consider while designing the learning algorithm.



