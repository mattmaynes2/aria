import Component    from '../component';
import Button       from '../control/button';
import Dialog       from '../dialog/dialog';

import './control.css';

class BehaviourControl extends Component {
    constructor (state, props) {
        super(state, props);
        this._sessions  = new Button('Sessions').addClass('behaviour-control-button');
        this._remove    = new Button('Remove').addClass('behaviour-control-button');
        this.append([this._sessions, this._remove]);
        this.addClass('behaviour-control');
        this._added = false;
    }
    _postrender () {
        if (!this._added) {
            this._added = true;
            this._remove.click(remove.bind(this));
            this._sessions.click(sessions.bind(this));
        }
    }
}

function sessions () {
    new Dialog(
        '',
        {
            title   : `${this._state.title} Sessions`,
            close   : true
        }
    ).render();
}

function remove () {
    let d = new Dialog(
        `Removing behaviour '${this._state.title}' will remove all associated training ` +
        'session data. Are you sure you want to remove it?',
        {
            title   : `Remove ${this._state.title}`,
            close   : false,
            buttons : [
                {
                    text    : 'Cancel',
                    click   : () => { d.remove(); }
                },
                {
                    text    : 'Remove',
                    click   : () => { console.log('Removing behaviour'); d.remove(); }
                }
            ]
        }
    ).width(400).height(200).render();
}

export default BehaviourControl;
