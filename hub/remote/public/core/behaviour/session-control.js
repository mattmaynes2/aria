import Component    from '../component';
import Button       from '../control/button';
import Service      from '../service/service';

import './session-control.css';

class SessionControl extends Component {

    constructor (state, props) {
        super(state, props);

        this._added = true;
        if (!this._state.stopped || this._props.hideButtons) {
            this._start = new Button('Start').addClass('session-control-button');
            this._stop  = new Button('Stop').addClass('session-control-button');
            this.append([this._start, this._stop]);
            this._added = false;
        }

        this.addClass('session-control');
    }
    _postrender () {
        if (!this._added) {
            this._added = true;
            this._start.click(start.bind(this));
            this._stop.click(stop.bind(this));
        }
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
    this._started = true;
    Service.set(`/hub/training/session/${this._state.id}/start`, {})
        .then(() => {
            this._$el.parent().parent().addClass('session-active');
        });
}

function stop () {
    if (this._started) {
        this._state.stopped = true;
        this.clear().render();
        Service.set(`/hub/training/session/${this._state.id}/stop`, {})
            .then(() => {
                this._$el.parent().parent().removeClass('session-active');
            });
    }
}

export default SessionControl;
