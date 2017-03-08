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
algorithm allowed early experimentation with sensor and device configurations. Building iteratively upon a simple a
lgorithm rather than attempting to use a complex machine learning algorithm or library immediately allows early 
identification of the challenges that are involved in machine learning. Iterative development also ensures that 
a basic working algorithm is available if unforeseen difficulties are found in implementing a more complex solution.

#### Strategy Version 1 {-}

The first strategy implemented considers the list of device and sensor events for a single training
session. The simple algorithm proceeds as follows:

1. Find the last user action taken during the training session
2. Find the first event preceding that action
3. Whenever the event found in (2) is detected, perform the user action

Whenever the user completes a training session, the strategy is rebuilt based on the session.

Implementing this simple strategy allowed for development of several building blocks for the 
machine learning component:

- An entity that observes incoming events and feeds them to the learning strategy.
- An entity that retrieves events from a training session and builds a strategy using the events

The machine learning component makes use of a Strategy design pattern, which allows different 
implementations of the learning strategy to be interchanged easily.

#### Strategy Version 2 {-}

The second strategy implemented improved on the previous strategy by looking for all user 
requests in the training session and associating each one with the event that had happened 
right before the request was made. The algorithm would then check if an incoming event had any 
requests associated with it. If it found a request it would trigger that action. 


#### Strategy Version 3 {-}

The third and current strategy looks at the events for a session as well as tracks the state of 
the system since the training session started and associates a user action with the last event 
that caused a change in the system.
