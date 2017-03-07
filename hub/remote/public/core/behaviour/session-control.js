import Component    from '../component';
import Button       from '../control/button';
import Service      from '../service/service';

import './session-control.css';

class SessionControl extends Component {

    constructor (state, props) {
        super(state, props);
        this._start = new Button('Start').addClass('session-control-button');
        this._stop  = new Button('Stop').addClass('session-control-button');

        this.append([this._start, this._stop]);
        this.addClass('session-control');
        this._added = false;
    }

    _postrender () {
        if (!this._added) {
            this._added = true;
            this._start.click(start.bind(this));
            this._stop.click(stop.bind(this));
        }
    }
}


function start () {
    Service.set(`/hub/training/session/${this._state.id}/start`, {});
}

function stop () {
    Service.set(`/hub/training/session/${this._state.id}/stop`, {});
}

export default SessionControl;
