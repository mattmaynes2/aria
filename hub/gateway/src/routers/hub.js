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
                .send(IPC.Request, { get : 'status' })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this, res));
        });

        app.get('/discover', (req, res) => {
            this._adapter
                .send(IPC.Request, { action : 'discover' })
                .then(() => {
                    res.json({});
                })
                .catch(onError.bind(this, res));
        });

        app.route('/mode')
            .get((req, res) => {
                this._adapter
                    .send(IPC.Request, { get : 'mode' })
                    .then((reply) => {
                        res.json({ mode : reply.payload.value });
                    })
                    .catch(onError.bind(this, res));
            })
            .post((req, res) => {
                this._adapter
                    .send(IPC.Request, { set : 'mode', value : req.body.mode})
                    .then((reply) => {
                        res.json({ mode : reply.payload.value });
                    })
                    .catch(onError.bind(this, res));
            });
            
        app.route('/events')
            .post((req, res) => {
                this._adapter
                    .send(IPC.Request, {
                        get     : 'eventWindow',
                        start   : req.body.start,
                        count   : req.body.count
                    })
                    .then((reply) => {
                        res.json(reply.payload.value || { records : [] });
                    })
                    .catch(onError.bind(this, res));
            });

        return app;
    };

    function onError (res, err) {
        res.status(500).json({ error : err || '' });
    }

    return HubRouter;
} ());

module.exports = HubRouter;
