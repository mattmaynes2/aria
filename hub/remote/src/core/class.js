var $ = require('jquery');

/**
 * @class Class
 *
 * Singleton object for creating prototypical class hierarchies. Class provides a utility
 * for doing prototypical inheritance.
 */
var Class = (function () {
    var Class = {};

    /**
     * Performs a prototype copy of a base class to a child target.
     * The child target constructor is then reset to be the correct
     * constructor.
     *
     * @param base      {function} Base class to inherit from
     * @param target    {function} Child class that will inherit
     */
    Class.inherit = function (base, target) {
        for (var key in base) { target[key] = base[key]; }
        target.prototype = Object.create(base.prototype);
        target.prototype.constructor = target;
    };

    /**
     * Decorates a class with a *clone* function for creating
     * object copies.
     *
     * @param target {function} Class to decorate
     */
    Class.cloneable = function (target) {
        inject(target.prototype, 'clone', cloneable(target));
    };

    /**
     * Injects a property into a prototype object with the given
     * field name if it does not already exist
     *
     * @param proto {object} Prototype object to inject into
     * @param field {string} Field name to inject
     * @param x     {any}    Data to inject
     */
    function inject (proto, field, x) {
        if ('undefined' === typeof proto[field]) {
            proto[field] = x;
        }
    }

    /**
     * Returns a function that will clone an instance of a target
     *
     * @param Target {function} Class to clone
     * @return {function} Cloning function
     */
    function cloneable (Target) {
        return function () {
            return $.extend(true, new Target(), this);
        };
    }

    return Class;
} () );

module.exports = Class;
