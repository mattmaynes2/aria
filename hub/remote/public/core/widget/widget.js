import $            from 'jquery';
import Component    from '../component';
import './widget.css';

class Widget extends Component {
    constructor (state, props) {
        super(state, props);
        this._state = this._state || {};
        this._state.title = this._state.title || 'Widget';
        this._state.body  = this._state.body  || '';
    }

    render () {
        this._$el
            .empty()
            .addClass('widget-frame')
            .append($('<div>').addClass('widget-header').text(this._state.title))
            .append($('<div>').addClass('widget-body').text(this._state.body))
            .append($('<div>').addClass('widget-footer'));

        return this;
    }

}

export default Widget;

