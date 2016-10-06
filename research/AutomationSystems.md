Automation Systems
=============

### Background

What is this section in the context of this system?

### Relation to System

Why is this section being considered?


Insteon
------------

## Description

Insteon is a home automation system that allows control of the home through a phone. 
They have 

## Technical Overview

Technically speaking, what does this item do?
Insteon has a line of smart sensors and devices that using their hub. 

### Insteon Hub

The hub is a central device that connects to all of the Insteon devices sending commands 
and monitoring sensor states. The 

### Insteon devices

Insteon supports control of 

- lights
- outlets
- thermostats
- cameras 
- 

Insteon uses a peer-to-peer network to connect the devices. All of Insteon's devices
can act as a controller to send messages, a repeater to forward messages or a responder to receive messages

### API

 The Insteon provides a REST API to interact with their devices. 
 The API 

## Evaluation

How does this specific item do against our criteria?

Issue with integrating with insteon using their API is that it requires their central hub. 
Their hub system does most of what we want our system to do and we ould like to learn how to 
do this rather than just use someone elses.

Insteon has a spec for their messageing system and command structure which would
allow us to communicate with their devices without the use of the hub, however adding 
the support using their messageing and command structures  is <something here>. 
Adding support for Insteon devices is something that could be looked at in the future though 
is outside of the scope of the project for now.
-----------------------


### Summary of Evaluation

All of the evaluation grouped together

### Conclusion

What did we decide upon? Why?
