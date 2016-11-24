import Component from '../component';
import './button.css';

class Button extends Component {
    constructor (title) {
        super();
        this._state = title || 'Button';
    }
    render () {
        this._$el.addClass('button').text(this._state);
        return this;
    }
    click (click) {
        this._$el.click(click);
    }
}

export default Button;
