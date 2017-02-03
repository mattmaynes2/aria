### H-7 Gateway Implementation {- #H-7}

![](./uml/GatewayClassDiagram.png)

#### Exchange Adapter {-}

The exchange adapter is responsible for communicating with the exchange server using inter process
communication with a connectionless socket. When the exchange adapter registers itself with the
exchange server it provides a callback port for asynchronous callback events. This allows the
exchange server to push communication to the gateway, which in turn forwards them on to the remote
client.

#### Test Adapter {-}

The test adapter allows the server to run independently of the exchange server and rely only on
integration tests. The integration tests provide a complete mock of the IPC protocol so that all
exchange communication is controlled. This is used for testing the gateway and remote client in
isolation from the exchange server.

#### Server {-}

The server class is the main class for the gateway project. This class initializes the appropriate
adapter object for the gateway class and binds itself to a port for serving data.

#### Gateway {-}

The gateway class provides a REST interface for communicating to the system over HTTP. The gateway
delegates the endpoints of the REST API to various routers. Internally, this is done using the
strategy pattern. As a request enters the system, it is routed to the appropriate handler based
on its URL.

#### HubRouter {-}

The hub router handles all requests for the hub endpoint. This router deals with communication
that will request or update the state of the central hub. The hub router is also responsible for
retrieving event logs from the hub's database.

#### DeviceRouter {-}

The device router handles all individual device requests. It is responsible for updating
individual device states as well as querying all device data.

#### IPC {-}

The IPC class is responsible for communicating to the exchange server. It serializes and
deserializes messages using the defined IPC protocol ([see IPC](#section-design-api-ipc)).
