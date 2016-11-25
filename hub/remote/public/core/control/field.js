import $            from 'jquery';
import Component    from '../component';

import './field.css';

class Field extends Component {
    constructor (state) {
        super();
        state = state || {};
        this._state = {
            label       : state.label    || '',
            value       : state.value    || '',
            editable    : state.editable || false
        };

        this._$label = $('<div>').addClass('field-label');
        this._$value = $('<div>').addClass('field-value');
    }
    render () {

        this._$label.text(this._state.label);
        this._$value.text(this._state.value).removeClass('field-editable');

        if (this._state.editable) {
            this._$value.addClass('field-editable');
        }

        this._$el
            .empty()
            .addClass('field-body')
            .append([this._$label, this._$value]);


        return this;
    }
    val (val) {
        this._$value.text(val);
        return this;
    }
    change () {
        return this;
    }
}

export default Field;
