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
