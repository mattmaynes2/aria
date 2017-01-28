import StateButton from '../../../public/core/control/state-button';

describe('State Button', function () {
    var button;

    beforeEach(function () {
        button = new StateButton();
    });

    afterEach(function () {
        button.remove();
    });

    it('Adds one button option', function () {
        expect(button.props(['a']).state('a').render().state()).toEqual('a');
    });

    it('Adds multiple button options', function () {
        expect(button.props(['a', 'b', 'c']).state('b').render().state()).toEqual('b');
    });

    it('Selects a button option and checks the state', function (done) {
        button.change((s) => {
            expect(s).toEqual('b');
            done();
        });

        button.props(['a', 'b', 'c']).state('a').render();
        button.$el().children().get(1).click();
    });
});
