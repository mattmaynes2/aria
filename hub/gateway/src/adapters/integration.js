let uuid    = require('node-uuid'),
    logger  = require('winston'),
    IPC     = require('../ipc');

let IntegrateAdatper = (function () {

    let DEVICE_TYPES = ['zwave', 'wemo', 'arduino'],
        DEVICE_NAMES = [
            'light',
            'switch',
            'light sensor',
            'temperature sensor',
            'music player',
            'coffee maker',
            'thermostat'
        ],
        HUB_ID = new Buffer(16).fill(0);

    function IntegrateAdatper () {
        var i, n;
        logger.debug('Gateway entering testing mode');

        this._id = new Buffer(16);
        this._state = {
            hub : {
                version : '1.0.0',
                mode    : 1,
                devices : []
            }
        };

        n = Math.ceil(Math.random() * 10);
        logger.debug(`Seeding hub with ${n} devices`);

        for (i = 0; i < n; i++) {
            this._state.hub.devices.push({
                type    : DEVICE_TYPES[Math.floor(Math.random() * DEVICE_TYPES.length)],
                name    : DEVICE_NAMES[Math.floor(Math.random() * DEVICE_NAMES.length)],
                address : uuid.v4()
            });
        }

        uuid.v4(null, this._id);
    }

    IntegrateAdatper.prototype.register = function () {
        logger.debug('Received request to register server');
        return Promise.resolve();
    };

    IntegrateAdatper.prototype.id = function () {
        return uuid.unparse(this._id);
    };

    IntegrateAdatper.prototype.send = function (type, payload) {
        logger.debug(`Sending test message of type ${type} with payload ` +
            JSON.stringify(payload));

        return new Promise((resolve, reject) => {
            var response;
            try {
                switch (type) {
                    case IPC.Request:
                        response = payload.get ?
                            requestGet.call(this, payload) :
                            requestSet.call(this, payload);
                        break;
                    case IPC.Event:
                        response = event.call(this, payload);
                        break;
                    default:
                        logger.error('Invalid message type');
                        reject('Invalid message type');
                }
            }
            catch (e) {
                reject(e.message);
            }
            resolve(response);
        });
    };

    function wrap (res, value) {
        return {
            type        : IPC.Request,
            sender      : HUB_ID,
            destination : this._id,
            payload     : {
                response    : res,
                value       : value
            }
        };
    }


    function requestGet (payload) {
        switch (payload.get) {
            case 'status':
                return wrap(payload.get, {
                    version     : this._state.hub.version,
                    mode        : this._state.hub.mode,
                    devices     : this._state.hub.devices.length
                });
            case 'mode':
                return wrap(payload.get, this._state.hub.mode);
            case 'devices':
                return wrap(payload.geta, this._state.hub.devices);
            default:
                throw new Error('Unknown request');
        }
    }

    function requestSet (payload) {
        switch (payload.set) {
            case 'mode':
                this._state.hub.mode = payload.value;
                break;
            default:
                throw new Error ('Unknown request');
        }
        payload.get = payload.set;
        return requestGet.call(this, payload);
    }




    function event () {
        return {};
    }
    return IntegrateAdatper;
} ());

module.exports = IntegrateAdatper;
