let express         = require('express'),
    socketio        = require('socket.io'),
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
        var app = express(), io = socketio(http.Server(app));

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

        io.on('connection', (socket) => {
            var emitters = DeviceRouter.SocketEvents.map((event) => {
                this._adapter.subscribe(event, (data) => {
                    socket.emit(event, data);
                });
            });

            socket.on('disconnect', () => {
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
        app.listen(port);
    };

    return Gateway;

} ());

module.exports = Gateway;

