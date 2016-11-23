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
        this._state = {
            title   : 'ARIA'
        };

        this._$menuGroup    = null;
        this._$menuItems    = [];
    }

    render () {
        this._$title = $('<div>').addClass('nav-title').text(this._state.title);
        this._$menuGroup = $('<div>').addClass('nav-menu-group');
        this._$menuGroup.append(PAGES.map((page) => {
            var $item = $('<div>')
                .addClass('nav-menu-item')
                .text(page.name)
                .click(() => { window.location = page.href; });
            this._$menuItems.push($item);
            return $item;
        }));

        this._$el.addClass('nav-menu').append(this._$title).append(this._$menuGroup);

        return this;
    }
}

export default Menu;
