### E-13 Summary of Evaluation {- #E-13}

Existing devices with an element of machine learning already incorporated in them are not
a good fit for our system, as they may cause unexpected results when introduced to our
custom machine learning algorithm. Similarly, devices that do not provide an API are also
not suitable for use in our system. Without being able to communicate with a device, there
is no way for us to control is from our hub or to retrieve data from it for the machine
learning algorithm. These aspects rule out devices such as the NEST thermostat and the irrigation
systems.

Third party Z-Wave devices are suitable for our system because they provide an easy method of
communication in a way that helps enable the machine learning rather than hinder it. Any device 
that has no special capabilities other than being Z-Wave ready are ideal, because they allow us
to use them with no unexpected behaviours. The Honeywell VisionPro Thermostat and devices from 
Aeon Labs are examples of this.


