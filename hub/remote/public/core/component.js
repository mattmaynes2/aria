import $ from 'jquery';

/**
 * A component is an object representing a element or collection of elements in the DOM. Its
 * purpose is to provide a simple, uniform interface for all visual elements. Any component
 * must be displayable by simply invoking its render function. This should be true no matter
 * what the state of the component is. The state of an object should always reflect the current
 * model of the view that that the component represents.
 *
 * @public
 */
class Component {

    /**
     * Creates a new component with empty content
     *
     * @param [state] {object} State value being displayed by this component
     * @param [props] {object} Visual properties to use when rendering this component
     */
    constructor (state, props) {
        this._state     = state || {};
        this._props     = props || {};

        this._observers = {
            change  : [],
            click   : [],
        };

        this._decorations = [];
        this._children = [];
        this._$el = $('<div>');
    }

    /**
     * Updates the state of this component but does not re-render the component
     *
     * @param state {object} The new state of this component
     * @return {Component} The updated component
     */
    update (state) {
        this.state(state);
        return this;
    }

    /**
     * Renders this component and all of its children. Subclasses of the Component class should
     * avoid overriding this method and instead override the `_prerender` or `_postrender`
     * methods where applicable.
     *
     * @return {Component} The rendered version of this component
     */
    render () {
        this._$el.empty();
        this._prerender();
        this._$el
            .append(this._children.map((child) => { return child.render().$el(); }));
        this._decorations.forEach((decor) => {
            decor.render(this);
        });
        this._postrender();
        return this;
    }

    /**
     * Removes this component from the visible DOM
     *
     * @return {Component} The removed component
     */
    remove () {
        this._clickObserver = null;
        if (this._$el) { this._$el.remove(); }
        return this;
    }

    decorate (decor) {
        this._decorations.push(decor);
        return this;
    }

    $el (el) {
        if (arguments.length === 0) {
            return this._$el;
        }
        this._$el = el;
        return this;
    }

    append (c) {
        if (Array.isArray(c)) {
            c.forEach(this.append.bind(this));
        }
        else if (c instanceof Component) {
            this._children.push(c);
            this._$el.append(c.$el());
        }
        else {
            throw new Error('Cannot append element of type ' + typeof c + ' - expected Component');
        }
        return this;
    }

    clear () {
        this._$el.empty();
        this._children = [];
        return this;
    }

    children () {
        return this._children;
    }

    props (props) {
        if (arguments.length === 0) {
            return this._props;
        }
        this._props = $.extend(this._props || {}, props);
        return this;
    }

    change (observer) {
        if (this._observers.change.indexOf(observer) === -1) {
            this._observers.change.push(observer);
        }
        return this;
    }

    click (observer) {
        if (!this._clickObserver) {
            this._clickObserver = this._click.bind(this);
        } else {
            this._$el.off(this._clickObserver);
        }
        this._$el.click(this._clickObserver);

        if (this._observers.click.indexOf(observer) === -1) {
            this._observers.click.push(observer);
        }
        return this;
    }

    trigger (event, custom) {
        let id = '_' + event;

        if (this[id]) { this[id](custom); }
        return this;
    }

    _prerender () { return this; }
    _postrender () { return this; }

    _change (custom) {
        notify.call(this, this._observers.change, custom);
    }

    _click (custom) {
        notify.call(this, this._observers.click, custom);
    }
}

function notify (V, e) {
    V.forEach((v) => { v(this._state, this, e); });
}

function wrap (s, t, a) {
    this[t] = function (x) {
        if (arguments.length === 0) {
            return a ? this[s] : this[s][t]();
        }
        if (a) { this[s] = x; } else { this[s][t](x); }
        return this;
    };
}

[ 'width', 'height', 'addClass', 'removeClass', 'text', 'val' ].forEach((target) => {
    wrap.call(Component.prototype, '_$el' , target, false);
});

wrap.call(Component.prototype, '_state', 'state', true);


export default Component;

