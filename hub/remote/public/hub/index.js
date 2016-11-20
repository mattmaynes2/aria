import $           from 'jquery';
import Menu        from '../nav/menu';
import WidgetPanel from '../core/widget-panel';
import Hub         from './hub';

import './index.css';

$(document).ready(() => {
    var panel, hub;

    hub     = new Hub();
    panel   = new WidgetPanel();

    hub.update();
    panel.addWidget(hub);

    $('body').append(new Menu().render().$el()).append(panel.$el());
    panel.render();
});
