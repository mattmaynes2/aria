# 3. Efficient Lights and Temperature

3.1 Background
--------------

Smart home should reduce your energy bills and keep you comfy. During your work week, your home
is left to cool during the day when no one is home. In the evening, before you arrive, the
system heats the house to a comfortable temperature. As you arrive home, the lights automatically
turn on in the rooms that you will enter. Later in the evening, the system cools the house to a
comfortable sleeping temperature and dims the lights.

On the weekend, the house remains warm during the day while you are home. If you leave then
to go to a store, the system turns off all the lights and lowers the temperature. When your
arrive home again the system turns the lights back on and raises the temperature.

In the summer months, when it is more light outside, the system does not turn the home's lights
on until later. In the winter months, the home turns the lights on earlier.


3.2 System Interaction
----------------------

The system will need to interact with a multiple sensors as well as light and temperature
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

3.3 System Requirements
-----------------------

To enable light and temperature control, sensors will be needed to observe the system. The
sensors will be needed to observe the ambient light and temperature of the home. There
will also need to be sensors to determine the occupancy of the home. The following is a list of
sensors that will be needed for this scenario.

| Sensor             | Usage                                                    |
| ------             | -----                                                    |
| Light Sensor       | Used to determine the amount of light in the home        |
| Temperature Sensor | Need to observe the temperature of the home              |
| Motion Sensor      | Will provide information about the occupancy of the home |

To enable this scenario, the system will need to be able to control a number of devices. The system
will need to have control of the home's lights and thermostat. In addition to having the devices in
the system, the system's user interface will need to provide control mechanisms for the device.
The following is a list of the devices that will be needed and how they will be used in the system.

| Device                | Usage                                                    |
| ------                | -----                                                    |
| Smart Lights          | Lights that can be controlled through an API             |
| Thermostat Controller | A device that can control the temperature through an API |
