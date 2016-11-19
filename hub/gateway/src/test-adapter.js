let uuid    = require('node-uuid'),
    logger  = require('winston');

let TestAdapter = (function () {

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

    function TestAdapter () {
        this._id = new Buffer(16);
        logger.debug('Gateway entering testing mode');
        this.nDevices = 5;

        uuid.v4(null, this._id);
    }

    TestAdapter.prototype.register = function () {
        logger.debug('Received request to register server');
        return Promise.resolve();
    };

    TestAdapter.prototype.id = function () {
        return uuid.unparse(this._id);
    };

    TestAdapter.prototype.send = function (type, payload) {
        logger.debug(`Sending test message of type ${type} with payload ${payload}`);
        return new Promise((resolve, reject) => {
            var response;
            switch (type) {
                case 2:
                    response = request.call(this, payload);
                    break;
                case 3:
                    response = event.call(this, payload);
                    break;
                default:
                    logger.error('Invalid message type');
                    reject('Invalid message type');
            }
            logger.debug(`Responsding to message with ${response}`);
            resolve(response);
        });
    };


    function request (payload) {
        var i, devices = [];

        switch (payload.action) {
            case 'status':
                return {
                    type        : 2,
                    sender      : HUB_ID,
                    destination : this._id,
                    payload     : {
                        version     : '1.0.0',
                        mode        : 'Normal',
                        devices     : 5
                    }
                };
            case 'list_devices':
                for (i = 0; i < this.nDevices; i++) {
                    devices.push({
                        type    : DEVICE_TYPES[Math.floor(Math.random() * DEVICE_TYPES.length)],
                        name    : DEVICE_NAMES[Math.floor(Math.random() * DEVICE_NAMES.length)],
                        address : uuid.v4()
                    });
                }
                return {
                    type        : 2,
                    sender      : HUB_ID,
                    destination : this._id,
                    payload     : devices
                };
            default:
                return {};
        }
    }

    function event () {
        return {};
    }


    return TestAdapter;
} ());

module.exports = TestAdapter;
