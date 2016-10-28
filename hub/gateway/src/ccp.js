var uuid = require('node-uuid')

module.exports.parse = function (buffer) {
    var type = buffer.readUIntBE(0, 1)
    var size = buffer.readUIntBE(1, 4)
    var sender = buffer.slice(5, 21)
    var destination = buffer.slice(21, 37)
    var payload = JSON.parse(buffer.toString('utf8', 37))

    return {
        type: type,
        size: size,
        sender: sender,
        destination: destination,
        payload: payload
    };
};
