import $         from 'jquery';
import Component from '../component';

import './event.css';

class Event extends Component {
    constructor (event) {
        super();
        this._state = event || {
            index       : 0,
            timestamp   : '',
            source      : '',
            device      : '',
            attribute   : '',
            datatype    : '',
            value       : ''
        };
    }
    render () {

        this._$icon = $('<div>').addClass('event-icon');
        this._$body = $('<div>')
            .addClass('event-body')
            .append([
                $('<div>').addClass('event-info').text(this._state.device),
                $('<div>').addClass('event-info').text(this._state.attribute),
                $('<div>').addClass('event-info').text(this._state.value)
            ]);

        this._$el
            .empty()
            .addClass('event-frame')
            .append([this._$icon, this._$body]);
        return this;
    }
}

export default Event;
