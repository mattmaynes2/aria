# 5. Computing Devices

5.1 Background
--------------

A computing devices is any electronic device that can be used to process data and send it over
a smart home network. Computing devices include computers, micro-controllers and other
embedded devices. Computing devices that are being examined all offer control of external
hardware interfaces. This report examines computing devices that can be used for prototyping
embedded control of sensors and actuators.

5.2 Relation to System
----------------------

Computing devices will be used for many aspects of the smart home system. A computing device will
be used for the central smart hub as well as for various other devices in the system. Different
devices will be more suitable to some tasks than others. This report compares a number of these
computing options with a focus on the areas of need within the system.

5.3 Arduino Uno
---------------

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
weight of approximately 25 g. The Uno also includes an integrated USB-Mini port used for serial
communication and as a power source. The board includes a 5 V DC power input for running the
board continually.

### Evaluation

The Arduino Uno offers fast and simple prototyping options for quickly building embedded circuits.
This board is very useful for rapidly testing but would not be practical in a mass production
system. For the smart learning system, this board would be optimal for experimentation and
quick deployment.

### References

[1] "ArduinoBoardUno," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoardUno. Accessed: Oct. 6, 2016.

5.4 Arduino 101
----------------

### Description

The Arduino 101 is a more sophisticated board that uses the Intel Curie processor for computing.
This board leverages the Real-Time Operating System (RTOS) developed by Intel for running the
board.

### Technical Overview

The Arduino 101 is the most feature rich board that Arduino is offers. It comes with a full
Real-Time Operating System (RTOS) that is powered by the Intel Curie. The processor is a 32-bit,
8 MHz or 16 MHz backed by 196 KB of flash memory. The RTOS is a light weight OS that only
occupies 2 KB of memory to provide managed, concurrent applications.

The 101 comes with a number of additional features above other microcontrollers in the Arduino
family. Beyond the standard USB-Mini serial connection, the 101 offers a 6 axis gyroscope
accelerometer and integrated Bluetooth. The 101 also provides a 5 V DC power input for
deployment use.

The 101 offers many of the same prototyping capabilities as the Uno with 14 digital pins, 4
of which provide pulse with modulation. The 101 also exposes 6 analog to digital pins.

### Evaluation

The 101 is a much more feature rich board than the Uno, however the added features are not
applicable to this project. The 101 also has a much higher price point per unit than the Uno
with no real added value. This makes the Uno a more appealing candidate for rapid prototyping
and simple circuit design.

### References

[1] "ArduinoBoard101," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoard101. Accessed: Oct. 6, 2016.


5.5 Arduino Pro
----------------

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

### Evaluation

The Pro has many advanced features but offers little in the way of rapid prototyping. The Pro is
intended for a more advanced audience than what is required for this project and is likely not
a good candidate for practical applications. However, if this system was to be replicated or
redistributed, the Pro would be useful for building a final product for an unmodifiable system.

### References

[1] "ArduinoBoardPro," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoardPro. Accessed: Oct. 6, 2016.


5.6 Arduino Micro
-----------------

### Description

The Arduino Micro is the smallest microcontroller of the Arduino family. The Micro also
provides the most external ports of any Arduino making it suitable for large circuits.

### Technical Overview

The Micro provides high performance embedded computing with a 8-bit, 16 MHz ATmega32U4 processor.
The Micro also comes standard with the Arduino bootloader and a standard 32 KB of flash memory.
The Micro has a operating voltage of 5 V and comes with a standard DC power input.

The Micro has 20 exposed digital pins, 7 of which can be pulse with modulation. These extra
pins make the Micro very suitable for large complex circuits that require many inputs or
outputs. The Micro also has 12 analog to digital pins. The Micro does lack in special features.
It only offers serial communication over a standard USB-Micro port. There are other special
features with this device.

Appropriately, the Micro is the smallest and lightest microcontroller in the  Arduino family.
It is only 48 mm long and 18 mm wide. The Micro also only has a weight of roughly 13 g.

### Evaluation

This Arduino would be perfectly suited to a mass production environment where size and weight
were valuable resources. If the learning home automation system was to be commercially
produced, this could be a very valuable microcontroller. This microcontroller could be used
for this system, but would take more effort for prototyping and would likely not be a suitable
fit.

### References

[1] "ArduinoBoardMicro," in Arduino, 2016. [Online]. Available:
https://www.arduino.cc/en/Main/ArduinoBoardMicro. Accessed: Oct. 6, 2016.


5.7 Comparison of Arduinos
--------------------------

##### Operation Criteria

| Criteria                   | Arduino Uno | Arduino 101    | Arduino Pro    | Arduino Micro |
| --------                   | ----------- | -----------    | -----------    | ------------- |
| Operating System           | None        | RTOS           | None           | None          |
| Processor Size             | 8-bit       | 32-bit         | 32-bit         | 8-bit         |
| Processor Family           | ATmega      | Intel          | ATmega         | ATmega        |
| Operating Voltage          | 5V          | 3.3V - 5V      | 3.3V - 5V      | 5V            |
| Input Voltage              | 7-12V       | 7-12V          | 7-12V          | 7-12V         |
| Clock Speed                | 16 MHz      | 8 MHz - 16 MHz | 8 MHz - 16 MHz | 16 MHz        |
| Digital Pins               | 14          | 14             | 14             | 20            |
| Pulse with Modulation Pins | 6           | 4              | 4              | 7             |
| Analog Input Pins          | 6           | 6              | 6              | 12            |
| DC Current per Pin         | 20 mA       | 20 mA          | 40 mA          | 20 mA         |
| Flash Memory               | 32 KB       | 196 KB         | 32 KB          | 32 KB         |
| System Size                | 0.5 KB      | 2 KB           | 2 KB           | 4 KB          |

##### Features

| Feature       | Arduino Uno | Arduino 101 | Arduino Pro | Arduino Micro |
| -------       | ----------- | ----------- | ----------- | ------------- |
| USB           | USB-Mini    | USB-Mini    | USB-Micro   | USB-Micro     |
| Accelerometer | No          | 6-Axis Gyro | No          | No            |
| Bluetooth     | No          | Yes         | No          | No            |
| UART          | No          | No          | Yes         | No            |
| SPI Bus       | No          | No          | Yes         | No            |
| I2C           | No          | No          | Yes         | No            |

##### Physical Characteristics

| Dimension | Arduino Uno | Arduino 101 | Arduino Pro | Arduino Micro |
| --------- | ----------- | ----------- | ----------- | ------------- |
| Length    | 68.6 mm     | 68.6 mm     | 52.1 mm     | 48 mm         |
| Width     | 53.4 mm     | 53.4 mm     | 53.3 mm     | 18 mm         |
| Weight    | 25 g        | 34 g        | N/A         | 13 g          |

----------

5.8 Raspberry Pi Zero
---------------------

### Description

The Raspberry Pi Zero is a minimal computer board that offers a full computing platform in a
compact form for embedded computing. The Zero is the smallest board in the Raspberry Pi family
and is ideal for medium to heavy computation with minimal footprint. The Raspberry Pi Zero is one
of the only Raspberry Pi boards that competes for a real embedded computing experience.

### Technical Overview

The Raspberry Pi Zero has the smallest surface area of any of the Pi's, measuring in at only
65mm long by 30mm wide. To make the board as small as possible, many of the standard Raspberry Pi
features were removed. This means that the Zero has no on-board WiFi, Bluetooth or even Ethernet.
Despite these losses, the board is still equip with a 32-bit 1GHz Broadcom BCM283 processor backed
by 512MB of flash storage.

The Zero provides a lot of room for flexibility with 40 available GPIO pins. The combination of
the Zero's computing power and general IO makes it ideal for small spaces that need a lot of
power.

### Evaluation

The Zero could be useful for programming devices in the system; however, while the Zero does offer
a smaller physical footprint and more GPIO than the Arduino Uno, it does require more power to
maintain operation. This extra power consumption does come with more performance which may be
useful but likely unnecessary for the smart learning system.

### Reference

[1] "Raspberry pi Zero," Raspberry Pi. [Online]. Available:
https://www.raspberrypi.org/products/pi-zero/. Accessed: Oct. 10, 2016.

[2] "Raspberry Pi Zero,". [Online]. Available:
https://shop.pimoroni.com/products/raspberry-pi-zero. Accessed: Oct. 10, 2016.

5.9 Raspberry Pi 1 Model A+
---------------------------

### Description

The Raspberry Pi 1 Model A+ is the original Raspberry Pi with some performance improvements.
This device is a computing board that provides desktop equivalent computing power in only a few
square inches of space. The Pi 1 is the first candidate being considered for the role of the
smart home learning hub.

### Technical Overview

The Pi 1 is the base Raspberry Pi that is powered by a 32-bit 700MHz Arm processor and 256MB of
DDR2 RAM. The Pi 1 comes with a standard HDMI output for visual output. The board also comes with
a standard Ethernet port, and a single USB port for serial communication. The Pi 1 does also offer
40 GPIO pins for more embedded purposes.

### Evaluation

The Raspberry Pi 1 is a good candidate for the central hub as it uses low power and provides
adequate computing performance.

### References

[1] "Raspberry pi 1 model A+," Raspberry Pi. [Online]. Available:
https://www.raspberrypi.org/products/model-a-plus/. Accessed: Oct. 10, 2016.

[2] J. Adams, "Raspberry Pi Model B+," Mar. 07, 2014. [Online]. Available:
https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/Raspberry-Pi-B-Plus-V1.2-Mechanical-Drawing.pdf.
Accessed: Oct. 10, 2016.

5.10 Raspberry Pi 2 Model B
---------------------------

### Description

The Raspberry Pi 2 Model B is the second generation of Raspberry Pi designs. The Pi 2 uses the same
design as the Pi 1 with all the same features and more performance.

### Technical Overview

The Pi 2 is very similar to the Pi 1 but provides a slight faster 32-bit 900MHz Arm processor. The
Pi 2 has significantly more RAM than the Pi 1 with 1GB of DDR2. The Pi 2 comes with a standard
HDMI video output for monitoring it from a screen. It also is equip with an Ethernet port and 4
USB ports. The Pi 2 also provides the same 40 GPIO pin configuration as the Pi 1

### Evaluation

The Pi 2 out performs the Pi 1 in all areas and is likely a better candidate for the smart hub. It
uses the same amount of power but provides far more computing performance.

### References

[1] "Raspberry pi 2 model B," Raspberry Pi. [Online]. Available:
https://www.raspberrypi.org/products/raspberry-pi-2-model-b/. Accessed: Oct. 10, 2016.

5.11 Raspberry Pi 3 Model B
---------------------------

### Description

The Raspberry Pi 3 Model B is the most advanced Raspberry Pi available. The Pi 3 is a
computer board that uses a very similar design to the other Pi Models. The Pi 3 offers more
computing performance than all of its predecessors and is a very suitable candidate for the
smart hub.

### Technical Overview

The Raspberry Pi 3 offers massive embedded performance with a 1.2GHz 64-bit Quad-core Arm
processor. Similar to the Pi 2, the Pi 3 also comes with 1GB of RAM. As with all other Pi models,
the Pi 3 provides a 40 GPIO pin configuration for external devices.

The Pi 3 also comes with a number of standard options that set it apart from all other Pi models.
It comes with integrated WiFi, Ethernet and Bluetooth communication interfaces. It has 4 standard
USB ports and an HDMI output for visual feedback.

### Evaluation

The Raspberry Pi 3 is the most advanced Raspberry Pi board available. Its extra computing power
would be a good asset for heavy computation making this an ideal candidate for the central smart
hub. The Pi 3 comes with many standard features including WiFi and Bluetooth communication which
will make external interfacing simple with minimal investment.

### References

[1] "Raspberry pi 3 model B," Raspberry Pi. [Online]. Available:
https://www.raspberrypi.org/products/raspberry-pi-3-model-b/. Accessed: Oct. 10, 2016.

[2] "Power supply - raspberry pi documentation,". [Online]. Available:
https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md.
Accessed: Oct. 10, 2016.

[3] "GPIO - raspberry pi documentation,". [Online]. Available:
https://www.raspberrypi.org/documentation/hardware/raspberrypi/gpio/README.md.
Accessed: Oct. 10, 2016.

[4] "Raspbian - raspberry pi documentation,". [Online]. Available:
https://www.raspberrypi.org/documentation/raspbian/. Accessed: Oct. 10, 2016.

[5]	J. Adams, "Raspberry Pi 3 Model B," Jun. 10, 2015. [Online]. Available:
https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/RPI-3B-V1_2.pdf.
Accessed: Oct. 10, 2016.

5.12 Comparison of Raspberry Pi
-------------------------------

##### Operation Criteria

| Criteria                   | Raspberry Pi Zero | Raspberry Pi 1 | Raspberry Pi 2 | Raspberry Pi 3 |
| --------                   | ----------------- | -------------- | -------------- | -------------- |
| Operating System           | Raspbian          | Raspbian       | Raspbian       | Raspbian       |
| Processor Size             | 32-bit            | 32-bit         | 32-bit         | 64-bit         |
| Processor Family           | Broadcom          | Arm            | Arm            | Arm            |
| Operating Voltage          | 5V                | 5V             | 5V             | 5V             |
| Input Voltage              | 3.3V              | 3.3V           | 3.3V           | 3.3V           |
| Clock Speed                | 1 GHz             | 700 MHz        | 900 MHz        | 1.2 GHz        |
| Digital Pins               | 40                | 40             | 40             | 40             |
| Pulse with Modulation Pins | N/A               | N/A            | N/A            | N/A            |
| Analog Input Pins          | N/A               | N/A            | N/A            | N/A            |
| DC Current per Pin         | 50 mA             | 50 mA          | 50 mA          | 50 mA          |
| Flash Memory               | 512 MB            | 256 MB         | 1 GB           | 1 GB           |
| System Size                | 1.6 GB            | 1.6 GB         | 1.6 GB         | 1.6 GB         |

##### Features

| Feature           | Raspberry Pi Zero | Raspberry Pi 1 | Raspberry Pi 2 | Raspberry Pi 3 |
| -------           | ----------------- | -------------- | -------------- | -------------- |
| USB               | USB-Micro         | 1              | 4              | 4              |
| HDMI              | Mini-HDMI         | Yes            | Yes            | Yes            |
| Bluetooth         | No                | No             | No             | Yes            |
| WiFI              | No                | No             | No             | Yes            |
| Audio             | No                | 3.5 mm Jack    | 3.5 mm Jack    | 3.5 mm Jack    |
| Ethernet          | No                | Yes            | Yes            | Yes            |
| Camera Interface  | No                | Yes            | Yes            | Yes            |
| Display Interface | No                | Yes            | Yes            | Yes            |
| Micro SD          | Yes               | Yes            | Yes            | Yes            |


##### Physical Characteristics

| Dimension | Raspberry Pi Zero | Raspberry Pi 1 | Raspberry Pi 2 | Raspberry Pi 3 |
| --------- | ----------------- | -------------- | -------------- | -------------- |
| Length    | 65 mm             | 85 mm          | 85 mm          | 85 mm          |
| Width     | 30 mm             | 56 mm          | 56 mm          | 56 mm          |


----------

5.13 BeagleBone
---------------

### Description

The BeagleBone is another computing board that is on the edge of embedded computing. The BeagleBone
is a small, feature rich, Linux system for concurrent, real-time embedded programming. This board
could be used for the learning hub or even a small device that requires more computation power than
a microcontroller can offer.

### Technical Overview

The standard BeagleBone is very comparable to the Raspberry Pi 2 in features and performance. It
is driven by a 32-bit 700MHz Arm processor with 256MB of flash memory. This computing board offers
2 USB ports and a standard Ethernet port for external communication.

The BeagleBone stands out from the Raspberry Pi with its general pin configurations, as it offers
60 GPIO pins. This makes the BeagleBone more suitable for embedded computing than the Raspberry
Pi models.

### Evaluation

How does this specific item do against our criteria?

### References

[1] "Bone-original,". [Online]. Available: http://beagleboard.org/bone-original.
Accessed: Oct. 10, 2016.

[1] "BeagleBone Schematic," Jun. 28, 2012. [Online]. Available:
https://github.com/CircuitCo/BeagleBone-RevA6/blob/master/BEAGLEBONE_REV_A6A.pdf?raw=true.
Accessed: Oct. 10, 2016.

5.14 BeagleBone Black
---------------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

### References

[1] "BeagleBone Black,". [Online]. Available: http://beagleboard.org/black.
Accessed: Oct. 10, 2016.

[2] "Beagleboard: BeagleBoneBlack,". [Online].
Available: http://elinux.org/Beagleboard:BeagleBoneBlack. Accessed: Oct. 10, 2016.

5.15 BeagleBone Green
---------------------

### Description

What is this item?

### Technical Overview

Technically speaking, what does this item do?

### Evaluation

How does this specific item do against our criteria?

### References

[1]	"BeagleBone Green,". [Online]. Available: http://beagleboard.org/green.
Accessed: Oct. 10, 2016.

5.16 Comparison of BeagleBone
-----------------------------

##### Operation Criteria

| Criteria                   | BeagleBone | BeagleBone Black | BeagleBone Green |
| --------                   | ---------- | ---------------- | ---------------- |
| Operating System           | Angstrom   | Debian           | Debian           |
| Processor Size             | 32-bit     | 32-bit           | 32-bit           |
| Processor Family           | ARM        | ARM              | ARM              |
| Operating Voltage          | 5V         | 5V               | 5V               |
| Input Voltage              | 1.8V       | 1.8V             | 1.8V             |
| Clock Speed                | 700MHz     | 1GHz             | 1GHz             |
| Digital Pins               | 60         | 69               | 65               |
| Pulse with Modulation Pins | 4          | 4                | 8                |
| Analog Input Pins          | 4          | 4                | 7                |
| Flash Memory               | 256MB      | 512MB            | 512 MB           |
| System Size                | 1.8 GB     | 2.2GB            | 2.2 GB           |

##### Features

| Feature   | BeagleBone | BeagleBone Black | BeagleBone Green |
| -------   | ---------- | ---------------- | ---------------- |
| USB       | 2          | 2                | 2                |
| HDMI      | No         | Yes              | No               |
| Bluetooth | No         | Yes              | Yes              |
| WiFI      | No         | Yes              | Yes              |
| Ethernet  | Yes        | Yes              | Yes              |
| UART      | No         | Yes              | Yes              |
| I2C       | No         | No               | Yes              |
| Micro SD  | Yes        | Yes              | Yes              |


##### Physical Characteristics

| Dimension | BeagleBone | BeagleBone Black | BeagleBone Green |
| --------- | ---------- | ---------------- | ---------------- |
| Length    | 86 mm      | 86 mm            | 86 mm            |
| Width     | 54 mm      | 54 mm            | 54 mm            |


-----------------------


5.17 Summary of Evaluation
--------------------------

### Embedded Devices

There will be a number of applications for embedded devices in the smart home system. There may be
various computing devices that are suitable for different tasks depending on the requirements.
However, for the general needs of the embedded computing in this system, the Arduino Uno will
likely be the most suitable candidate.

The Uno provides a rapid prototyping environment with support for a wide array of custom devices.
It has sufficient computing power with minimal power consumption for the requirements of the general
devices that have been identified in the system scenarios.

As an added benefit, the Arduino community offers many high quality tutorial, examples and
documentation of system usage. The extensive support offered by the community is a major advantage
over the other systems and will be a major asset for developing on this device.

### Learning Hub

The learning hub will require a significant amount of computational performance to make decisions
about home environment. For this component, full computer boards were considered as they provide
more performance than the available microcontrollers. After a close examination of a number of
computing devices it was determined that the Raspberry Pi 3 Model B is the most suitable
option for this roll in the system.

Since this device is heavily reliant on performance, the decision was reduced to 2 candidates,
the Raspberry Pi 3 and the BeagleBone Black. They both offer considerable performance but the Pi 3
offers more processing cores with a higher clock speed, larger registers and more RAM. This
makes the decision simple, the Pi 3 is the better candidate.


