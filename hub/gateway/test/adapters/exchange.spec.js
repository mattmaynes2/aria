var ExchangeAdapter = require('../../src/adapters/exchange');
//var IPC = require('../../src/ipc')
var sinon = require('sinon');
var assert = require('assert');

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

    var adapter;
    var fakeSocket;

    beforeEach(function() {
      adapter =  new ExchangeAdapter();
      fakeSocket = new FakeSocket();
      sinon.stub(adapter.transport, 'createSocket', () => { return fakeSocket; });
     });

     afterEach(function () {
        adapter.transport.createSocket.restore();
     });

    it('Should send messages over UDP to the exchange server', function(){
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
        adapter.registered = true;
        adapter.send(2, payload).then(()=>{
        }).catch(()=>{
            assert(false);
        })
   });

   it("Should signal that an error has occurred if an error response is received", () => {
        var payload = {'response':'Invalid Message'};

        var sizeBuf = new Buffer(4);
        sizeBuf.fill(0);
        sizeBuf.writeUInt32BE(JSON.stringify(payload).length);

        var errorResponse = Buffer.concat([Buffer.from([0x00]),
                                            sizeBuf,
                                            new Buffer(16).fill(0),
                                            adapter._id,
                                            Buffer.from(JSON.stringify(payload))]);
        fakeSocket.setNextResponse(errorResponse);
        adapter.registered = true;
        var error = false;
        adapter.send(2, {}).then(()=>{
            assert(false, "Promise did not error as expected");
        }).catch(()=>{
        });
   });
});
