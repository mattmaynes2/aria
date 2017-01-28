import Button from '../../../public/core/control/button';

describe('Button', function () {
    var button;

    beforeEach(function () {
        button = new Button();
    });

    afterEach(function () {
        button.remove();
    });

    it('Checks the text of a button', function () {
        expect(button.state('Test').render().$el().text()).toEqual('Test');
    });

    it('Ensures clicking the button triggers an event', function (done) {
        button.click(() => {
            done();
        });
        button.render().trigger('click');
    });

    it('Ensures clicking a button in the DOM triggers an event', function (done) {
        button.click(() => {
            done();
        });
        button.render().$el().click();
    });
});
