let express         = require('express'),
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

    Gateway.prototype.start = function (port) {
        var app = express();

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

