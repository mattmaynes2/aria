### Design Patterns {#sec-3-2-7-1}

#### Communication Adapters {-}

The exchange server has the requirement of communicating to several different devices on
potentially different protocols. In order to communicate with all of these different
protocols, the exchange uses the *Adapter Pattern* to translate between the external protocol
and a single, uniform internal protocol. This pattern is best illustrated with the diagram
below.

![][design-adapter]

#### Learning Strategies {-}

To be able to test different learning algorithms, the strategy pattern was used. This allows
different learning algorithms to be supplied for modeling the user's environment and making
decisions. The diagram below illustrates this pattern.

![][design-strategy]

#### Control Commands {-}

To accommodate the numerous different operations that can be executed on the hub, the command
pattern was used. This pattern allows disjoint commands to be executed with a single uniform
interface. This allows the hub to receive a command from a device, the user or the machine
learning, and then be able to execute it without knowledge of the command itself. This
pattern significantly simplifies the design of the hub.

![][design-command]

#### Reactive Interface {-}

In order to be able to respond to changes within the user's environment, the web client uses
a reactive display pattern. This pattern allows the user interface to re-render the components
that change whenever the underlying model changes. By doing so, the user interface is able to
perform updates when the state of the environment changes by listening to state push notifications.

![][design-react]


