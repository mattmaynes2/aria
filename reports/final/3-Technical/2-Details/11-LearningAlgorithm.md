### Learning Algorithm {#sec-3-2-11-2}

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
