### Introduction

#### Audience {-}

This document describes the high level architecture of the Aria system. It details the major
components within the system as well as their deployment artifacts. This document is intended
for a technical audience to understand the organization, deployment and internals of the
Aria system.

#### Background {-}

The automated real-time interactive architecture (ARIA) system provides software for a machine
learning smart home. The Aria system allows multiple smart devices to connect to a central hub
to create a smart home. The system observes a user in a home environment and uses historical
decisions to predict future actions.

This complex system is built upon several different subsystems that work together within a single
hub. The hub communicates to several different devices over different protocols that are all
synchronized with a custom Aria messaging protocol. This document outlines the details of these
subsystems, interactions and the Aria messaging protocol.


