import $            from 'jquery';
import Menu         from '../nav/menu';
import DevicePanel  from './device-panel';
import './index.css';

$(document).ready(() => {
    var devices = new DevicePanel();

    $('body')
        .append(new Menu().render().$el())
        .append(devices.update().$el());
});
