import $            from 'jquery';
import Menu         from '../nav/menu';
import WidgetPanel  from '../core/widget/widget-panel';
import Hub          from './hub';
import EventFeed    from './events/event-feed';

import './index.css';

$(document).ready(() => {
    var panel, hub, events;

    panel   = new WidgetPanel();
    hub     = new Hub();
    events  = new EventFeed();

    hub.update();
    events.update();
    panel.addWidget(hub);
    panel.addWidget(events);

    $('body')
        .append(new Menu().render().$el())
        .append(panel.$el());
    panel.render();
});
