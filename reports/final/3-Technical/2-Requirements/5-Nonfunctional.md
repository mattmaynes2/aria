### Other Nonfunctional Requirements

#### Performance Requirements {-}

##### Device Communication Range {-}

Devices must be able to communicate wirelessly using the network. The range of communication must be
sufficiently large that devices can be placed anywhere in an average home. The smart home devices
will need to be capable of receiving and transmitting data using this network with enough range.

The distance between nodes in our system must be no more than 50 meters. The will allow for any
protocol to communicate with the necessary nodes.

##### System Responsiveness {-}

The system must readily adapt to environmental changes to be effective. When in training mode, the
system does not make any decisions and therefore has no responsiveness requirement. However, when
the system enters playback mode it must make decisions as fast as environmental changes are
received. This will ensure that the system is as responsive as possible when a user performs an
action.

#### Security Requirements {-}

##### Device Connection Security {-}

All commands to devices must be authenticated to ensure that they are from an authorized source.
This is in order to eliminate the possibility of malicious entities taking control of a home's
devices.

##### Remote Interface Security {-}

Digital access to the hub's configuration interface must be secured using TLS 1.2 (RFC 5246) and
HTTP basic authentication as described in RFC 2617. Use of these Internet Official Protocol
Standards ensures that the system uses widely accepted authentication practices.

#### Quality Requirements {-}

##### Learning Hub Reliability {-}

The learning hub is the center of communications and is responsible for interfacing with the system
user. It must record data on some form of internal storage to log actions that have occurred as
well as decisions that is has made. It is critical that the learning hub not lose its data as this
would set the system back to its initial, untrained state. Precautions should be taken so that in
the case of a system failure or power failure, the critical system data is preserved. Hub
operations should be atomic and reversible should they fail.

The learning hub must also be online and available to record system events. If the learning hub is
to go into a state faulty state then it should indicate this to the user. The system must provide
a mechanism for resetting itself if errors are occurring.

##### Device Reliability {-}

Devices in the system do not need to meet as high of a standard as the learning hub for
reliability. However, devices should have some indicator when faults occur. Devices may be hard
to access so any device that can be restarted should provide functionality for doing so from the
remote interface. If this is not possible then as a minimum, the remote interface should
indicate whether or not a device has encountered a fault or if it is no longer responding.
Restarting a device in the network should then reconnect to the system and retain all of its
history within the learning hub.




