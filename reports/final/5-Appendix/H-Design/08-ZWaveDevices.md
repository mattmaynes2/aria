### H-8 Communication with Z-Wave Devices {- #H-8}

The system uses the Aeotec Z-Stick Series 2 from Aeon Labs to communicate with
Z-Wave devices from the system's hub. The Z-Stick is attached to a USB port in the
system hub device (Raspberry Pi).

#### Controlling the Z-Stick {-}

When connected to a USB port, the Z-Stick exposes a proprietary serial API, which
can be used by controller software to manage a network of Z-Wave devices. This document
describes how the hub software uses the Z-Stick to communicate with devices in 
the home's network.

#### Z-Stick API {-}

There are several challenges to overcome in order to write Z-Wave controller software that
uses the Z-Stick.

- Proprietary API: The serial API exposed by the Z-Stick is not made public
- Low-level: The Z-Stick API is very low-level; significant effort is required in order to 
    use the most basic features of Z-Wave devices

In order to avoid the difficulties of using the Z-Stick API directly, we chose to search for
a Z-Wave controller library which provides a higher level of abstraction away from the 
Z-Stick API.

#### Library Alternatives {-}

Comparison Criteria

- Does the library have a Python binding? The hub code is primarily written in Python, it is less 
    effort to include a Python library as opposed to a C/C++ library
- Is the library mature enough to be a reliable part of the project? If many other projects use the
    library already, with positive results, this indicates that the library is stable enough to include
    in the project
- Is documentation and tutorial material readily accessible?

##### Sigma Designs Developer Kit (ZWare) {-}

Sigma Designs is the primary company involved in development of the Z-Wave protocol. Sigma Designs
provides an developer kit, targeted at companies that are attempting to build custom Z-Wave devices.
The targeted applications for the library are listed as: door locks, lights, sensors, and 
thermostats.

For commercial applications, the developer kit also includes licenses which allow custom Z-Wave
devices to be sold legally [66].

The developer kit provides access to the following software resources:

- Documentation for the Serial API
- Z-Ware C API
- Sample applications

##### OpenZWave {-}

OpenZWave is a free open-source library for communicating with Z-Wave devices using compatible
ZWave controller devices. The Aeotec Z-Stick is fully compatible with OpenZWave. OpenZWave is a 
C++ library; the developers have created bindings for several other languages including Python.

The OpenZWave source code is well-documented, and includes several examples of usage. OpenZWave is
used by several existing home automation products to communicate with devices, with 259 forks on
Github and an active community of developers [67]. Additionally, OpenZWave is a member of the Z-Wave 
Alliance, the consortium of companies that certifies Z-Wave devices [68]. 

#### Comparison {-}

| Library       | Python Binding  | Maturity     | Availability      |
| ------------- | --------------- | ------------ | ------------      |
| Sigma Designs | No binding      | Official SDK | License Required  |
| OpenZWave     | Has a binding   | Mature       | Open Source       |

We decided to include the OpenZWave library in the project. The availability of a Python binding
for the library makes including it in the project simpler than the Sigma Designs C API. The Sigma 
Designs Developer Kit is also targeted at companies that are attempting to create their own 
certified Z-Wave devices, which is outside the scope of this project. Tutorials and examples of 
using the OpenZWave library are also more accessible online, from a variety of sources.

