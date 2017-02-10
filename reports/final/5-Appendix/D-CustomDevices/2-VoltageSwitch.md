### D-2 Variable-Voltage Switch {- #D-1}

The characteristics of variable-voltage switches vary significantly depending on the type of device
that the switch is expected to control (DC vs AC).

#### Controlling DC power {-}

If the type of device being controlled requires DC power input, the amount of power supplied to the
device can be controlled using pulse-width modulation (PWM). A digital output is used to create a
square wave. By varying the frequency of the square wave, it is possible to simulate the application
of a steady voltage between the pin's high and low voltages.

Limitations to simple PWM

- Power available to the device is limited by the power supplied by the controlling device - Limited
to DC devices

##### Expertise Required {-}

Minimal expertise is required to use PWM to control a device. The circuits required are as simple as
the circuits required to power a simple LED.

##### Reliability {-}

Simple PWM circuits are limited to controlling devices with low power requirements. While the
technique is reliable for devices which meet the power requirements, such as LED lamps, the power
requirements of most home devices means that the applicability of this technique will be severely
limited. Most devices are intended to be connected to a wall socket, meaning that they are expecting
AC current, which a significantly higher amount of power than is available from a microcontroller
such as an Arduino.

#### Controlling AC power {-}

##### Expertise Required {-}

- Safety concerns: Controlling devices which expect to receive the voltages available from
 a wall socket means dealing with high voltages. Without any team members trained in using high
 voltages, building a device to control high voltages is a very serious safety risk.

- Lack of trusted tutorials: For most of the circuits considered during this research, it has
 been possible to find tutorials online from trusted sources, such as the official Arduino website.

##### Level of Effort {-}

- When it was possible to find a tutorial online for building a circuit to control AC
 voltages, the circuit was found to be much more complex than the simple light switch circuit. Due
 to the amount of time required to fully understand these circuits, it is estimated that effort
 required is high.

| Feature            | Custom     | GE Z-Wave Plugin-in Smart Dimmer | Philips Hue Dimmer Switch | Lutron Caseta Wireless Plugin-In Lamp Dimmer |
| -------            | ------     | -------------------------------- | ------------------------- | -------------------------------------------- |
| Compatible Devices | AC devices | AC devices                       | Philips Hue Products      | AC Devices                                   |
| Interfaces         | _          | Z-Wave                           | ZigBee                    | Lutron Integration Protocol                  |

#### Evaluation {-}

| Criterion          | Score |
| ---------          | ----- |
| Expertise Required | High  |
| Level of Effort    | High  |
| Quality Comparison | Equal |

Note: There are safety concerns for custom-building this device