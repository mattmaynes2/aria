import ColorPicker from '../../../public/core/control/color-picker';

describe('Color Picker', function () {
    var picker;

    beforeEach(function () {
        picker = new ColorPicker();
    });

    afterEach(function () {
        picker.remove();
    });

    function pad(hexString, length){
        var pad = '000000';
        return (pad+hexString).slice(-length);
    }

    function randomColor () {
        //16777215 is the number of possible colours
        return pad(Math.floor(Math.random() * 16777215).toString(16), 6);
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
