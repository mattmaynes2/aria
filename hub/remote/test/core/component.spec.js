import Component from '../../public/core/component';

describe('Component', function () {
    var component;

    beforeEach(function () {
        component = new Component();
    });

    afterEach(function () {
        component.remove();
    });

    it('Checks setting el to undefined works', function () {
        expect(component.$el(undefined)).toEqual(component);
        expect(component.$el()).toEqual(undefined);
    });

    it('Checks that updating the component updates the state', function () {
        let state = Math.random();

        expect(component.update(state).state()).toEqual(state);
    });

    describe('Change Observers', function () {
        it('Adds a change observer to the component', function (done) {
            component.change(() => { done(); });
            setTimeout(component.trigger.bind(component, 'change'));
        });

        it('Validates change event parameters', function (done) {
            let token = Math.random(),
                state = Math.random();


            component.state(state);
            component.change((s, c, e) => {
                expect(c).toBe(component);
                expect(s).toEqual(state);
                expect(e).toEqual(token);
                done();
            });

            setTimeout(component.trigger.bind(component, 'change', token));
        });
    });

    describe('Click Observers', function () {
        it('Adds a click observer to the component', function (done) {
            component.click(() => { done(); });
            setTimeout(component.trigger.bind(component, 'click'));
        });

        it('Triggers a click event on the component', function (done) {
            component.click(() => { done(); });
            component.$el().click();
        });

        it('Validates click event parameters', function (done) {
            let token = Math.random(),
                state = Math.random();

            component.state(state);
            component.click((s, c, e) => {
                expect(c).toBe(component);
                expect(s).toEqual(state);
                expect(e).toEqual(token);
                done();
            });

            setTimeout(component.trigger.bind(component, 'click', token));
        });
    });
});
