let uuid        = require('node-uuid'),
    logger      = require('winston'),
    observable  = require('../../lib/observable'),
    IPC         = require('../ipc');

let IntegrateAdapter = (function () {

    let DEVICE_TYPES = ['zwave', 'wemo', 'arduino'],
        DEVICE_NAMES = [
            'Light',
            'Switch',
            'Light Sensor',
            'Temperature Sensor',
            'Music Player',
            'Coffee Maker',
            'Thermostat'
        ],
        DEVICE_ATTRIBUTES = [
            'State',
            'Brightness',
            'Hue'
        ],
        DATATYPES = [
            'binary',
            'int',
            'float',
            'color',
            'enum',
            'time',
            'date',
            'string'
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
                name    : 'Smart Hub',
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
        observable.create(this);
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
                    name        : this._state.hub.name,
                    devices     : this._state.hub.devices.length
                });
            case 'mode':
                return wrap(payload.get, this._state.hub.mode);
            case 'name':
                return wrap(payload.get, this._state.hub.name);
            case 'devices':
                return wrap(payload.get, this._state.hub.devices);
            case 'eventWindow':
                return wrap(payload.get, { total : 1500, records : makeEvents.call(this, payload)});
            case 'deviceEvents':
                return wrap(payload.get, { total : 100, records : makeEvents.call(this, payload)});
            default:
                throw new Error('Unknown request');
        }
    }

    function requestSet (payload) {
        switch (payload.set) {
            case 'mode':
                logger.debug(`Setting hub mode to ${payload.value}`);
                this._state.hub.mode = payload.value || 0;
                break;
            case 'name':
                logger.debug(`Setting hub name to ${payload.value}`);
                this._state.hub.name = payload.value;
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

    function makeEvents (payload) {
        var i, events = [], devices = this._state.hub.devices, device,
            start   = payload.start,
            count   = payload.count,
            id      = payload.id || '',
            index   = devices.map((dev) => { return dev.id; }).indexOf(id);

        for (i = 0; i < count; i++) {
            device  = index >= 0 ? devices[index] : random(devices);
            events.push({
                index       : start + i,
                timestamp   : new Date().toJSON(),
                source      : device.id,
                device      : device.name,
                attribute   : random(DEVICE_ATTRIBUTES),
                datatype    : random(DATATYPES),
                value       : Math.floor(Math.random() * 100)
            });
        }

        return events;
    }

    function random (arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }
    return IntegrateAdatper;
} ());

module.exports = IntegrateAdapter;
