Computing Devices
=================

### Background

Computing devices are any electronic device that can be used to process data and send it over
a smart home network. Computing devices include computers, micro-controllers and other
embedded devices. Computing devices that are being examined all offer control of external
hardware interfaces. This report examines computing devices that can be used for prototyping
embedded control of sensors and actuators.

### Relation to System

Computing devices will be used for many aspects of the smart home system. A computing device will
be used for the central smart hub as well as for various other devices in the system. Different
devices will be more suitable to some tasks than others. This report compares a number of these
computing options with a focus on the areas of need within the system.

Arduino Uno
-----------

### Description

The Arduino Uno is a small starter microcontroller that is intended for hobby projects and
newcomers to embedded programming. The Uno is intended for rapid prototyping of small circuits
and small embedded systems.

### Technical Overview

The Uno is a microcontroller that uses the Arduino boot loader software for launching the system
and executing code. The Uno is fully compatible with the Arduino SDK that provides simple
access to all pins and controls on the board. The Uno comes with a 8-bit ATmega328P processor
running at 16 MHz. The system comes with 32 KB of on board flash memory as well as 2 KB of SRAM
and 1 KB of EEPROM. The system boot loader occupies 0.5 KB of the flash memory capacity.

The Uno comes with 14 digital pins, 6 of which can be programmed to use pulse with modulation.
Included in the microcontroller is 6 analog to digital input pins. The board has a operating
voltage of 5 V and will accept between 7-12 V for input pins. The maximum voltage range of the
input pins are 6-20V.

The Uno is a medium sized microcontroller that is 68.6 mm long and 53.4 mm wide. It has a total
weight of approximately 25 g. The Uno also includes an integrated USB-Mini port for serial
communication and as a power source. The board includes a 5 V DC power input for running the
board continually.

##### Operation Criteria

| Criteria                   | Specification |
| --------                   | ------------- |
| Operating System           | None          |
| Processor Size             | 8-bit         |
| Processor Family           | ATmega        |
| Operating Voltage          | 5V            |
| Input Voltage              | 7-12V         |
| Clock Speed                | 16 MHz        |
| Digital Pins               | 14            |
| Pulse with Modulation Pins | 6             |
| Analog Input Pins          | 6             |
| DC Current per Pin         | 20 mA         |
| Flash Memory               | 32 KB         |
| System Size                | 0.5 KB        |
| SRAM                       | 2 KB          |
| EEPROM                     | 1 KB          |

##### Features

| Feature |          |
| ------- | ------   |
| USB     | USB-Mini |

##### Physical Characteristics

| Dimension | Length  |
| --------- | ------  |
| Length    | 68.6 mm |
| Width     | 53.4 mm |
| Weight    | 25 g    |

### Evaluation

The Ardunio Uno offers fast and simple prototyping options for quickly building embedded circuits.
This board is very useful for rapidly testing but would not be practical in a mass production
system. For the smart learning system, this board would be optimal for experimentation and
quick deployment.

### References

[1] "ArduinoBoardUno," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoardUno. Accessed: Oct. 6, 2016.

Arduino 101
-----------

### Description

The Arduino 101 is a more sophisticated board that uses the Intel Curie processor for computing.
This board leverages the Real-Time Operating System (RTOS) developed by Intel for running the
board.

### Technical Overview

The Ardunio 101 is the most feature rich board that Ardunio is offers. It comes with a full
Real-Time Operating System (RTOS) that is powered by the Intel Curie. The processor is a 32-bit,
8 MHz or 16 MHz backed by 196 KB of flash memory. The RTOS is a light weight OS that only
occupies 2 KB of memory to provide managed, concurrent applications.

The 101 comes with a number of additional features above other microcontrollers in the Arduino
family. Beyond the standard USB-Mini serial connection, the 101 offers a 6 axis gyroscope
accelerometer and integrated Bluetooth. The 101 also provides a 5 V DC power input for
deployment use.

The 101 offers many of the same prototyping capabilities as the Uno with 14 digital pins, 4
of which provide pulse with modulation. The 101 also exposes 6 analog to digital pins.

##### Operation Criteria

| Criteria                   | Specification  |
| --------                   | -------------  |
| Operating System           | RTOS           |
| Processor Size             | 32-bit         |
| Processor Family           | Intel          |
| Operating Voltage          | 3.3V - 5V      |
| Input Voltage              | 7-12V          |
| Clock Speed                | 8 MHz - 16 MHz |
| Digital Pins               | 14             |
| Pulse with Modulation Pins | 4              |
| Analog Input Pins          | 6              |
| DC Current per Pin         | 20 mA          |
| Flash Memory               | 196 KB         |
| System Size                | 2 KB           |
| SRAM                       | 2 KB           |
| EEPROM                     | 1 KB           |

##### Features

| Feature       |              |
| -------       | -----        |
| Bluetooth     | Yes          |
| USB           | USB-Mini     |
| Accelerometer | 6-Axis Gyros |


##### Physical Characteristics

| Dimension | Length  |
| --------- | ------  |
| Length    | 68.6 mm |
| Width     | 53.4 mm |
| Weight    | 34 g    |

### Evaluation

The 101 is a much more feature rich board than the Uno, however the added features are not
applicable to this project. The 101 also has a much higher price point per unit than the Uno
with no real added value. This makes the Uno a more appealing candidate for rapid prototyping
and simple circuit design.

### References

[1] "ArduinoBoard101," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoard101. Accessed: Oct. 6, 2016.


Arduino Pro
-----------

### Description

The Arduino Pro is a slim, no frills version of the Ardiuno Uno. This board requires more
technical knowledge then the Uno or the 101. All pins exposed on the Pro require soldering to
make a connection. The Pro is intended for replication of a complex circuit design with
requirements for a wide range of input and output ports.

### Technical Overview

The Pro is an embedded system that leverages the Arduino boot loader and a 32-bit ATmega328
processor. The Pro has two operating speeds; 8 MHz or 16 MHz. This device has an operating
voltage of 5 V but has a lower power alternative that runs at 3.3 V. The Pro has the same
limited memory as the Uno with only 32 KB of flash memory, 0.5 KB of which is occupied by
the boot loader.

The Pro offers the same pin configuration as the 101 with 14 digital pins, 4 of which can
be pulse with modulation, and 6 analog pins. The Pro also provides some more advanced I/O
options with a universal asynchronous receiver / transmitter (UART), serial peripheral
interface (SPI) bus, and an inter-integrated circuit (I2C) connection.

##### Operation Criteria

| Criteria                   | Specification  |
| --------                   | -------------  |
| Operating System           | None           |
| Processor Size             | 32-bit         |
| Processor Family           | ATmega         |
| Operating Voltage          | 3.3V - 5V      |
| Input Voltage              | 7-12V          |
| Clock Speed                | 8 MHz - 16 MHz |
| Digital Pins               | 14             |
| Pulse with Modulation Pins | 4              |
| Analog Input Pins          | 6              |
| DC Current per Pin         | 40 mA          |
| Flash Memory               | 32 KB          |
| System Size                | 2 KB           |
| SRAM                       | 2 KB           |
| EEPROM                     | 1 KB           |

##### Features

| Feature |           |
| ------- | -----     |
| USB     | USB-Micro |
| UART    | Yes       |
| SPI Bus | Yes       |
| I2C     | Yes       |

##### Physical Characteristics

| Dimension | Length  |
| --------- | ------  |
| Length    | 52.1 mm |
| Width     | 53.3 mm |

### Evaluation

The Pro has many advanced features but offers little in the way of rapid prototyping. The Pro is
intended for a more advanced audience than what is required for this project and is likely not
a good candidate for practical applications. However, if this system was to be replicated or
redistributed, the Pro would be useful for building a final product for an unmodifiable system.

### References

[1] "ArduinoBoardPro," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoardPro. Accessed: Oct. 6, 2016.


Arduino Micro
-------------

### Description

What is this item?

### Technical Overview

##### Operation Criteria

| Criteria                   | Specification |
| --------                   | ------------- |
| Operating System           | None          |
| Processor Size             | 8-bit         |
| Processor Family           | ATmega        |
| Operating Voltage          | 5V            |
| Input Voltage              | 7-12V         |
| Clock Speed                | 16 MHz        |
| Digital Pins               | 20            |
| Pulse with Modulation Pins | 7             |
| Analog Input Pins          | 12            |
| DC Current per Pin         | 20 mA         |
| Flash Memory               | 32 KB         |
| System Size                | 4 KB          |
| SRAM                       | 2.5 KB        |
| EEPROM                     | 1 KB          |

##### Features

| Feature |           |
| ------- | -----     |
| USB     | USB-Micro |

##### Physical Characteristics

| Dimension | Length |
| --------- | ------ |
| Length    | 48 mm  |
| Width     | 18 mm  |
| Weight    | 13 g   |

### Evaluation

How does this specific item do against our criteria?

### References

[1] "ArduinoBoardMicro," in Arduino, 2016. [Online]. Available: https://www.arduino.cc/en/Main/ArduinoBoardMicro. Accessed: Oct. 6, 2016.


Arduino Pro Mini
----------------

### Description

What is this item?

### Technical Overview

##### Operation Criteria

| Criteria                   | Specification  |
| --------                   | -------------  |
| Operating System           | None           |
| Processor Size             | 8-bit          |
| Processor Family           | ATmega         |
| Operating Voltage          | 3.3V - 5V      |
| Input Voltage              | 7-12V          |
| Clock Speed                | 8 MHz - 16 MHz |
| Digital Pins               | 20             |
| Pulse with Modulation Pins | 7              |
| Analog Input Pins          | 12             |
| DC Current per Pin         | 20 mA          |
| Flash Memory               | 32 KB          |
| System Size                | 2 KB           |
| SRAM                       | 2 KB           |
| EEPROM                     | 1 KB           |

##### Features

| Feature |           |
| ------- | -----     |
| USB     | USB-Micro |
| UART    | Yes       |
| SPI Bus | Yes       |
| I2C     | Yes       |

##### Physical Characteristics

| Dimension | Length  |
| --------- | ------  |
| Length    | 17.9 mm |
| Width     | 33 mm   |

### Evaluation

How does this specific item do against our criteria?

### References

[1] "ArduinoBoardProMini," in Arduino, 2016. [Online]. Available: https://www.arduino.cc/en/Main/ArduinoBoardProMini. Accessed: Oct. 6, 2016.


Comparison of Arduinos
-----------------------

##### Operation Criteria

| Criteria                   | Arduino Uno | Arduino 101    | Arduino Pro    | Ardunio Micro | Arduino Pro Mini |
| --------                   | ----------- | -----------    | -----------    | ------------- | ---------------- |
| Operating System           | None        | RTOS           | None           | None          | None             |
| Processor Size             | 8-bit       | 32-bit         | 32-bit         | 8-bit         | 8-bit            |
| Processor Family           | ATmega      | Intel          | ATmega         | ATmega        | ATmega           |
| Operating Voltage          | 5V          | 3.3V - 5V      | 3.3V - 5V      | 5V            | 3.3V - 5V        |
| Input Voltage              | 7-12V       | 7-12V          | 7-12V          | 7-12V         | 7-12V            |
| Clock Speed                | 16 MHz      | 8 MHz - 16 MHz | 8 MHz - 16 MHz | 16 MHz        | 8 MHz - 16 MHz   |
| Digital Pins               | 14          | 14             | 14             | 20            | 20               |
| Pulse with Modulation Pins | 6           | 4              | 4              | 7             | 7                |
| Analog Input Pins          | 6           | 6              | 6              | 12            | 12               |
| DC Current per Pin         | 20 mA       | 20 mA          | 40 mA          | 20 mA         | 20 mA            |
| Flash Memory               | 32 KB       | 196 KB         | 32 KB          | 32 KB         | 32 KB            |
| System Size                | 0.5 KB      | 2 KB           | 2 KB           | 4 KB          | 2 KB             |
| SRAM                       | 2 KB        | 2 KB           | 2 KB           | 2.5 KB        | 2 KB             |
| EEPROM                     | 1 KB        | 1 KB           | 1 KB           | 1 KB          | 1 KB             |


##### Features

| Feature       | Arduino Uno | Arduino 101 | Ardunio Pro | Arduino Micro | Ardunio Pro Mini |
| -------       | ----------- | ----------- | ----------- | ------------- | ---------------- |
| USB           | USB-Mini    | USB-Mini    | USB-Micro   | USB-Micro     | USB-Micro        |
| Accelerometer | No          | 6-Axis Gyro | No          | No            | No               |
| Bluetooth     | No          | Yes         | No          | No            | No               |
| UART          | No          | No          | Yes         | No            | Yes              |
| SPI Bus       | No          | No          | Yes         | No            | Yes              |
| I2C           | No          | No          | Yes         | No            | Yes              |

##### Physical Characteristics

| Dimension | Arduino Uno | Arduino 101 | Ardunio Pro | Arduino Micro | Ardunio Pro Mini |
| --------- | ----------- | ----------- | ----------- | ------------- | ---------------- |
| Length    | 68.6 mm     | 68.6 mm     | 52.1 mm     | 48 mm         | 17.9 mm          |
| Width     | 53.4 mm     | 53.4 mm     | 53.3 mm     | 18 mm         | 33 mm            |
| Weight    | 25 g        | 34 g        | N/A         | 13 g          | N/A              |



Raspberry Pi 3 Model B
----------------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

Raspberry Pi 2 Model B
----------------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

Raspberry Pi 1 Model A+
-----------------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

Raspberry Pi Zero
-----------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?


BeagleBone
-----------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

BeagleBone Black
-----------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

BeagleBone Green
-----------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?


-----------------------


### Summary of Evaluation


### Conclusion

What did we decide upon? Why?
