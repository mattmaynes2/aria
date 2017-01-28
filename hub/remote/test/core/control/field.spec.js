import Field from '../../../public/core/control/field';


describe('Field', function () {
    var field;

    beforeEach(function () {
        field = new Field();
    });

    afterEach(function () {
        field.remove();
    });

    it('Should block a change event for an non-editable field', function () {
        field.props({ editable : false }).render().change(() => { fail(); }).trigger('change');
    });
});
