### Use Cases

In order to translate the scenarios into technical requirements for the Aria system, use cases
were developed. These use cases outline the major functionality that is required by the Aria
system. Figure <!-- FIGURE NUMBER --> outlines the use cases for the entire Aria system.
Below are the descriptions of each use case for the system.

![][system-use-case]

+----------------+--------------------------------------------------------------------------------+
| Name           | **Install Hub**                                                                |
+----------------+--------------------------------------------------------------------------------+
| Description    | The user installs the learning hub in their home in order to enable automation |
|                | of their smart devices.                                                        |
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User plugs hub into outlet and turns power on                               |
|                | 2. User connects hub to a home network using Ethernet                          |
|                | 3. Hub provides confirmation that system is online                             |
+----------------+--------------------------------------------------------------------------------+


+----------------+--------------------------------------------------------------------------------+
| Name           | **Add Device**                                                                 |
+----------------+--------------------------------------------------------------------------------+
| Description    | Devices can be added to the system simply by powering them on and connecting   |
|                | to the network.                                                                |
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   | A learning hub must be installed in the user's home                            |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  | The device's state will now be used as input in learning mode. If the device   |
|                | contains an actuator, the actuator will be controlled by the learning hub in   |
|                | normal mode.                                                                   |               
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User plugs in device and turns power on                                     |
|                | 2. Device discovers network                                                    |
|                | 3. Hub discovers device and provides confirmation                              |
+----------------+--------------------------------------------------------------------------------+


+----------------+--------------------------------------------------------------------------------+
| Name           | **Enter Learning Mode**                                                        |
+----------------+--------------------------------------------------------------------------------+
| Description    | The user enters learning mode in order to indicate to the system that it       |
|                | should begin recording changes in the state of connected devices, without      |
|                | attempting to control them. Learning mode accomplishes the user's goal of      |
|                | configuring the system without manual programming.                             | 
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  | The system saves changes in the state of connected devices                     |              
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User selects enter learning mode                                            |
|                | 2. While the system is in learning mode, the system will record the user's     |
|                |    interactions with connected devices.                                        |
|                | 3. When the user selects normal mode or standby mode, the system exits         |
|                |    learning mode.                                                              |
+----------------+--------------------------------------------------------------------------------+

+----------------+--------------------------------------------------------------------------------+
| Name           | **Enter Normal Mode**                                                          |
+----------------+--------------------------------------------------------------------------------+
| Description    | The user enters normal mode in order to instruct the system to begin           |
|                | controlling connected devices.                                                 |
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  | The system maintains control over connected actuators                          |              
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User selects enter normal mode                                              |
|                | 2. System exits the currently active mode                                      |
|                | 3. System begins controlling connected actuators, using the data collected     |
|                |    during learning mode to infer the desired state of the system.              |
+----------------+--------------------------------------------------------------------------------+

+----------------+--------------------------------------------------------------------------------+
| Name           | **Enter Standby Mode**                                                         |
+----------------+--------------------------------------------------------------------------------+
| Description    | The user enters standby mode in order to instruct the system that control over |
|                | connected devices should be halted, and changes in the state of devices should |
|                | not be accepted as learning data. Standby mode allows a user to control their  |
|                | devices under exceptional circumstances without learning the system to perform |
|                | an incorrect task.                                                             |
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  | System does not accept learning data, System does not modify the state of      |
|                | devices                                                                        |               
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User enters standby mode                                                    |
|                | 2. System exits the active mode                                                |
+----------------+--------------------------------------------------------------------------------+

+----------------+--------------------------------------------------------------------------------+
| Name           | **Remove Device**                                                              |
+----------------+--------------------------------------------------------------------------------+
| Description    | Devices will stop recording when removed from the smart learning network. To   |
|                | remove the history of the device, the user can delete it using the remote      |
|                | interface.                                                                     |
+----------------+--------------------------------------------------------------------------------+
| Dependencies   | **INCLUDE** Reset Device                                                       |
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  | System does not accept learning data, System does not modify the state of      |
|                | devices                                                                        |               
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User disconnects device from the network                                    |  
|                | 2. If the user wishes to remove the device permanently, **INCLUDE** use case   |
|                |    Reset Device                                                                |
+----------------+--------------------------------------------------------------------------------+

+----------------+--------------------------------------------------------------------------------+
| Name           | **Reset Device**                                                               |
+----------------+--------------------------------------------------------------------------------+
| Description    | States of the selected devices from before the reset are no longer used to     |
|                | infer states in normal mode.                                                   |
+----------------+--------------------------------------------------------------------------------+
| Dependencies   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Primary Actor  | Homeowner                                                                      |
+----------------+--------------------------------------------------------------------------------+
| Precondition   |                                                                                |
+----------------+--------------------------------------------------------------------------------+
| Postcondition  | System does not accept learning data, System does not modify the state of      |
|                | devices                                                                        |               
+----------------+--------------------------------------------------------------------------------+
| Flow 			 | 1. User logs in to remote interface                                            | 
|                | 2. User selects a device                                                       |
|                | 3. User selects reset device                                                   |
|                | 4. System erases the saved historical states of the device                     |
+----------------+--------------------------------------------------------------------------------+


#### Training Use Cases



![][training-use-case]

##### View Behaviours {-}

1. User naviagtes to the training view
1. User is presented with a list of existing behaviours

##### Add Behaviour {-}

**PRECONDITION**: User is on the training view
1. User selects "Add behaviour"
1. User specifies a name for the new behaviour
1. User saves behaviour
**POSTCONDITION**: User is on the details view for the new behaviour

##### Edit Behaviour {-}

**PRECONDITION**: User is on the training view
1. User selects a behaviour from the list of behaviours.
1. Behaviour details view is opened.
1. User can change the name of the behaviour.
1. User is presented with a list of training sessions associated with the behaviour.

##### Add Training Session {-}

**PRECONDITION**: User is on the behaviour details view

1. User clicks on the add new training session button
1. User specifies a name for their session
1. User saves session

**POSTCONDITION**: User is on the details view for the new session

##### Edit Training Session {-}

1. User clicks the details view for a training sesion
2. User clicks a view event details button
3. System displays system events associated with that training session


##### Start Training Session {-}

**PRECONDITION**: User is on the details view for a session

1. User clicks start session button
1. View indicates that the training session is active

**POSTCONDITION**: The active training session is indicated on the hub main view

**POSTCONDITION**: The system starts recording events and associating them with the training session

**POSTCONDITION**: Hub is in training mode

##### Stop Training Session {-}

**PRECONDITION**: User is on the details view for a session

1. User clicks stop session button
1. View indicates that the training session is no longer active

**POSTCONDITION**: The training session is not longer marked as active on the hub main view

**POSTCONDITION**: The system no longer associated new events with the session

**POSTCONDITION**: Hub is in normal mode
