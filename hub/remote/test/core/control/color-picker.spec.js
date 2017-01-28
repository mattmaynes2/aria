import ColorPicker from '../../../public/core/control/color-picker';

describe('Color Picker', function () {
    var picker;

    beforeEach(function () {
        picker = new ColorPicker();
    });

    afterEach(function () {
        picker.remove();
    });

    function randomColor () {
        return Math.floor(Math.random() * 16777215).toString(16);
    }

    it('Displays a color using hexadecimal values', function () {
        let color = randomColor();

        picker.state(color).render();
        expect(picker.$el().val()).toEqual('#' + color);
    });

    it('Changes the color in a picker', function (done) {
        let color = randomColor();

        picker.change((s) => {
            expect(s).toEqual(color);
            done();
        });

        picker.state(randomColor()).render().$el().val('#' + color).change();
    });

});
