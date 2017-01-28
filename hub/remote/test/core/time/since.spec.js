import Since from '../../../public/core/time/since';

describe('Time Since', function () {
    var timer;

    beforeEach(function () {
        timer = new Since();
    });

    afterEach(function () {
        timer.remove();
    });

    it('Checks the title of the component', function () {
        var now = new Date();

        timer.state(now).render();
        expect(timer.$el().attr('title'))
            .toEqual(now.toLocaleString());
    });

    it('Checks a time within the last 10 seconds', function () {
        timer.state(new Date()).render();

        expect(timer.$el().text()).toEqual('now');
    });

    it('Checks a time within the last minute', function () {
        var time    = new Date(),
            delta   = Math.floor(Math.random() * 50 + 10);

        time.setSeconds(time.getSeconds() - delta);
        timer.state(time).render();

        expect(timer.$el().text()).toEqual(delta + 's');
    });

});
