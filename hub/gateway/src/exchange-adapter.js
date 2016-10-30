var ExchangeAdapter = (function () {
    var dgram   = require('dgram'),
        uuid    = require('node-uuid'),
        packets = require('./ccp');

    function ExchangeAdapter (endpoint) {
        this.id         = new Buffer(16);
        this.registered = false;
        this.transport  = dgram;
        this.endpoint   = endpoint || {
            port    : 7600,
            address : 'localhost'
        };
        uuid.v4(null, this.id, 16);
    }

    ExchangeAdapter.prototype.register = function () {

        return new Promise ((resolve, reject) => {
            send.call(this, 1, {}).then((response) => {
                console.log('Got a response to discovery request');
                if (response.type !== 4) {
                    reject(Error('Communication server responded with an unexpected packet type'));
                }
                else {
                    this.registered = true;
                    resolve()
                }

            }, (err) => {
                reject(Error('Error in discovery request'));
            })
        })
    };

    ExchangeAdapter.prototype.send = function (type, payload) {
        if (!this.registered) {
            throw new Error('Exchange adapter is not yet registered');
        }
        return send.call(this, type, payload);
    };

    function send (type, payload) {
        return new Promise((resolve, reject) => {
            var client, packet, message, expiry;

            packet = {
                type        : type,
                sender      : this.id,
                destination : new Buffer(16).fill(0),
                payload     : payload
            };

            client  = this.transport.createSocket('udp4');
            message = packets.serialize(packet);
            expiry  = setTimeout(timeout, 5000);

            client.on('message', function(message) {
                console.log('Received response from comm server');
                client.close();
                clearTimeout(expiry);
                resolve(packets.parse(message));
            });


            client.send(message, 0, message.length,
                this.endpoint.port, this.endpoint.address,
                function (err) {
                    if (err) {
                        clearTimeout(expiry);
                        reject(Error(err));
                    }
                    console.log('Sent UDP message');
                }
            );
        });

    }

    function timeout (client, reject) {
        client.close();
        reject(Error('Response wait period timed out'));
    }


    return ExchangeAdapter;
} ());

module.exports = ExchangeAdapter;
