var expect = require('chai').expect
var assert = require('chai').assert
var gateway = require('../src/gateway')
var sinon = require('sinon')

describe('Gateway REST API Logic', function () {

    it('Should return a version number when GET /system/state is called', function(){
        var app = {}
        app.get = sinon.spy()

        gateway.gateway(app)
        assert(app.get.calledWith('/system/state'), "Gateway does not provide /system/state endpoint")
    })
})
