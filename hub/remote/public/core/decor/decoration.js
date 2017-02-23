import $ from 'jquery';

class Decoration {
    constructor (props) {
        this._props = props || {};
    }

    props (props) {
        if (arguments.length === 0) {
            return this._props;
        }
        this._props = $.extend(this._props, props);
        return this;
    }

    render (target) {
        this._target = target;
        return this;
    }

}

export default Decoration;
