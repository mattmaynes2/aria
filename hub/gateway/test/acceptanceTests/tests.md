1. Get System State

**Given that**
The communication server is running
**And**
the system version is 0.0.1
**When**
The user sends a GET request to the resource `/system/state`
**Then**
The gateway sends the following response:

{

    "version" : "0.0.1"

}
