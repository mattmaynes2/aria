import Component from '../core/component';
import './menu.css';

class Menu extends Component {
    constructor () {
        super();
    }
    render () {
        this._$el.addClass('nav-menu');
        return this;
    }
}

export default Menu;
