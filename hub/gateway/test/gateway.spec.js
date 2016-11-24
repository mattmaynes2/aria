var sinon = require('sinon');
var proxyquire = require('proxyquire');

describe('Tests the REST endpoints exposed by the gateway', () => {

    var Gateway;
    var express;
    var fakeApp;
    var adapter;

    beforeEach(()=>{
        express = sinon.stub();
        adapter = sinon.stub();
        adapter.send = sinon.stub();

        Gateway = proxyquire('../src/gateway.js', {'express' : express});

        fakeApp = sinon.stub();
        fakeApp.get = sinon.stub();
        fakeApp.post = sinon.stub();
        fakeApp.use = sinon.stub();
        fakeApp.listen = sinon.stub();

        express.onFirstCall().returns(fakeApp);
    });

    it('Should forward requests for /request to the communication server', () => {

        var gateway = new Gateway(adapter);
        var registerRequest = fakeApp.post.withArgs('/request');
        var req = {
            body: {
                'action' : 'status'
            }
        };

        var res = sinon.stub();
        res.send = sinon.stub();

        gateway.start(800);

        sinon.assert.called(registerRequest);
        var endpointCallback = registerRequest.firstCall.args[1];

        var ret = {state:'some message'};

        var fakePromise = sinon.stub();
        fakePromise.then = sinon.stub();
        fakePromise.then.yields(ret);

        adapter.send.returns(fakePromise);
        endpointCallback(req, res);

        sinon.assert.calledWith(res.send, JSON.stringify(ret));
    });

});
