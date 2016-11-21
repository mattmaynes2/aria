let router  = require('express').Router,
    IPC     = require('../ipc');

let DeviceRouter = (function () {
    function DeviceRouter (adapter) {
        this._adapter = adapter;
    }

    DeviceRouter.prototype.router = function () {
        var app = router();

        app.get('/list', (req, res) => {
            this._adapter
                .send(IPC.Request, { get : 'devices' })
                .then((reply) => {
                    res.json({ devices : reply.payload.value });
                })
                .catch(onError.bind(this, res));
        });

        return app;
    };

    function onError (res, err) {
        res.status(500).json({ error : err });
    }

    return DeviceRouter;
} ());


module.exports = DeviceRouter;
