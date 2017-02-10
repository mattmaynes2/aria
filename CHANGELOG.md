Change Log
==========

## v0.5.2

- Training behaviours and sessions have been added to database and gateway
- Added release build command to build
- Removed report compilation from continuous integration

## v0.5.1

- Error Management
    - Web client now captures errors from requests and presents them to the user
- Notification History
    - Notifications that are sent to the user interface are now maintained in a history buffer

## v0.5.0

- Updated Database Design
    - Modified database storage to match specification
    - Added data types for device parameters and attributes
- User Interface
    - Added display fields for different data types
    - Added integrated control for actuators in the system
    - Introduced error handling for web client when disconnected from the ARIA system

## v0.4.0

- End-to-end Push Events
    - Gateway provides callback port for exchange data pushing
    - Gateway can now communicate over websockets
    - Client can receive messages using a websocket
- Exchange Database
    - Added event logging and retrieval
    - Stores discovered devices
- Web Client
   - Dynamic event feed
   - Device information
   - Added device discovery
- Software Devices
    - Added configurable software timer
    - Added interface for adding custom devices

## v0.3.0

- Build system re-write
    - Re-written in `node.js`
    - Added `--quiet` and `--silent` flags to build
    - Added build statistics with `--stats` flag
    - Added `--stay-alive` flag so build can run to completion even with errors
- Added initial database to central exchange
- Added database integration tests
- Gateway improvements
    - Expanded REST API in gateway
    - Gateway can now be run in isolation mode with `--test`
- Added remote interface
    - Skeleton of event feed
    - Addition of device controls
- Added adapter for software devices
    - Added software timer device

## v0.2.0

- Added WeMo device communication
- Added Arduino WiFi communication
- Exchange server
    - Added debugging logging
    - Added pid file to daemonized processes
- Added gateway logging
