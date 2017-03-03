import Component        from '../component';
import WidgetPanel      from '../widget/widget-panel';
import Service          from '../service/service';
import Button           from '../control/button';
import Dialog           from '../dialog/dialog';
import Session          from '../behaviour/session';
import AddSession       from './add-session';

import './session-panel.css';

class SessionPanel extends WidgetPanel {
    constructor (state, props) {
        super(state, props);
        this._state = {
            behaviour   : this._state.behaviour || {},
            sessions    : this._state.sessions  || []
        };
    }

    _prerender () {
        this.clear();
        this._buttonBar = new Component().addClass('session-button-bar');
        this._newButton = new Button('New');

        this.clearWidgets();
        this.append(this._buttonBar);

        this._state.sessions.forEach(this.addWidget.bind(this));
        this._buttonBar.append(this._newButton);

        super._prerender();
        return this;
    }

    _postrender () {
        this._newButton.click(newSession.bind(this));
        return this;
    }
}


function newSession () {
    let session = new AddSession({
            name        : '',
            behaviourId : this._state.behaviour.id
        }),
        dialog  = new Dialog(session,
            {
                title   : 'New Session',
                buttons : [
                    {
                        text    : 'Create',
                        click   : () => {
                            addSession.call(this, session);
                            dialog.remove();
                        }
                    }
                ]
            }).render().height(200).width(400);
}


function addSession (session) {
    Service.set('/hub/training/session', session.state())
        .then((res) => {
            var s = new Session(res.payload);
            this._state.sessions.push(s);
            this.render();
        });
}

export default SessionPanel;
