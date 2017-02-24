import $            from 'jquery';
import Component    from '../component';

import './state-button.css';

class StateButton extends Component {
    constructor (state, props) {
        super();
        this._state = state || '';
        this._props = props || [];
    }
    render () {
        this._$el
            .empty()
            .addClass('state-button')
            .append(this._props.map((option, i) => {
                return $('<div>')
                    .addClass('state-button-item')
                    .text(option)
                    .click(buttonSelected.bind(this, i));
            }));

        select.call(this, this._state);
        return this;
    }
    state (state) {
        if (arguments.length === 0) {
            return this._state;
        }
        this._state = state;
        clearSelected.call(this, this._$el);
        select.call(this, this._state);
        return this;
    }
}

function clearSelected ($el) {
    $el.find('.state-button-selected').removeClass('state-button-selected');
}

function select (x) {
    let index = this._props.indexOf(x);
    if (index === -1) {
        index = Number(x);
    }
    this._$el.children().eq(index).addClass('state-button-selected');
}

function buttonSelected (index, e) {
    clearSelected(this._$el);
    $(e.delegateTarget).addClass('state-button-selected');
    this._state = this._props[index];
    this.trigger('change');
}

export default StateButton;
