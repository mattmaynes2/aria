import Component    from '../core/component';
import WidgetPanel  from '../core/widget/widget-panel';
import Service      from '../core/service/service';
import Behaviour    from '../core/behaviour/behaviour';
import Button       from '../core/control/button';
import Dialog       from '../core/dialog/dialog';
import AddBehaviour from './add-behaviour';

import './training-panel.css';

class TrainingPanel extends WidgetPanel {
    constructor () {
        super();
        this._state = {
            behaviours: []
        };
    }

    update () {
        Service.get('/hub/training/behaviours', { start: 0, count: 10 }).then((res) => {
            this._state.behaviours = res.payload.records.map((b) => {
                return new Behaviour(b);
            });
            this.render();
        });
        return this;
    }
    _prerender () {
        this.clear();
        this._buttonBar = new Component().addClass('training-button-bar');
        this._newButton = new Button('New');


        this.clearWidgets();
        this._state.behaviours.forEach(this.addWidget.bind(this));

        this.append(this._buttonBar);
        this._buttonBar.append(this._newButton);
        super._prerender();

        return this;
    }
    _postrender () {
        this._newButton.click(newBehaviour.bind(this));
        return this;
    }
}

function newBehaviour () {
    let behaviour   = new AddBehaviour(),
        dialog      = new Dialog(behaviour,
            {
                title   : 'New Behaviour',
                buttons : [
                    {
                        text    : 'Create',
                        click   : () => {
                            addBehaviour.call(this, behaviour);
                            dialog.remove();
                        }
                    }
                ]
            }
        ).render().height(200).width(400);
}

function addBehaviour (behaviour) {
    Service.set('/hub/training/behaviour', behaviour.state())
        .then((res) => {
            var b = new Behaviour(res.payload);
            this._state.behaviours.push(b);
            this.render();
        });
}

export default TrainingPanel;
