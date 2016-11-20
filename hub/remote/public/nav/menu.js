import $ from 'jquery';
import Component from '../core/component';
import './menu.css';

let PAGES = [
    {
        name    : 'Hub',
        href    : '../hub/'
    },
    {
        name    : 'Devices',
        href    : '../devices/'
    },
    {
        name    : 'Schedule',
        href    : '../schedule/'
    },
    {
        name    : 'Statistics',
        href    : '../stats/'
    }
];

class Menu extends Component {
    constructor () {
        super();
        this._$menuGroup = null;
        this._$menuItems = [];
    }
    render () {
        this._$menuGroup = $('<div>').addClass('nav-menu-group');
        this._$el.addClass('nav-menu').append(this._$menuGroup);

        this._$menuGroup.append(PAGES.map((page) => {
            var $item = $('<div>')
                .addClass('nav-menu-item')
                .text(page.name)
                .click(() => { window.location = page.href; });
            this._$menuItems.push($item);
            return $item;
        }));

        return this;
    }
}

export default Menu;
