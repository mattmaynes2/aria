let IPC = (function () {

    function parse (buffer) {
        var type        = buffer.readUIntBE(0, 1),
            size        = buffer.readUIntBE(1, 4),
            sender      = buffer.slice(5, 21),
            destination = buffer.slice(21, 37),
            payload     = JSON.parse(buffer.toString('utf8', 37));

        return {
            type: type,
            size: size,
            sender: sender,
            destination: destination,
            payload: payload
        };
    }

    function serialize (packet) {
        var payloadSize = JSON.stringify(packet.payload).length;

        var buf = new Buffer(5);

        buf.writeUInt8(packet.type, 0);
        buf.writeUInt32BE(payloadSize, 1);

        return  Buffer.concat ([buf,
                               packet.sender,
                               packet.destination,
                               Buffer.from(JSON.stringify(packet.payload))]);
    }

    return {
        Error       : 0,
        Discover    : 1,
        Request     : 2,
        Event       : 3,
        Ack         : 4,
        parse       : parse,
        serialize   : serialize
    };

} ());

module.exports = IPC;
