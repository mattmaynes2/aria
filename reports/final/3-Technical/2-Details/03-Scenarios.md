### Scenarios {#sec-3-2-3-1}

To better understand the motivations for using the learning home automation system,
scenarios outlining expected behaviours have been developed. These scenarios are designed to
examine use cases of the Aria system. The intent of these scenarios is to explore what ways
the system could be used, uncover potential areas of concern and to help reason about the technical
operations of the system. In particular, each scenario has been coupled with a set of example
data that will be used to better understand the data requirements of the system. These samples
scenario sequences can be found in [Appendix G](#G).

The following scenarios are isolated example usages of the system. Each provides a brief
description of the scenario, followed by the details about the interactions and features the
scenario will require from the system

#### Music Automation {- #sec-3-2-3-2}

###### Background {-}

Smart home automation should make your life easy and fun. Imagine a group of people arrive at your
house for a party. Your home automation system has learned how to set up your environment to give
you the best experience possible. The lights dim, the temperature goes down, and the music goes up.
Your home is now ready for your guests! The sample data for this scenario can be found in
[Appendix G-1](#G-1).

###### System Interaction {-}

The home automation system will be able to interact with a music system. The remote interface will
allow the user to turn on and off music and control the system volume. The system may also be able
to control the specific speakers that are active and playing music.

The user may choose to schedule the operation of music within the home to start at a certain date
or time. Alternatively, the user may train the system that when many people enter the home then
music should start playing at a certain volume. This could be accomplished by entering training
mode, having a large number of people enter the room and then turning on music. Motion sensors would
be required to measure the occupancy of the home to enable this learning.

Using a similar method to the music training, the user could train the system to tune the
temperature, lights, and any other devices they wish. This could indicate to the system that
when there are many people in the home, all of the trained systems should be activated.

###### System Requirements {-}

To be able to monitor the home, the following sensors may be of interest. These sensors will be
use to monitor the occupancy of the home as well as determine the noise level of the home to
appropriately adjust the music.

| Sensor             | Usage                                                      |
| ------------------ | ---------------------------------------------------------- |
| Beam Motion Sensor | 2 Beam sensors in series can be used to estimate occupancy |
| Audio Sensor       | Audio sensor for tuning music volume to the atmosphere     |
| PIR Motion Sensor  | A PIR motion sensor can detect activity in a room          |

The system will require some devices to be able to produce the desired outputs. The following
table lists example devices to allow this system to perform the tasks outlined in this
scenario.

| Device              | Usage                                               |
| ------------------- | --------------------------------------------------- |
| Speakers            | Controllable speakers for home configuration        |
| Controllable Lights | Lights that can be controlled by the central system |
| Thermostat          | Allows temperature to be adjusted                   |


#### Efficient Lights and Temperature {- #sec-3-2-3-3}

###### Background {-}

A smart home should reduce your energy bills and keep you comfy. During your work week, your home
is left to cool during the day when no one is home. In the evening, before you arrive, the
system heats the house to a comfortable temperature. As you arrive home, the lights automatically
turn on in the rooms that you will enter. Later in the evening, the system cools the house to a
comfortable sleeping temperature and dims the lights.

On the weekend, the house remains warm during the day while you are home. If you leave then
to go to a store, the system turns off all the lights and lowers the temperature. When you
arrive home again the system turns the lights back on and raises the temperature.

In the summer months, when it is more light outside, the system does not turn the home's lights
on until later. In the winter months, the home turns the lights on earlier. The sample data
for this scenario can be found in [Appendix G-2](#G-2).

###### System Interaction {-}

The system will need to interact with multiple sensors as well as light and temperature
controllers. The remote interface will need to be able to display the state of all the sensors
in the system. The remote will also need to offer control of the other devices in the system.

The system will also be able to be trained to obtain the desired output. To be able to have the
lights turn off when the user leaves the room, the user could enter training mode with the
lights on, leave the room and then turn off the lights. If this interaction was repeated, then the
system might learn this behaviour.

For the system to learn the desired temperature that the user desired, the learning process may
be much longer. At different times of day, the user will change the temperature. As environmental
factors changes, the system will make these observations and use them to decide what the should
be set to.

###### System Requirements {-}

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

#### Coffee Automation {- #sec-3-2-3-4}

###### Background {-}

Routine tasks done on a periodic schedule and can be automated by a smart process. Every morning
you wake up and make a pot of coffee before you go about your day. Making a pot of coffee is a
task that can be handled automatically by the smart home system. The system should learn when
you wake up and make your coffee for you.

Let's imagine that on the weekend you don't make any morning coffee, the system should learn this
behaviour and adapt during the days of the week. On a day that you are not at home, the system
should not make any coffee either. The sample data for this scenario can be found in
[Appendix G-3](#G-3).

###### System Interaction {-}

The system will need to be able to interact with a number of sensors to detect the user's
presence. The system will also need to be able to communicate to a smart coffee maker so that it
can observe when it is running as well as turn it off and on. The system will also need to be
able to differentiate between the different days of the week and the time of day.

To train the system, the user could put the system into training mode and then get
into bed. The user could then get out of bed and go directly to the kitchen and make a pot
of coffee. The system could observe the user's leaving the bed with motion sensors and track
that they are making coffee in a smart coffee maker.

###### System Requirements {-}

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


#### Effortless Home Lighting {- #sec-3-2-3-5}

###### Background {-}

A learning smart home should reduce the need to manually perform everyday environmental control 
tasks. The system should be able to take in information from multiple sensors and devices, and be
able to adjust the home environment based on that information. 

The homeowner enters their home office on a bright afternoon, and the lights remain turned off. 
They continue working through the afternoon and into the evening. As the sun begins to set, the lights
in the room turn on at a low intensity to maintain the current level of brightness. The lights continue
to increase in brightness as the sun continues to set, without any interaction from the person in the
room. When the homeowner exits the room, the lights shut off.

At the same time the following day, the home owner re-enters the office. The weather outside is dark
and rainy. The lights turn on to a comfortable brightness level upon entry, and remain there as
the home owner works into the evening again. Upon exiting the room, the lights shut off again.
The sample data for this scenario can be found in [Appendix G-4](#G-4).

###### System Interaction {-}

The system is required to combine information about the external environment with information about
the homes internal environment. Simply tracking any one factor will not result in the system 
being able to perform this scenario, as the required device output does not correspond linearly to
any one input.

Having the external environment be a factor in this scenario makes it hard to train the system 
to specifically do this, as you cannot easily control the external light levels. However, assuming the
home owner keeps the light in the room at a certain level while the system is learning, the behaviour
should be able to be learned.

###### System Requirements {-}

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


