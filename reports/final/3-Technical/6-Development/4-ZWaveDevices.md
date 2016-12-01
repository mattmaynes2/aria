## Communication with Z-Wave Devices

The system uses the Aeotec Z-Stick Series 2 from Aeon Labs to communicate with
Z-Wave devices from the system's hub. The Z-Stick is attached to a USB port in the
system hub device (Raspberry Pi).

### Controlling the Z-Stick

When connected to a USB port, the Z-Stick exposes a proprietary serial API, which
can be used by controller software to manage a network of Z-Wave devices. This document
described how this system's software uses the Z-Stick to communicate with devices in 
the home's network.

### Z-Stick API

There are several challenges to overcome in order to write Z-Wave controller software that
uses the Z-Stick.

- Proprietary API: The serial API exposed by the Z-Stick is not made public

- Low-level: The Z-Stick API is very low-level; significant effort is required in order to 
  use the most basic features of Z-Wave devices

- Complexity: Z-Wave is a complex protocol. The API provided by the Z-Stick does not provide
  a high level of abstraction from the details of the protocol

In order to avoid the difficulties of using the Z-Stick API directly, we chose to search for
a Z-Wave controller library which provides a higher level of abstraction away from the 
Z-Stick API.

### Library Alternatives

Comparison Criteria

- Does the library have a Python binding? The hub code is primarily Python, it is less effort to 
include a Python library as opposed to a C/C++ library

- Is the library mature enough to be a reliable part of the project? If many other projects use the
library already, with positive results, this indicates that the library is stable enough to include
in the project

- Is documentation and tutorial material readily accessible?

#### Sigma Designs Developer Kit (ZWare)

Sigma Designs is the primary company involved in development of the Z-Wave protocol. Sigma Designs
provides an developer kit, targeted at companies that are attempting to build custom Z-Wave devices.
The target applications for the library are listed as: door locks, lights, sensors, and thermostats.

For commercial applications, the developer kit also includes licenses which allow custom Z-Wave
devices to be sold legally.

The developer kit provides access to the following software resources:

- Documentation for the Serial API
- Z-Ware C API
- Sample applications

http://z-wavealliance.org/sigma-designs-introduces-z-wave-iot-ready-development-kits/

| ----------- | --------------- | ------------ | ------------      |
| Library     | Python Binding  | Maturity     | Availability      |
| ----------- | --------------- | ------------ | ------------      |
| Z-Ware      | No binding      | Official SDK | License Required> |
|             |                 |              |                   |
