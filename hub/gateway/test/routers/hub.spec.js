var proxyquire = require('proxyquire');
var sinon = require('sinon');
var expect  = require('chai').expect;
var ipc = require("../../src/ipc")

describe('Test the endpoints provided by the hub router', function(){

    var subAdapter;
    var express;
    var HubRouter;
    var stubRouter;
    var stubRoute;
    var specificRouter;

    beforeEach(()=>{
        stubAdapter = sinon.stub();
        stubAdapter.send = sinon.stub();
        stubPromise = sinon.stub();
        stubPromise.then = sinon.stub();
        stubPromise.catch = sinon.stub();     
        stubPromise.then.returns(stubPromise);
        stubAdapter.send.returns(stubPromise);

        stubRoute = sinon.stub();
        stubRoute.post = sinon.stub();
        stubRoute.get = sinon.stub();
        stubRoute.get.returns(stubRoute);
        stubRoute.post.returns(stubRoute);

        stubRouter = sinon.stub();
        stubRouter.route = sinon.stub();
        stubRouter.route.returns(stubRoute);
        stubRouter.get = sinon.stub();
        stubRouter.post = sinon.stub();
        stubRouter.get.returns(stubRouter);
        stubRouter.post.returns(stubRouter);

        specificRouter = sinon.stub();
        specificRouter.get = sinon.stub();
        specificRouter.post = sinon.stub();
        specificRouter.get.returns(specificRouter);
        specificRouter.post.returns(specificRouter);

        express = sinon.stub();
        express.Router = sinon.stub();
        express.Router.returns(stubRouter);
        
        HubRouter = proxyquire('../../src/routers/hub.js', {'express' : express});
    });

    setupStubForRoute = function (route) {
        argsRouter = sinon.stub();
        argsRouter.route = sinon.stub();
        argsRouter.route.returns(stubRouter);
        argsRouter.route.withArgs(route).returns(specificRouter);
        argsRouter.get = sinon.stub();
        argsRouter.post = sinon.stub();
        argsRouter.get.returns(argsRouter);
        argsRouter.post.returns(argsRouter);
        express.Router.returns(argsRouter);
    };

    it("Should have an endpoint for Adding Behaviours", () => {
        setupStubForRoute("/training/behaviour");
        hubRouter = new HubRouter(stubAdapter);
        router = hubRouter.router();

        postFn = specificRouter.post.getCalls()[0].args[0];
        req = { body: { name: "test" }};
        res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { "create" : "behaviour", "name" : "test" });
    });

    it("Should have an endpoint for getting a list of behaviours", () => {
        setupStubForRoute("/training/behaviours");
        hubRouter = new HubRouter(stubAdapter);
        router = hubRouter.router();

        getFn = specificRouter.get.getCalls()[0].args[0];
        req = { body: { start: 1, count: 10}};
        res = {};
        getFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { "get" : "behaviours", "start": 1, "count": 10 });
    });

    it("Should have an endpoint for creating a new training session for a behaviour", () => {
        setupStubForRoute("/training/session");
        hubRouter = new HubRouter(stubAdapter);
        router = hubRouter.router();

        postFn = specificRouter.post.getCalls()[0].args[0];
        req = { body: { behaviourId: 1, name: "test"}};
        res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { "behaviourId" : 1, "create" : "session", "name":"test" });
    });

    it("Should have an endpoint for activating a session", () => {
        setupStubForRoute("/training/session/:id/start");
        hubRouter = new HubRouter(stubAdapter);
        router = hubRouter.router();

        postFn = specificRouter.post.getCalls()[0].args[0];
        req = { params: { id: 1}, body: { behaviourId: 1}};
        res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { "value" : 1, "start" : "session"});
    });

    it("Should have an endpoint for activating a session", () => {
        setupStubForRoute("/training/session/:id/stop");
        hubRouter = new HubRouter(stubAdapter);
        router = hubRouter.router();

        postFn = specificRouter.post.getCalls()[0].args[0];
        req = { params: { id: 1}, body: { behaviourId: 1}};
        res = {};
        postFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { "value" : 1, "stop" : "session"});
    });

    it("Should have an endpoint for getting a list of training sessions for a behaviour", () => {
        setupStubForRoute("/training/sessions");
        hubRouter = new HubRouter(stubAdapter);
        router = hubRouter.router(); 

        getFn = specificRouter.get.getCalls()[0].args[0];
        req = { body: { behaviourId: 1}};
        res = {};
        getFn(req, res);
        sinon.assert.calledWith(stubAdapter.send, ipc.Request, { "behaviourId" : 1, "get" : "sessions"});
    });

});
