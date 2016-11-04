### D-2 Technologies {-}

The Aria system is composed of many different technologies that each serve a different, task
specific purpose. This document outlines the details about the technologies chosen and the
reasons for them being selected. This document is broken down into the different subsystem
of the Aria system.

##### Exchange Server {-}

The exchange server is responsible for logging and sending messages throughout the Aria system.
The exchange server functions as the central communication point for all messages within the
Aria system. This server needs to support the main communication protocols that are required for
interfacing with several different protocols, including UDP, UPnP, Z-Wave and others. To
accommodate this requirement, Python 3 was selected as the primary language.

Python 3 offers support for most of the desired protocols since it can directly interface with
C it can support any external library implementations. As for the version decision of Python,
choosing 3 over version 2 allows us to use many of the new features that Python offers. It also
means that we are not writing Python using a set of deprecated standards.

###### Database {-}

The central exchange server needs to record all events and messages that it receives. This
database will be accessed by the exchange server and could be integrated into the exchange process.
The database needs to have transaction management but does not need to be a sophisticated database
server. SQLite provides all of the required features for this operation and provides the system
with a relational data store. Using SQLite means that the system will need SQL to read and write
data from the database.

###### Quality Control {-}

To maintain a desired level of quality in development, tooling will be needed to validate the
system. Both static and dynamic techniques for quality control will be used to aid in the
development of the smart home system. For static code analysis of the exchange hub, *pyflakes*
is being used to stop syntax errors. This tool reads a python file and reports if it conforms
to a set of desired constraints.

To check the system's dynamic functionality, the system has sets of integrated unit tests.
Python comes with a built in unit testing framework appropriately named *unittest*. This package
is being used to develop test stubs and test cases to validate the operations of the exchange.
To drive these tests, *nosetools* was used. This tool automatically discovers test cases and
manages running the test cases in a contained environment. The two tools complement each other
and create the basis for the exchange unit testing structure.

###### Communication Libraries {-}

In order to interface with different communication protocols, the central exchange is required to
use a number of different third party libraries to communicate. These libraries provide direct
translation from the exchange's internal message structure to the target devices communication
protocol.

####### WeMo {-}

The first of the these communication libraries is used to interface to WeMo devices and is titled
*ouimeaux*. This library provides the exchange command with the ability to discover WeMo devices,
get device states as well as send control commands.

##### HTTP Gateway {-}

The HTTP Gateway is responsible for serving static web content as well as enabling communication
from the web client to the exchange server. This server is a creates a thin wrapper around the
internal communication structure of the exchange server and serves it to the web client with a
RESTful API. To perform these tasks a simple, new web technology, *node.js* was used. Node is an
JavaScript interpreter that provides a massive set of server development tools and libraries.

One of the easiest to use node packages is a web server called *express*. Express is a web server
that is dynamically configured through code enables rapid development of a web server. This
technology has been used for the HTTP gateway to simplify the development.

###### Deployment {-}

In order to compile the server into a single executable, *webpack* was used. 

###### Quality Control {-}

- Mocha
- JSHint

- NPM
- Webpack

##### Remote {-}

- Webpack
- Babel
- NPM
- Jasmine
- Karma
- JSHint
- jQuery
- PhantomJS


