var ExchangeAdapter = require('../../src/adapters/exchange');
//var IPC = require('../../src/ipc')
var sinon = require('sinon');
//var assert = require('assert');

function FakeSocket(){

}

FakeSocket.prototype.setNextResponse = function(response){
    this.nextResponse = response;
};

FakeSocket.prototype.on = function(action, callback)
{
    this.messageCallback = callback;
};

FakeSocket.prototype.send = function()
{
    this.messageCallback(this.nextResponse);
};

FakeSocket.prototype.close = function(){};

describe('Exchange Adapter Testing', function(){

    it('Should send messages over UDP to the exchange server', function(){
        var adapter = new ExchangeAdapter();
        var fakeSocket = new FakeSocket();

        sinon.stub(adapter.transport, 'createSocket', () => { return fakeSocket; });

        var payload = {
            action  : 'status'
        };

        var sizeBuf = new Buffer(4);
        sizeBuf.fill(0);
        sizeBuf.writeUInt32BE(JSON.stringify(payload).length);

        var expectedBuffer = Buffer.concat([Buffer.from([0x02]),
                                        sizeBuf,
                                        adapter._id,
                                        new Buffer(16).fill(0),
                                        Buffer.from(JSON.stringify(payload))]);

        var discoveryAck = Buffer.concat([Buffer.from([0x04]),
                                            sizeBuf,
                                            new Buffer(16).fill(0),
                                            adapter._id,
                                            Buffer.from(JSON.stringify(payload))]);

        fakeSocket.setNextResponse(discoveryAck);

        adapter.register().then(()=>{
            var spy = sinon.spy(fakeSocket, 'send');
            adapter.send(2, payload).then(()=>{
                sinon.assert.calledWith(spy, expectedBuffer);
            });
        });
   });

//    it ('Should listen for push messages from the exchange server',function() {
//        var adapter = new ExchangeAdapter(null, 60000)
//        var fakeSocket = new FakeSocket();
//        sinon.stub(adapter.transport, 'createSocket', () => { return fakeSocket; });

//        // The name HttpGateway is apparently very important, don't change it unless you know why
//        var expectedPayload = { "port" : 60000, "name" : "HttpGateway"}; 
//        var spy = sinon.spy(fakeSocket, 'send');
//        adapter.register().then(() => {
//            var args = spy.args[0];
//            message = IPC.parse(args[0])
//            assert(message.payload.port === 60000);
//            assert(message.payload.name === 'HttpGateway');
//        })

//    });
});
