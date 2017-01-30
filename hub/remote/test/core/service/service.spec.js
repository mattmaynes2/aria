import $        from 'jquery';
import Service  from '../../../public/core/service/service';

describe('Service', function () {
    let MockRequest = (function () {

        function MockRequest (options) {
            this.readyState     = 0;
            this.status         = 0;
            this.responseText   = '';
            this.payload        = '';
            this.method         = 'POST';
            this.endpoint       = '';
            this.header         = [];
            this.waitInterval   = 100;
            this.async          = true;

            this.onreadystatechange = function () {};
            this.config(options);
        }

        MockRequest.prototype.config = function (options) {
            $.extend(this, options || {});
        };

        MockRequest.prototype.setRequestHeader = function (tag, value) {
            this.header.push({ tag : value });
        };

        MockRequest.prototype.open = function (method, endpoint, async) {
            this.method     = method;
            this.endpoint   = endpoint;
            this.async      = async;
        };

        MockRequest.prototype.send = function (payload, options) {
            this.payload        = payload;
            this.readyState     = 4;
            this.status         = 200;
            this.responseText   = '{}';
            this.config(options);

            if (this.async) {
                setTimeout(this.onreadystatechange.bind(this), this.waitInterval);
            }
        };

        return MockRequest;
    } ());


    beforeEach(function () {
        Service.Request = MockRequest;

        spyOn(MockRequest.prototype, 'setRequestHeader');
        spyOn(MockRequest.prototype, 'open');
        spyOn(MockRequest.prototype, 'send');
    });

    afterEach(function () {
        MockRequest.defaults = {};
    });

    it('Sends a get request', function () {
        Service.get('/abc/test');

        expect(MockRequest.prototype.open).toHaveBeenCalledWith('GET', '/abc/test', true);
        expect(MockRequest.prototype.send).toHaveBeenCalledWith('');
    });

    it('Sends a get request with parameters', function () {
        Service.get('/user', 'foo');

        expect(MockRequest.prototype.open).toHaveBeenCalledWith('POST', '/user', true);
        expect(MockRequest.prototype.send).toHaveBeenCalledWith('foo');
    });

    it('Sends a set request', function () {
        Service.set('/abc/name', 'foo');

        expect(MockRequest.prototype.open).toHaveBeenCalledWith('POST', '/abc/name', true);
        expect(MockRequest.prototype.send).toHaveBeenCalledWith('foo');
    });

    it('Sends a request that responds with a failure', function (done) {
        MockRequest.prototype.send.and.callFake(function (payload) {
            this.payload        = payload;
            this.readyState     = 4;
            this.status         = 500;
            this.responseText   = '{ "error" : "failure" }';

            if (this.async) {
                setTimeout(this.onreadystatechange.bind(this), this.waitInterval);
            }
       });

        Service.set('/abc/name', 'foo')
            .then(function () { fail(); })
            .catch(function (res) {
                expect(res.status).toEqual(500);
                expect(res.payload).toEqual({ error : 'failure' });
                done();
            });

        expect(MockRequest.prototype.open).toHaveBeenCalledWith('POST', '/abc/name', true);
        expect(MockRequest.prototype.send).toHaveBeenCalledWith('foo');
    });


});
