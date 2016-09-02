import 'babel-polyfill';
import $ from 'jquery';
import Remote from './Remote';

$(document).ready(() => {
    new Remote().start();
});
