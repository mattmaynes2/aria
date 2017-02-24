let uuid        = require('node-uuid'),
    logger      = require('winston'),
    observable  = require('../../lib/observable'),
    IPC         = require('../ipc');

let IntegrateAdapter = (function () {

    let DEVICE_TYPES = [
        'Z-Wave',
        'SmartThings',
        'UPnP',
        'ZigBee',
        'WiFi'
        ],
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
        DEVICE_MAKERS = [
            'WeMo',
            'Phillips',
            'Aeon Labs',
            'Honeywell',
            'Nest',
            'Google',
            'Apple'
        ],
        DATA_TYPES = [
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

    function IntegrateAdapter () {
        var i, n;
        logger.debug('Gateway entering testing mode');

        this._id = new Buffer(16);
        this._state = {
            hub : {
                version     : '1.0.0',
                mode        : 1,
                name        : 'Smart Hub',
                devices     : [],
                behaviours  : []
            }
        };

        n = randomInt(10);
        logger.debug(`Seeding hub with ${n} devices`);

        for (i = 0; i < n; i++) {
            this._state.hub.devices.push(makeDevice());
        }

        uuid.v4(null, this._id);
        observable.create(this);
        spawnEvent.call(this);
    }

    IntegrateAdapter.prototype.register = function () {
        logger.debug('Received request to register server');
        return Promise.resolve();
    };

    IntegrateAdapter.prototype.listen = function () {};
    IntegrateAdapter.prototype.id = function () {
        return uuid.unparse(this._id);
    };

    IntegrateAdapter.prototype.send = function (type, payload) {
        logger.debug(`Sending test message of type ${type} with payload ` +
            JSON.stringify(payload));

        return new Promise((resolve, reject) => {
            var response;
            try {
                switch (type) {
                    case IPC.Request:
                        if (payload.action) {
                            response = requestAction.call(this, payload);
                        }
                        else {
                            response = makeRequest.call(this, payload);
                        }
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

    IntegrateAdapter.prototype.sendTo = function (type, id, payload) {
        logger.debug(`Setting device ${id} attribute ` + payload.set + ' to ' +
            JSON.stringify(payload.value));

        return new Promise((resolve) => {
            setAttribute(getDevice.call(this, id) || {}, payload.set, payload.value);
            resolve(wrap(payload.set, payload.value));
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

    function makeRequest (payload) {
        var response;
        if (payload.get) {
            response = requestGet.call(this, payload);
        }
        else if (payload.set){
            response = requestSet.call(this, payload);
        }
        else if (payload.create) {
            response = requestCreate.call(this, payload);
        }
        return response;
    }

    function requestAction (payload) {
        switch(payload.action) {
            case 'discover':
                logger.debug('Received request to launch discovery');
                setTimeout(() => {
                    var i, dev;
                    for (i = 0; i < 1 + randomInt(5); i++) {
                        dev = makeDevice();
                        setTimeout(
                            this.signal.bind(this, observable.NEXT, 'device.discovered', dev),
                            (1 + i) * randomInt(1000)
                        );
                        this._state.hub.devices.push(dev);
                    }
                }, 500);
                return wrap(payload.action, {});
            default:
                throw new Error('Unknown request');

        }
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
            case 'behaviours' :
                return wrap(payload.get, {
                    records     : this._state.hub.behaviours.slice(
                        payload.start,
                        Math.min(
                            this._state.hub.behaviours.length,
                            payload.start + payload.count
                        )
                    )
                });
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

    function requestCreate (payload) {
        var index, res;

        switch (payload.create) {
            case 'behaviour':
                logger.debug(`Creating a new behaviour with name ${payload.name}`);

                index = this._state.hub.behaviours.length;
                this._state.hub.behaviours.push({
                    name        : payload.name,
                    id          : index,
                    createdDate : generateTime(),
                    lastUpdated : generateTime(),
                    active      : true,
                    sessions    : []
                });
                res = wrap(payload.get, this._state.hub.behaviours[index]);
                logger.debug('Sending test response: ' + JSON.stringify(res));
                return res;
        }
    }

    function event () {
        return {};
    }

    function getDevice (id) {
        for (var dev in this._state.hub.devices) {
            if (dev.id === id) {
                return dev;
            }
        }
        return null;
    }

    function setAttribute (dev, name, params) {
        for (var attr in dev.attributes) {
            if (attr.name === name) {
                attr.parameters = params;
            }
        }
        return dev;
    }

    function makeEvents (payload) {
        var i, events = [], devices = this._state.hub.devices, device,
            start   = payload.start,
            count   = payload.count,
            id      = payload.id || '',
            last    = 0, offset = 0,
            index   = devices.map((dev) => { return dev.id; }).indexOf(id);

        for (i = 0; i < count; i++) {
            device  = index >= 0 ? devices[index] : random(devices);
            offset = last + randomInt(20000000);
            events.push(makeEvent(device, start, i, offset));
            last = offset;
        }

        return events;
    }

    function makeParameter () {
        var dataType = random(DATA_TYPES);
        return {
                name        : random(DEVICE_ATTRIBUTES),
                value       : generateValue(dataType),
                dataType    : dataType,
                min         : random(10),
                max         : 10 + random(10),
                step        : random(3)
        };
    }

    function makeAttribute () {
        return {
            name            : random(DEVICE_ATTRIBUTES),
            isControllable  : true,
            dataType        : random(DATA_TYPES),
            parameters      : [makeParameter()]
        };
    }

    function makeDevice () {
        var maker   = random(DEVICE_MAKERS), protocol = random(DEVICE_TYPES),
            name    = random(DEVICE_NAMES);

        return {
            version     : '' + randomInt(10) + '.' + randomInt(10) + '.' + randomInt(10),
            name        : name,
            address     : uuid.v4(),
            deviceType  : {
                name        : maker + ' ' + protocol + ' ' + name,
                maker       : maker,
                protocol    : protocol,
                attributes  : Array.apply([], Array(randomInt(10))).map(makeAttribute)
            }
        };
    }

    function makeEvent (device, start, i, offset) {
        return {
            index       : start + i,
            timestamp   : generateTime(offset),
            source      : device.id,
            device      : device.name,
            deviceType  : device.deviceType.name,
            attribute   : makeAttribute(),
            dataType    : random(DATA_TYPES),
        };
    }

    function generateTime (offset) {
        var now = new Date();

        if (offset) {
            now = new Date(now.getTime() - offset);
        }

        return now.getTime();
    }

    function generateValue (type) {
        switch (type) {
            case 'color':
                return toHex([randomInt(256), randomInt(256), randomInt(256)]);
            default:
                return randomInt(100);
        }
    }

    function spawnEvent () {
        setTimeout(() => {
            this.signal(
                observable.NEXT,
                'device.event',
                makeEvent(random(this._state.hub.devices), 0, 0)
            );
            spawnEvent.call(this);
        }, randomInt(5000));
    }

    function toHex (arr) {
        return arr.map((byte) => {
            return ('0' + (byte & 0xFF).toString(16)).slice(-2);
        }).join('');
    }

    function random (arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    function randomInt (max) {
        return Math.floor(Math.random() * max);
    }
    return IntegrateAdapter;
} ());

module.exports = IntegrateAdapter;
