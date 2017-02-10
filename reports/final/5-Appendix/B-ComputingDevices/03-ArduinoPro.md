### B-3 Arduino Pro {- #B-3}

#### Description {-}

The Arduino Pro is a slim, no frills version of the Ardiuno Uno. This board requires more
technical knowledge than the Uno or the 101. All pins exposed on the Pro require soldering to
make a connection. The Pro is intended for replication of a complex circuit design with
requirements for a wide range of input and output ports.

#### Technical Overview {-}

The Pro is an embedded system that leverages the Arduino boot loader and a 32-bit ATmega328
processor. The Pro has two operating speeds; 8 MHz or 16 MHz. This device has an operating
voltage of 5 V but has a lower power alternative that runs at 3.3 V. The Pro has the same
limited memory as the Uno with only 32 kB of flash memory, 0.5 kB of which is occupied by
the boot loader [^B-3-1].

The Pro offers the same pin configuration as the 101 with 14 digital pins, 4 of which can
be pulse with modulation, and 6 analog pins. The Pro also provides some more advanced I/O
options with a universal asynchronous receiver / transmitter (UART), serial peripheral
interface (SPI) bus, and an inter-integrated circuit (I2C) connection [^B-3-1].

#### Evaluation {-}

The Pro has many advanced features but offers little in the way of rapid prototyping. The Pro is
intended for a more advanced audience than what is required for this project and is likely not
a good candidate for practical applications. However, if this system was to be replicated or
redistributed, the Pro would be useful for building a final product for an unmodifiable system.

[^B-3-1]: "ArduinoBoardPro," in Arduino, 2016. [Online]. Available: <https://www.arduino.cc/en/Main/ArduinoBoardPro>. Accessed: Oct. 6, 2016.


