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
                    setValue.call(this, 0, this._max, this._offset + e.clientX - this._start);
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
                this._max       = this._$el.width() - this._$target.width();
                this._offset    = bound(0, this._max,
                    this._start - this._$el.offset().left - (this._$target.width() / 2)
                );
                this._$target.addClass('slider-target-active');
                setValue.call(this, 0, this._max, this._offset);
                e.preventDefault();
                e.stopPropagation();
            });
        return this;
    }
}

function setValue (lower, upper, value) {
    var x   = bound(lower, upper, value),
        p   = bound(0, 1, value / (upper - lower)),
        s   = this._props.step,
        c   = p * (this._props.max - this._props.min),
        m   = c % s,
        v   = m > (s / 2) ? c + s - m : c - m;


    this._$target.css('left', x);
    this._state = this._props.round ? Math.round(v) : v;
}

function bound (lower, upper, val) {
    return Math.min(upper, Math.max(lower, val));
}

export default Slider;
