var packets = require('../src/ccp')
var expect = require('chai').expect

describe('Parse packet', function () {

    it('Should return an object representation of packet', function () {
        var expectedStructure = {
            type: 1,
            size: 4,
            sender: 16,
            destination: 16,
            payload: 0
        }

        const buf = Buffer.from ([0x01,
                                0, 0, 0, 0x04,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x10,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0x10,
                                0, 0, 0, 0 ]);

        expect(packets.parse(buf)).to.deep.equal(expectedStructure);
    });
});


