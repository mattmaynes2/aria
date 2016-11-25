import Service  from '../../core/service/service';
import Widget   from '../../core/widget/widget';
import Event    from './event';

import './event-feed.css';

class EventFeed extends Widget {
    constructor () {
        super();
        this._state = {
            title   : 'Event Feed',
            events  : []
        };
        Service.socket.on('device.event', (e) => {
            var event = new Event(e);
            this._state.events = this._state.events.splice(0, 0, event).slice(0, 10);
            this._$el.find('.widget-body')
                .prepend(event.render().$el())
                .children().slice(10).remove();
        });
    }
    update () {
        Service.get('/hub/events', { start : 0, count : 10 })
            .then((res) => {
                this._state.events = res.records.map((event) => {
                    return new Event(event);
                });
                this.render();
            });
        return this;
    }
    render () {
        super.render();
        this._$el
            .find('.widget-body')
            .empty()
            .append(this._state.events.map((event) => {
                return event.render().$el();
            }));
        return this;
    }
}

export default EventFeed;
