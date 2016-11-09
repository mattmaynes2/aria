Aria - Autonomous Real-Time Interactive Architecture
====================================================

[![Build Status](https://travis-ci.com/mattmaynes2/aria.svg?token=MPuUxtfuLzmhXtay93BR&branch=master)](https://travis-ci.com/mattmaynes2/aria)

## Overview

Aria is a smart home automation system that learns from its environment and automatically automates
common actions. The Aria system uses a central hub to interconnect various smart devices through
multiple different communication mediums. The Aria hub uses smart sense through machine learning
to predict desired user interactions.

## Background

Any home maintenance task which can be automated can save the owner time and money. Automated
environmental control is not a novel concept; devices such as light timers and programmable
thermostats have existed for many years. Most of these common devices, however, must be configured
manually. The system proposed in this report is able to configure itself based on normal actions
taken by the user. By having the system learn the habits of the user dynamically, the
configuration is essentially eliminated, leading to an ease of installation that does not currently
exist.

## Project Deployment

To build the Aria system, a set of automated build scripts are provided in the `./build` folder.
The `./build/run` script provides all the facilities for configuring the project environment,
installing dependencies, building and testing the project, and deployment. Below is the help
information to the `run` script.

```
  Usage: run cmd [target]
    Performs the given build command. If a target is specified then run the
    command on just the given target.

  Commands:
    help        Displays this message and exit
    all         Installs all dependencies, runs a build and tests it
    enviro      Installs environmental dependencies
    deps        Installs project specific dependencies
    build       Builds and package project
    deploy      Starts running the built project
    clean       Cleans the build resources
    tests       Runs test configurations for project
```

To build the entire project, simply run `./build/run all`. Finally, to deploy the system after it
has been build, run `./build/run deploy`.


