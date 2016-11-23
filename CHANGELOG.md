Change Log
==========

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
