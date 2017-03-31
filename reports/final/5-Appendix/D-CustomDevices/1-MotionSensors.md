### D-1 Motion Sensor {- #D-1}

#### Technical Overview {-}

This section considers devices that can be used to alert the system when a person enters or leaves
an area of the home.

#### Sensor Technologies {-}

This section provides a comparison of several different sensor technologies that are commonly used
in motion detection.

##### Passive Infrared (PIR) {-}

A passive infrared sensor detects motion using the infrared radiation (heat) from a warm body. A
sensor contains two slots, each of which contains a material which is sensitive to infrared
radiation. As a warm body passes in front of the sensor, a different amount of radiation is received
at each slot. This difference in radiation causes a signal in the output of the device[^D-1-1].

Use of the PIR modules encountered during this research does not require expert knowledge of circuit
design; the complexity of the circuits involved in connecting the modules to a microcontroller is
comparable to that of a simple LED circuit. A power source and a resistor is sufficient to get the
module up and running.

Most PIR modules have 3 pins to connect to a circuit. One pin connects to ground, another to power,
andthe third pin is used for output. The output consists of a single digital signal indicating when
motion is detected.

Tutorials describing how to connect PIR modules to common microcontrollers, such as a Raspberry Pi
or Arduino are widely available online.

The complexity of the circuit required to interface with a PIR module is comparable to the light
switch circuit, consisting of a single push button used to toggle an LED. Therefore, development
time required for the complete device is expected to be under 10 hours.

PIR sensor modules are reliable because they do not typically contain any moving components, other
than potentiometer used for sensitivity adjustment.

PIR sensors are easy to use, the main difficulties that a user may encounter in setting up a PIR
sensor are ensuring that the detectorès field of view covers the correct area, as well as
potentially adjusting the sensitivity of the detector.

PIR sensors are available with a range which is suitable for a typical room (approximately 7m
range)[^D-1-2].

The following tutorials explain how to interface with PIR modules:

<https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf>
<https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/>


##### Doppler-Effect based sensors {-}

Several types of motion detectors use the Doppler effect to detect motion. The detector transmits a
signal of a known frequency. This signal is reflected by any objects in its path and detected when
it returns to the sensor. The sensor tracks the frequency of the reflected wave; when a wave is
reflected off of a moving object the frequency of the reflected wave differs from that of the
incident wave due to the Doppler effect. This change in frequency is detected by the sensor and
registered as motion [^D-1-3].

##### Infrared Break-Beam {-}

An infrared break-beam sensor consists of two physical modules separated by some distance.  One side
of the detector transmits a beam of infrared light which is detected by the other side.

#### Expertise Required {-}

- Little expertise required, circuits are simple
- Tutorials widely available online

#### Component Availability {-}

- Components widely available

#### Reliability {-}

- Sensors generally have a lower range than PIR sensors, availability of detectors with a longer
    range may be lower

- Allows for finer control over the area of detection than a PIR sensor

#### Usability {-}

- More difficult setup than a PIR sensor, requires the user to precisely aim the transmitted beam.

#### Feature Comparison {-}

| Feature    | Custom | D-Link Wifi Motion Sensor | Samsung SmarttThings Motion Sensor  | Belkin |
| -------    | ------ | ------------------------- | ----------------------------------- | ------ |
| Range      | 7m     | 8m                        | 15m - 40m                           | 3m     |
| Interfaces | _      | WiFi                      | ZigBee                              | WiFi   |
| Type       | PIR    | PIR                       | PIR                                 | PIR
|

Note: The custom device can potentially support multiple different communication interfaces

#### Evaluation {-}

| Criterion          | Score |
| ---------          | ----- |
| Expertise Required | Low   |
| Level of Effort    | Low   |
| Quality Comparison | Equal |

[^D-1-1]: “PIR Motion Sensor,” How PIRs Work | PIR Motion Sensor | Adafruit Learning System. [Online]. Available: <https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work>. Accessed: Oct. 29, 2016.

[^D-1-2]: Adafruit Industries, "PIR (motion) sensor ID: 189 - $9.95: Adafruit industries, unique & fun DIY electronics and kits,". [Online]. Available: <https://www.adafruit.com/product/189>. Accessed: Oct. 29, 2016.

[^D-1-3]: "IR beam motion detector", Hkvstar.com, 2017. [Online]. Available: <http://www.hkvstar.com/category/ir-motion-detector.html>. [Accessed: 24-Mar-2017].