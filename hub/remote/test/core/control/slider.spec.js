import $        from 'jquery';
import Slider   from '../../../public/core/control/slider';

describe('Slider', function () {
    var slider;

    beforeEach(function () {
        slider = new Slider();
        $('body').append(slider._$el);
    });

    afterEach(function () {
        slider.remove();
    });

    describe('Domain Mapping', function () {
        it('Maps an integer domain to the visual domain and back', function () {
            slider.props({ max : 100, min : 0, step : 1 });
            for (var x = 0; x < 100; x++) {
                slider.state(x).render();
                expect(slider.state()).toEqual(x);
            }
        });

        it('Maps a float domain to the visual domain and back', function () {
            slider.props({ max : 100, min : 0, step : 1, round : true }).state(51.65).render();

            expect(slider.state()).toEqual(52);
        });

        it('Maps a domain with a negative bound', function () {
            slider.props({ min : -10, max : 10, step : 1 });
            for (var x = -10; x < 10; x++ ){
                slider.state(x).render();
                expect(slider.state()).toEqual(x);
            }
        });
    });

    describe('Interaction', function () {
        it('Moves a slider and tests the value', function () {
            var e;
            slider.props({ max : 100, min : 0, step : 1 }).state(0).render();

            // Check the initial state
            expect(slider.state()).toEqual(0);

            e = new $.Event('mousedown');
            e.clientX = 0;
            slider._$el.trigger(e);

            // Move the mouse to the midpoint of the slider
            e = new $.Event('mousemove');
            e.clientX = (slider._$el.width() - (slider._$target.width() / 2)) / 2;
            slider._$target.trigger(e);

            expect(slider.state()).toEqual(50);

            // Move the mouse to the end of the slider
            e = new $.Event('mousemove');
            e.clientX = slider._$el.width() + (slider._$target.width() / 2);
            slider._$target.trigger(e);

            expect(slider.state()).toEqual(100);
       });

        it('Uses a negative range and moves a slider and tests the value', function () {
            var e;
            slider.props({ min : -10, max : 10, step : 1 }).state(-2).render();

            // Check the initial state
            expect(slider.state()).toEqual(-2);

            // Start at the midpoint of the slider
            e = new $.Event('mousedown');
            e.clientX = (slider._$el.width() - (slider._$target.width() / 2)) / 2;
            slider._$el.trigger(e);

            // Move the mouse to the start of the slider
            e = new $.Event('mousemove');
            e.clientX = 0;
            slider._$target.trigger(e);

            expect(slider.state()).toEqual(-10);

            // Move the mouse to the end of the slider
            e = new $.Event('mousemove');
            e.clientX = slider._$el.width() + (slider._$target.width() / 2);
            slider._$target.trigger(e);

            expect(slider.state()).toEqual(10);
        });
   });

});
