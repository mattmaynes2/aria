### Project Status {#section-details-status}

The project planning and development has been an intertwined process that has changed the
direction of the project on a week to week basis. Every week the team selects a set of tasks
to focus on in order to achieve the next major milestone. This process has been iterative and
is allowing for incremental development of the system.

#### Current Status {-}

The next major milestone for the development of the system is the
**Oral Presentation Demonstration** in January. In order to reach this milestone a number of basic
system features need to be in place and operational. The details of these items are outlined
in the revised proposed timeline table above.

The system currently has a large portion of these items working. More specifically, the system
can currently perform the following tasks:

##### Discovery of devices {-}

The user is able to add devices to the system by connecting them to the network and following
the discovery sequence. Discovery is different for different devices and protocols. The system
is able to automatically discover WiFi devices using UPnP discovery.

##### Device displayed in user interface {-}

All devices that are registered in the system are visible from the user interface. The remote
web client provides observability for the specific devices in the system as well as their
currently reported status. Some basic metadata including name, manufacturer and protocol is
also displayed to the user.

##### Events displayed in user interface {-}

The user interface currently uses push notifications to receive events as they are logged in
the system. These events are then immediately displayed to the user in a live updating
event feed.

##### Discovery of devices from user interface {-}

The user interface provides a mechanism for launching an automated discovery probe. This
process kicks off discovery for any devices to be added to the system. If any new devices are
added to the system during this process, the user is notified and the user interface is updated.




