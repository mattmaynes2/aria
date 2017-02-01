### E-2 Nest Thermostat {- #E-2}

#### Description {-}

The Nest thermostat is a smart learning thermostat. Over time  the thermostat learns the
homeowner's routine and adjusts the temperature accordingly. The thermostat also turns off
automatically when it detects that nobody is home, and can be remotely controlled using a
smartphone app.

#### Technical Overview {-}

Nest communicates using WiFi and a custom nest protocol called **Nest Weave**. Nest Weave uses
WiFi and the Thread protocol.

Nest provides API support through the nest cloud. The API is accessed as a RESTful service or
using Firebase.

#### Evaluation {-}

The nest thermostat already has some machine learning on it. Trying to control it using our
algorithm could cause unexpected results. They also require the use of a cloud API to control
the thermostat and we are trying to avoid this and communicate locally with our devices. Due to
these resons it seems like the nest thermostat is not a great fit for our system and we should
not invest time into integrating with it.

