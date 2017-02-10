let express         = require('express'),
    io              = require('socket.io'),
    http            = require('http'),
    bodyParser      = require('body-parser'),
    logger          = require('winston'),
    IPC             = require('./ipc'),
    HubRouter       = require('./routers/hub'),
    DeviceRouter    = require('./routers/device');

let Gateway = (function () {

    function Gateway (adapter) {
        this.public = 'public';
        this._adapter = adapter;
        this._routers = {
            hub     : new HubRouter(adapter),
            device  : new DeviceRouter(adapter)
        };
    }

    Gateway.SocketEvents = [
        'device.discovered',
        'device.event'
    ];


    Gateway.prototype.start = function (port) {
        var app = express(), server = http.createServer(app), websock = io(server);

        app.use(bodyParser.json());
        app.use((req, res, next) => {
            logger.debug('[' + new Date().toUTCString() + '] ' + req.method + ' ' + req.url);
            if (req.method === 'POST') {
                logger.debug('Message Body: ' + JSON.stringify(req.body));
            }
            next();
        });

        app.use('/hub'      , this._routers.hub.router());
        app.use('/device'   , this._routers.device.router());
        
        websock.on('connection', (socket) => {
            var emitters = Gateway.SocketEvents.map((event) => {
                return this._adapter.subscribe(event, (data) => {
                    logger.debug(`Received socket event ${event} - forwarding to clients`);
                    socket.emit(event, data);
                });
            });

            socket.on('disconnect', () => {
                logger.debug('Websocket disconnected');
                emitters.map((emitter) => { this._adapter.unsubscribe(emitter); });
            });
        });

        app.post('/request', (req, res) => {
            this._adapter.send(IPC.Request, req.body).then((response) => {
                res.send(JSON.stringify(response));
            }, (err) => {
                logger.error('Error sending request to communication server', err);
            });
        });

        app.use(express.static(this.public));
        server.listen(port);
        return this;
    };

    return Gateway;

} ());

module.exports = Gateway;

