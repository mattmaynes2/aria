var packets = require('../src/ccp')

describe('Parse packet', function () {

    it('Should return an empty string', function () {
        expect(packets.parse()).toBe('');
    });
});
