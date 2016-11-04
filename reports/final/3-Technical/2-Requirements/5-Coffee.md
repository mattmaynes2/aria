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


