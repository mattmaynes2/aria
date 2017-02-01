### D-6 Coffee Makers {- #D-6}

#### Using a Relay Switch {-}

A simple way to connect a coffee machine to a microcontroller is by using a voltage relay. A voltage
relay is an electrically controlled switch for high power devices. A simple coffee machine that only
needs to be plugged in in order to start brewing could be controlled using a simple voltage relay
circuit.

#### Level of Effort {-}

The same circuit which is used in the LED switch could be used to control the coffee machine, since
both the coffee machine and LED can be connected to the same voltage relay, so the level of effort
required is low.

#### Required Expertise {-}

- Safety risks: Coffee machine are normally connected directly into a wall socket. Controlling
 the coffee machine using a voltage relay would therefore involve high voltage levels which are
 unsafe to work with without proper training

In order to interface a microcontroller with more sophisticated coffee machines, some level of
reverse engineering of the coffee machine's control circuits would be necessaary. This would greatly
increase the amount of time necessary to create the device, due to the lack of electronics knowledge
on the team.

#### Evaluation {-}

Custom builds of both simple and fully-featured coffee makers may be infeasible due safety concerns
when controlling high voltage devices.

