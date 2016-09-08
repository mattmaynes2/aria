Machine Learning Smart Building
===============================

Supervisor: Babak Esfandiari


| Name              | Student Number | Email                              |
| ----              | -------------- | -----                              |
| Matthew Maynes    | 100882216      | mattmaynes@cmail.carleton.ca       |
| Cameron Blanchard | 100886476      | cameronblanchard@cmail.carleton.ca |
| Jeremy Dunsmore   | 100889935      | jeremydunsmore@cmail.carleton.ca   |
| Peter Mark        | 100886038      | petermark@cmail.carleton.ca        |



## Introduction



## Motivation

Supervised machine learning traditionally requires massive data sets with a map of inputs to
expected outputs. It then requires tuning, either automated or manual to achieve a desired level
of correctness. This process is tedious and massively time consuming.

Supervised learning also requires massive amounts of computation and data storage. One goal of
this system is to have records and learn sessions with live input and interactions from users in
a physical environment. This data will be mapped to the machine learning algorithm and then mapped
back to the physical domain.

The average person spends a large amount of time in their house, so any task in a home that becomes
automated saves the building owner a substantial amount of effort over time. There are many
commercial applications as well, such as in schools and nursing homes. Maintaining a building
requires at least one, if not more, full time staff. This amount of effort can be drastically
reduced by a system that handles it all automatically, saving time and money.

The downside of existing automated environment systems is the amount of configuration required to
have the system meet your specific needs. By having the system learn the habits of the user
dynamically, the configuration is essentially eliminated, leading to an ease of installation that
does not currently exist.

## Objectives

Currently, supervised learning algorithms require a complete input dataset and a meticulously
configured output to train the system. We want to have the algorithm be trained in a real world
environment where users perform live actions and the system determines relevant changes and
environmental factors. This automated learning system will be generic and use only the categorical
and numerical information provided by sensors and actuators.

Manual adjustment of a home's environment can be tedious. A goal of the project will be to use the
automated learning system to create a system that can be installed in the home to automatically
adjust the home environment based on input from a number of sensors. The system should support
simple configuration of any type of sensor; the system should not contain detailed knowledge about
any sensors and actuators.

This system will have dynamically updatable configuration of sensors and actuators. This will have
minimal overhead for adding and remove new devices from the system. The smart algorithm will then 
adjust to take these new devices into account when performing its computations.

## Technical Overview

## Schedule

| Item                                    | Date                 |
| ----                                    | ----                 |
| Machine Leaning Server Prototype        | September 25th, 2016 |
| Communicating Protocol + Service        | October 16th, 2016   |
| Sensor Communication and Discovery      | November 6th, 2016   |
| Sensors and Actuator Inputs and Control | November 6th, 2016   |
| Gateway + Web Client                    | January 29th, 2017   |
| Remote Record and Learn                 | February 12th, 2017  |

## Required Facilities





