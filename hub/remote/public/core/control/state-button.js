import $            from 'jquery';
import Component    from '../component';

import './state-button.css';

class StateButton extends Component {
    constructor (options) {
        super();
        this._state = {
            options     : options || [],
            value       : -1
        };
        this._listeners = [];
    }
    render () {
        this._$el
            .empty()
            .addClass('state-button')
            .append(this._state.options.map((option, i) => {
                return $('<div>')
                    .addClass('state-button-item')
                    .text(option)
                    .click(buttonSelected.bind(this, i));
            }))
            .children().eq(this._state.value).addClass('state-button-selected');

        return this;
    }
    val (val) {
        if (arguments.length === 0) {
            return this._state.options[this._state.value];
        }
        this._state.value = this._state.options.indexOf(val);
        clearSelected(this._$el);
        this._$el.children().eq(this._state.value).addClass('state-button-selected');
        return this;
    }
    options (options) {
        if (arguments.length === 0) {
            return this._state.options;
        }
        this._state.options = options;
        this.render();
        return this;
    }
    change (listener) {
        this._listeners.push(listener);
        return this;
    }
}

function clearSelected ($el) {
    $el.find('.state-button-selected').removeClass('state-button-selected');
}

function buttonSelected (index, e) {
    clearSelected(this._$el);
    $(e.delegateTarget).addClass('state-button-selected');
    this._state.value = index;
    notifyListeners(this._listeners, this);
}

function notifyListeners (listeners, state) {
    listeners.forEach((listener) => {
        listener(state);
    });
}

export default StateButton;
