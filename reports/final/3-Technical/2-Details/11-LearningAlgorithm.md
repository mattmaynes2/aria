### Learning Algorithm {#sec-3-2-11-2}

#### Introduction {-}

One of the principal goals of the project is allow users to train the system to control their devices without 
creating explicit rules. The Aria system observes the user's interactions with devices and sensors during 
*training sessions*. A training session is a short period of time in which the user performs a series of 
actions that they would like the system to replicate in the future. Actions may include triggering sensors,
or controlling the state of an actuator. Each training session is associated with a particular *behaviour* that
the user is attempting to teach the system. 

From the viewpoint of the Aria system, all user actions and sensor reports during a training session are 
processed as events; these events are either labelled as user actions or sensor reports. The task of the system
is to infer associations between the reported values from sensors and the actions that a user took in response.
This process of inferring the relationship between the state of sensors and user actions is referred to as
*supervised learning* 

An iterative approach was used for development of the supervised learning component. Starting with a very simple
algorithm allowed early experimentation of sensor and device configuration, as well as analysis of device data
in the context of machine learning. Building iteratively upon a simple algorithm rather than attempting to use a 
complex machine learning algorithm or library immediately allows early identification of the challenges that are 
involved in machine learning. Iterative development also ensures that a basic working algorithm is available 
if unforeseen difficulties are found in implementing a more complex solution.

#### Strategy Version 1 {-}

The first strategy implemented was a simple algorithm that looked at the events for a training 
session, find the last user request and use this as its action on every incoming event to the 
system. 

#### Strategy Version 2 {-}

The second strategy implemented improved on the previous strategy by looking for all user 
requests in the training session and associating each one with the event that had happened 
right before the request was made. The algorithm would then check if an incoming event had any 
requests associated with it. If it found a request it would trigger that action. 


#### Strategy Version 3 {-}

The third and current strategy looks at the events for a session as well as tracks the state of 
the system since the training session started and associates a user action with the last event 
that caused a change in the system.
