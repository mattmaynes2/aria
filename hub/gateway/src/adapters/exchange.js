let dgram   = require('dgram'),
    uuid    = require('node-uuid'),
    logger  = require('winston'),
    IPC     = require('../ipc'),
    observable = require('../../lib/observable');

let ExchangeAdapter = (function () {

    function ExchangeAdapter (endpoint, pushPort) {
        this._id        = new Buffer(16);
        this.registered = false;
        this.transport  = dgram;
        this.endpoint   = endpoint || {
            port    : 7600,
            address : 'localhost'
        };
        this.pushPort = pushPort;
        observable.create(this);
        uuid.parse('00000000-0000-0000-0000-000000000001', this._id);
    }

    ExchangeAdapter.prototype.register = function () {
        return new Promise ((resolve, reject) => {
            send.call(this, 1, 
                        new Buffer(16).fill(0), { 'port' : this.pushPort, 'name' : 'HttpGateway'})
                        .then(
                (response) => {
                logger.debug('Got a response to discovery request');
                if (response.type !== 4) {
                    reject(Error('Communication server responded with an unexpected packet type'));
                }
                else {
                    this.registered = true;
                    resolve();
                }

            }, () => {
                reject(Error('Error in discovery request'));
            });
        });
    };

    ExchangeAdapter.prototype.id = function () {
        return uuid.unparse(this._id);
    };

    ExchangeAdapter.prototype.send = function (type, payload) {
        if (!this.registered) {
            throw new Error('Exchange adapter is not yet registered');
        }
        return send.call(this, type, new Buffer(16).fill(0), payload);
    };

    ExchangeAdapter.prototype.sendTo = function(type, destination, payload) {
        if (!this.registered) {
            throw new Error('Exchange adapter is not yet registered');
        }
	    var destBuf = new Buffer(16);
	    uuid.parse(destination, destBuf);
        return send.call(this, type, destBuf, payload);
    };

    ExchangeAdapter.prototype.listen = function () {
        var server = dgram.createSocket('udp4');

        server.on('listening', function() {
            var address = server.address();
            logger.info('UDP Push server listening on address ', address.address, ' : ',
                        address.port);
        });

        server.on('message', (message, remote) => {
            logger.info('Got a push message from ', remote.address, ' : ', remote.port);
            logger.debug('Raw message is: 0x' + message.toString('hex'));
            try {
                var parsed = IPC.parse(message);
                logger.debug('Push message payload: ', parsed.payload);
                this.signal(observable.NEXT, parsed.payload.event, parsed.payload);
            } catch (err) {
                logger.error('Error parsing push message from exchange. Stack:', err.stack);
                this.signal(observable.ERROR, 'error',  err);
            }
        });

        server.on('close', () => {
            this.signal(observable.COMPLETE, 'complete');
        });

        server.on('error', (err) => {
            this.signal(observable.ERROR, 'error', err);
        });

        server.bind(this.pushPort);
    };


    function send (type, destination, payload) {
        return new Promise((resolve, reject) => {
            var client, packet, message, expiry;

            packet = {
                type        : type,
                sender      : this._id,
                destination : destination,
                payload     : payload
            };

            client  = this.transport.createSocket('udp4');
            message = IPC.serialize(packet);
            expiry  = setTimeout(() => {
                client.close();
                reject(Error('Response wait period timed out'));
            }, 5000);

            client.on('message', function (message) {
                logger.debug('Received response from comm server');
                client.close();
                clearTimeout(expiry);
                resolve(IPC.parse(message));
            });

            client.send(message, 0, message.length,
                this.endpoint.port, this.endpoint.address,
                function (err) {
                    if (err) {
                        clearTimeout(expiry);
                        reject(Error(err));
                    }
                    logger.debug('Sent UDP message');
                }
            );
        });

    }

    return ExchangeAdapter;
} ());

module.exports = ExchangeAdapter;
