import Component from '../../src/core/component';

describe('Component', function () {
    var component;

    beforeEach(function () {
        component = new Component();
    });

    it('Checks setting el to undefined works', function () {
        expect(component.$el(undefined)).toEqual(component);
        expect(component.$el()).toEqual(undefined);
    });

    it('Checks that updating the component updates the state', function () {
        var state = Math.random();

        expect(component.update(state).state()).toEqual(state);
    });

});
