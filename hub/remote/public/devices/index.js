import $    from 'jquery';
import Menu from '../nav/menu';
import './index.css';

$(document).ready(() => {
    $('body').append(new Menu().render().$el());
});
