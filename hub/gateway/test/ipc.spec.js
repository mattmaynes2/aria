var packets = require('../src/ipc');
var expect  = require('chai').expect;
var uuid    = require('node-uuid');

describe('Packet Parsing and Serialization', function () {

    describe('Packet Parsing', function() {

        it('Should return an object representation of packet', function () {
            var senderUUIDBuf = new Buffer(16);
            var destinationUUIDBuf = new Buffer(16);

            uuid.v4(null, senderUUIDBuf, 0);
            uuid.v4(null, destinationUUIDBuf, 0);

            var expectedStructure = {
                type: 1,
                size: 23,
                sender: senderUUIDBuf,
                destination: destinationUUIDBuf,
                payload: {
                    version : '0.0.2'
                }
            };

            var payloadString = '{ "version" : "0.0.2" }';

            var payloadLengthB = new Buffer(4);
            payloadLengthB.fill(0);
            payloadLengthB.writeUInt32BE(payloadString.length, 0);

            const buf = Buffer.concat ([Buffer.from([0x01]),
                                       payloadLengthB,
                                       senderUUIDBuf,
                                       destinationUUIDBuf,
                                       Buffer.from(payloadString)]);

            expect(packets.parse(buf)).to.deep.equal(expectedStructure);
        });
    });

    describe('Serialize packet', function() {

        it('Should create a byte buffer representation of a packet structure', function() {
            var senderUUIDBuf = new Buffer(16);
            var destinationUUIDBuf = new Buffer(16);

            uuid.v4(null, senderUUIDBuf, 0);
            uuid.v4(null, destinationUUIDBuf, 0);

            var packet = {
                type: 1,
                sender: senderUUIDBuf,
                destination: destinationUUIDBuf,
                payload: {
                    version : '0.0.2'
                }
            };

            var payloadLengthB = new Buffer(4);
            payloadLengthB.fill(0);
            payloadLengthB.writeUInt32BE(JSON.stringify(packet.payload).length, 0);

            const expectedBuffer = Buffer.concat ([Buffer.from([0x01]),
                                       payloadLengthB,
                                       senderUUIDBuf,
                                       destinationUUIDBuf,
                                       Buffer.from(JSON.stringify(packet.payload))]);

            expect(packets.serialize(packet)).to.deep.equal(expectedBuffer);
        });
    });

});



