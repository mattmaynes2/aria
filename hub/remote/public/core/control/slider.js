import $            from 'jquery';
import Component    from '../component';

import './slider.css';

class Slider extends Component {
    constructor (state, props) {
        super();
        props = props || {};

        this._state = state || 0;
        this._props = {
            min     : props.min     || 0,
            max     : props.max     || 100,
            step    : props.step    || 1,
            round   : props.round   || false,
            color   : props.color   || ''
        };
        this._$target = $('<div>');

        $(document)
            .mouseup(() => {
                this._dragging = false;
                this._$target.removeClass('slider-target-active');
                this._changed();
            })
            .mousemove((e) => {
                if (this._dragging) {
                    updateValue.call(this, 0, this._max, this._offset + e.clientX - this._start);
                }
            });

    }

    render () {
        this._$el
            .empty()
            .addClass('slider-container')
            .append($('<div>').addClass('slider-body'))
            .append(this._$target.addClass('slider-target'));

        this._$el
            .off()
            .mousedown((e) => {
                this._dragging  = true;
                this._start     = e.clientX;
                this._max = this._$el.width() - this._$target.width();
                this._offset    = bound(0, this._max,
                    this._start - this._$el.offset().left - (this._$target.width() / 2)
                );
                this._$target.addClass('slider-target-active');
                updateValue.call(this, 0, this._max, this._offset);
                e.preventDefault();
                e.stopPropagation();
            });

        setValue.call(this, 0, 110, this._state);
        return this;
    }
}

function updateValue (lower, upper, value) {
    var x = bound(lower, upper, value),
        v = stepValue(
            mapDomain(lower, upper, this._props.min, this._props.max, value),
            this._props.step
        );

    this._$target.css('left', x);
    this._state = this._props.round ? Math.round(v) : v;
}

function setValue (lower, upper, value) {
    var x = mapDomain(this._props.min, this._props.max, lower, upper, value);

    this._$target.css('left', x);
    this._state = value;
}

function mapDomain (omin, omax, nmin, nmax, val) {
    return (nmax - nmin) * bound(0, 1, val / (omax - omin));
}

function stepValue (val, step) {
    var m = val % step;
    return m > (step / 2) ? val + step - m : val - m;
}

function bound (lower, upper, val) {
    return Math.min(upper, Math.max(lower, val));
}

export default Slider;
