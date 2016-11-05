### Coffee Automation

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

####  System Requirements {-}

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

The house is setup with a motion sensor outside the user's room (MotionRoom), a motion sensor 
outside the bathroom (MotionBathroom), a motion sensor outside the kitchen (MotionKitchen) 
and, a smart coffee machine in the kitchen (Coffee). 

The user wakes leaves their room and heads towards the bathroom at 7:00 AM. 
MotionRoom sends a motion detected message to the hub. The hub logs that MotionRoom detected 
motion at 7:00:00 AM. MotionBathroom then sends a motion detected message to the hub. The 
hub then logs that MotionBathroom detected motion at 7:00:25. The user then leaves the bathroom
and heads back to their room. MotionBathroom sends a motion detected message to the hub. The
hub logs MotionBathroom detected motion at 7:15:00 AM. MotionRoom then sends a motion detected
message to the hub. The hub logs MotionRoom detected motion at 7:15:25 AM. The user then heads
from their room to the kitchen. MotionRoom sends a moition detected message to the hub. The hub 
logs MotionRoom detected motion at 7:20:00 AM. MotionKitchen sends a motion detected message to the
hub and the hub logs MotionKitchen detected motion at 7:21:00. The user then turns on the 
coffee maker. Coffee sends a start brewing message to the hub at 7:21:30. When the coffee is done,
Coffee sends a done message to the hub. The hub logs that Coffee finished at 7:27:30. 
 

##### Logs {-}

The logs for the above scenario would look like the following:

```
2016-11-4 7:00:00 MotionRoom: Motion Detected
2016-11-4 7:00:25 MotionBathroom: Motion Detected
2016-11-4 7:15:00 MotionBathroom: Motion Detected
2016-11-4 7:15:25 MotionRoom: Motion Detected
2016-11-4 7:20:00 MotionRoom: Motion Detected
2016-11-4 7:21:00 MotionKitchen: Motion Detected
2016-11-4 7:21:30 Coffee: Starting
2016-11-4 7:27:30 Coffee: Done
```


##### Alternate Sequences {-}

There are a few different ways that the coffee maker could be setup to make coffee instead of 
being turned on manually. It could be scheduled to start at a specific time or it could be started
by the user when they get up through the web UI. The difference in the logs for both these cases
is simply when the log for the coffee starting and coffee done apear. 



##### Expected Learning {-}

The 


