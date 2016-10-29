var Gateway = (function () {
    var express = require('express'),
        packets = require('./ccp');


    function Gateway (adapter) {
        this.adapter = adapter;
    }

    Gateway.prototype.start = function (port) {
        var app = express();

        app.get('/system/state', (req, res) => {
            this.adapter.send(2, {'action': 'status'}).then((response) => {
                res.send(JSON.stringify(packets.parse(response)));
            }, (err) =>{
                console.log('Error requesting system state from communication server', err);
            });
        });

        app.listen(port);
    };

    return Gateway;

} ());

module.exports = Gateway;

