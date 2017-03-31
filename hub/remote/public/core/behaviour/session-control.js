import Component    from '../component';
import Button       from '../control/button';
import Service      from '../service/service';

import './session-control.css';

class SessionControl extends Component {

    constructor (state, props) {
        super(state, props);

        this._started = this._props.isActive;
        this._start = new Button('Start').addClass('session-control-button');
        this._stop  = new Button('Stop').addClass('session-control-button');
        if (!this._state.stopped && !this._props.hideButtons) {
           

            if (this._props.isActive) {
                this.append(this._stop);
            }
            else {
                this.append([this._start, this._stop]);
            }
        }

        this.addClass('session-control');
    }
    _postrender () {
        this._start.$el().off().click(start.bind(this));
        this._stop.$el().off().click(stop.bind(this));

        if (this._state.stopped) {
            this._$el.append(
                new Component()
                    .addClass('session-complete')
                    .render()
                    .$el()
                    .text('Session Complete')
            );
        }

    }
}


function start () {
    Service.set(`/hub/training/session/${this._state.id}/start`, {})
        .then(() => {
            this._started = true;
            this._start.remove();
            this._$el.parent().parent().addClass('session-active');
        });
}

function stop () {
    if (this._started) {
        Service.set(`/hub/training/session/${this._state.id}/stop`, {})
            .then(() => {
                this._state.stopped = true;
                this.clear().render();
                this._$el.parent().parent().removeClass('session-active');
            });
    }
}

export default SessionControl;
