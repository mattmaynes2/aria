var packets = require('../src/ccp')
var expect = require('chai').expect
var uuid = require('node-uuid')

describe('Parse packet', function () {

    it('Should return an object representation of packet', function () {
        var senderUUIDBuf = new Buffer(16)
        var destinationUUIDBuf = new Buffer(16)

        uuid.v4(null, senderUUIDBuf, 0)
        uuid.v4(null, destinationUUIDBuf, 0)

        var expectedStructure = {
            type: 1,
            size: 23,
            sender: senderUUIDBuf,
            destination: destinationUUIDBuf,
            payload: {
                version : "0.0.2"
            }
        }

        var payloadString = '{ "version" : "0.0.2" }'

        var payloadLengthB = new Buffer(4)
        payloadLengthB.fill(0)
        payloadLengthB.writeUInt32BE(payloadString.length, 0)

        const buf = Buffer.concat ([Buffer.from([0x01]),
                                   payloadLengthB,
                                   senderUUIDBuf,
                                   destinationUUIDBuf,
                                   Buffer.from(payloadString)]);

        expect(packets.parse(buf)).to.deep.equal(expectedStructure);
    });
});


describe('Serialize packet', function() {

    var senderUUIDBuf = new Buffer(16)
    var destinationUUIDBuf = new Buffer(16)

    uuid.v4(null, senderUUIDBuf, 0)
    uuid.v4(null, destinationUUIDBuf, 0)

    var packet = {
        type: 1,
        size: 23,
        sender: senderUUIDBuf,
        destination: destinationUUIDBuf,
        payload: {
            version : "0.0.2"
        }
    }

    var payloadString = '{ "version" : "0.0.2" }'

    var payloadLengthB = new Buffer(4)
    payloadLengthB.fill(0)
    payloadLengthB.writeUInt32BE(payloadString.length, 0)

    const expectedBuffer = Buffer.concat ([Buffer.from([0x01]),
                               payloadLengthB,
                               senderUUIDBuf,
                               destinationUUIDBuf,
                               Buffer.from(payloadString)]);

    //expect(packets.serialize(packet)).to.deep.equal(expectedBuffer);
})
