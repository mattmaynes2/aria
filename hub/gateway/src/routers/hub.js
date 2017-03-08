let router  = require('express').Router,
    IPC     = require('../ipc'),
    logger          = require('winston');

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

        app.delete('/training/behaviour/:id', (req, res) => {
            this._adapter
                .send(IPC.Request, {
                    delete  : 'behaviour',
                    id      : req.params.id
                })
                .then((reply) => {
                    res.json(reply.payload.value || {});
                })
                .catch(onError.bind(this, res));
        });

        app.post('/training/behaviour', (req, res) => {
            this._adapter
                .send(IPC.Request, {
                    create  : 'behaviour',
                    name    : req.body.name
                })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this,res));
        });

        app.post('/training/behaviours', (req,res) => {
            this._adapter
                .send(IPC.Request, {
                    get     : 'behaviours',
                    start   : req.body.start,
                    count   : 10
                })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this,res));
        });

        app.delete('/training/session/:id', (req,res) => {
            this._adapter
                .send(IPC.Request, {
                    delete    : 'session',
                    id          : req.params.id
                })
                .then((reply) => {
                    res.json(reply.payload.value || {});
                })
                .catch(onError.bind(this,res));
        });

        app.post('/training/session', (req,res) => {
            this._adapter
                .send(IPC.Request, {
                    create      : 'session',
                    behaviourId : req.body.behaviourId,
                    name        : req.body.name
                })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this,res));
        });

        app.post('/training/sessions', (req,res) => {
            this._adapter
                .send(IPC.Request, {
                    get         : 'sessions',
                    start       : req.body.start,
                    count       : req.body.count,
                    behaviourId : req.body.behaviourId
                })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this,res));
        });

        app.post('/training/session/:id/start', (req,res) => {
            this._adapter
                .send(IPC.Request, {
                    activate    : 'session',
                    id          : req.params.id
                })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this,res));
        });

        app.post('/training/session/:id/stop', (req,res) => {
            this._adapter
                .send(IPC.Request, {
                    deactivate  : 'session',
                    id          : req.params.id
                })
                .then((reply) => {
                    res.json(reply.payload.value);
                })
                .catch(onError.bind(this,res));
        });

        return app;
    };

    function onError (res, err) {
        logger.error('Error handling request: ', err.message);
        res.status(500).json({ error : err.message || '' });
    }

    return HubRouter;
} ());

module.exports = HubRouter;
