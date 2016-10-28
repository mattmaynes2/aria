module.exports.parse = function (buffer) {
    var type = buffer.readUIntBE(0, 1)
    var size = buffer.readUIntBE(1, 4)
    var sender = buffer.readUIntBE(5, 16)
    var destination = buffer.readUIntBE(21, 16)
    var payload = buffer.readUIntBE(37, size)

    return {
        type: type,
        size: size,
        sender: sender,
        destination: destination,
        payload: payload
    };
};
