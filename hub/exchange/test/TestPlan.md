Central Exchange Test Plan
==========================

This document outlines the acceptance test for the central exchange server. These are manual
tests that need to be completed for a minimum viable product.

## Startup

The server should start up and connect to a port for communication. The default port that should
be connected to is 7600. The server should accept a command line input for the port with the
flag `-p` or `--port`.

## Device Status

The exchange should be able to formulate a request for a device's status.

## Report System Status

The system should be able to report on its own status. The hub needs to have a state that can
be queried. This state should include the system mode as well as any other system details.


