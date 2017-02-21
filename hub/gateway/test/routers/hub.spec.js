var proxyquire = require('proxyquire');
var sinon = require('sinon');
var ipc = require('../../src/ipc');

describe('Test the endpoints provided by the hub router', function(){

    var express;
    var HubRouter;
    var stubAdapter;
    var stubApp;

    var setupStubForRoute = function () {
        stubApp = sinon.stub();
        stubApp.route = sinon.stub();
        stubApp.route.returns(stubApp);
        stubApp.get = sinon.stub();
        stubApp.post = sinon.stub();
        stubApp.get.returns(stubApp);
        stubApp.post.returns(stubApp);
        express.Router.returns(stubApp);
    };


    beforeEach(()=>{
        stubAdapter = sinon.stub();
        stubAdapter.send = sinon.stub();
        var stubPromise = sinon.stub();
        stubPromise.then = sinon.stub();
        stubPromise.catch = sinon.stub();     
        stubPromise.then.returns(stubPromise);
        stubAdapter.send.returns(stubPromise);

        express = sinon.stub();
        express.Router = sinon.stub();

        setupStubForRoute();

        HubRouter = proxyquire('../../src/routers/hub.js', {'express' : express});
    });


    it('Should have an endpoint for Adding Behaviours', () => {
        var hubRouter = new HubRouter(stubAdapter);
        hubRouter.router();

        var postFn = stubApp.post.withArgs('/training/behaviour').getCalls()[0].args[1];
        var req = { body: { name: 'test' }};
        var res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { 'create' : 'behaviour', 'name' : 
                                                                'test' });
    });

    it('Should have an endpoint for getting a list of behaviours', () => {
        var hubRouter = new HubRouter(stubAdapter);
        hubRouter.router();

        var postFn = stubApp.post.withArgs('/training/behaviours').getCalls()[0].args[1];
        var req = { body: { start: 1, count: 10}};
        var res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { 'get' : 'behaviours', 'start': 1, 
                                                                'count': 10 });
    });

    it('Should have an endpoint for creating a new training session for a behaviour', () => {
        var hubRouter = new HubRouter(stubAdapter);
        hubRouter.router();

        var postFn = stubApp.post.withArgs('/training/session').getCalls()[0].args[1];
        var req = { body: { behaviourId: 1, name: 'test'}};
        var res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { 'behaviourId' : 1, 'create' : 
                                                                'session', 'name':'test' });
    });

    it('Should have an endpoint for activating a session', () => {
        var hubRouter = new HubRouter(stubAdapter);
        hubRouter.router();

        var postFn = stubApp.post.withArgs('/training/session/:id/start').getCalls()[0].args[1];
        
        var req = { params: { id: 1}, body: { behaviourId: 1}};
        var res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { 'id' : 1, 'activate' : 
                                                                                'session'});
    });

    it('Should have an endpoint for stopping a session', () => {
        var hubRouter = new HubRouter(stubAdapter);
        hubRouter.router();

        var postFn = stubApp.post.withArgs('/training/session/:id/stop').getCalls()[0]
                                                                                .args[1];
        var req = { params: { id: 1}, body: { behaviourId: 1}};
        var res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { 'id' : 1, 'deactivate' : 
                                                                                'session'});
    });

    it('Should have an endpoint for getting a list of training sessions for a behaviour', () => {
        var hubRouter = new HubRouter(stubAdapter);
        hubRouter.router(); 

        var getFn = stubApp.post.withArgs('/training/sessions').getCalls()[0].args[1];
        var req = { body: { start: 1, count: 10, behaviourId: 1}};
        var res = {};
        getFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { 'start' : 1,
                                                                 'count' : 10,
                                                                'behaviourId' : 1, 'get' : 
                                                                'sessions'});
    });

});
