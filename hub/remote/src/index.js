import $ from 'jquery';
import Home from './home';
import './index.css';


$(document).ready(() => {
    new Home().render();
});
