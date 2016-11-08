var Gateway = (function () {
    var express = require('express'),
        bodyParser = require('body-parser'),
        logger = require('winston');


    function Gateway (adapter) {
        this.adapter = adapter;
        this.public = 'public';
    }

    Gateway.prototype.start = function (port) {
        var app = express();

        app.use(bodyParser.json());
        app.get('/system/state', (req, res) => {
            this.adapter.send(2, {'action': 'status'}).then((response) => {
                res.send(JSON.stringify(response));
            }, (err) =>{
                logger.error('Error requesting system state from communication server', err);
            });
        });

        app.post('/request', (req, res) => {
            this.adapter.send(3, req.body).then((response) => {
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

