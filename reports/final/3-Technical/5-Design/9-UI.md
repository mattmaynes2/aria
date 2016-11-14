### Remote User Interface {#section-3-5-9}

The user interface must be able to provide the user with control of the Aria system. It must
provide features for observability and controllability of the system. This interface is the
sole point of communication of the user to the system so it needs to be presented in a
non-technical way that provides complete control.

In order to be accessible from any computer, the remote interface will be served as a web
application to any standard browser. The user can log into their favourite browser and
navigate to the remote application by typing in the address of their smart hub

#### Home Page {-}

When the user initially logs into the smart hub page, they will be presented with the remote
home screen. The starting page of the remote provides a general overview of the state of the
system as well as an event feed of the latest device interactions. The user can use this page
to change the system's state from standby to training or normal mode. For convenience, the user
can jump right to device discovery and being configuring a new device in the system by clicking
the "Discover" shortcut. Below is an outline of what the remote home page could look like.

![](./images/UI-Homepage.png)

#### Devices {-}

In order to go into more details about each device, the user will also have a devices page. The
devices page allows a user to control or configure a given device. The user can choose to
perform a specific action by clicking the UI toggles for the appropriate task. Interacting with
the UI in this manor to cause an event will be logged in the system in the same way as it would
if the user had manually interacted.

Each device can also be scheduled to perform specific tasks at desired times. This can be done
by pressing the schedule tab, adding an action and configuring the date and time. These
scheduled tasks will override any smart hub decisions and will be top priority. Below is
an outline of what the devices tab could look like.

![](./images/UI-Devices.png)

#### Statistics {-}

To aid in observability of the system, a statistics page will be provided. This page will allow
the user to view all of the data logs that are contained within the system as well as plot them
using various regressions through the UI. The plots created through the UI will help the user in
understanding the decisions that the system makes by displaying its data in easily consumable
graphs.
