import $            from 'jquery';
import Component    from '../component';
import './widget.css';

class Widget extends Component {
    constructor () {
        super();
        this._state = {
            title   : 'Widget',
            body    : ''
        };
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
