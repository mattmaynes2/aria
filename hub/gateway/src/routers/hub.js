let router  = require('express').Router,
    IPC     = require('../ipc');

let HubRouter = (function () {

    function HubRouter (adapter) {
        this._adapter = adapter;
    }

    HubRouter.prototype.router = function () {
        var app = router();

        app.get('/state', (req, res) => {
            this._adapter
                .send(IPC.Request, { action : 'status' })
                .then((reply) => {
                    res.json(reply.payload);
                })
                .catch(onError.bind(this, res));
        });

        app.route('/mode')
            .get((req, res) => {
                this._adapter
                    .send(IPC.Request, { action : 'status' })
                    .then((reply) => {
                        res.json({ mode : reply.payload.mode });
                    })
                    .catch(onError.bind(this, res));
            })
            .post((req, res) => {
                this._adapter
                    .send(IPC.Request, { action : 'set_mode', mode : req.body.mode})
                    .then((reply) => {
                        res.json({ mode : reply.payload.mode });
                    })
                    .catch(onError.bind(this, res));
            });

        return app;
    };

    function onError (res, err) {
        res.status(500).json({ error : err });
    }

    return HubRouter;
} ());

module.exports = HubRouter;
