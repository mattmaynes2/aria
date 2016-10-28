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

        const buf = Buffer.from ([1,
                                0, 0, 0, 4,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 16,
                                0, 0, 0, 0 ]);

        expect(packets.parse(buf)).to.deep.equal(expectedStructure);
    });
});


