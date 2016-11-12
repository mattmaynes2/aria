import $            from 'jquery';
import Component    from '../core/component';
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
        if (this._$el.hasClass('widget-panel')) {
            return this;
        }


        this._$el
            .addClass('widget-panel')
            .append($('<div>').addClass('widget-header').text(this._state.title))
            .append($('<div>').addClass('widget-body').text(this._state.body))
            .append($('<div>').addClass('widget-footer'));

        return this;
    }

}

export default Widget;

