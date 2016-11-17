let Timer = require('./timer');

let CPUClock = (function () {

    function CPUClock () {
        this._timer = new Timer();
        this._start = {};
        this._end = {};
    }

    CPUClock.prototype.start = function () {
        this._timer.start();
        this._start = process.cpuUsage();
        return this;
    };

    CPUClock.prototype.stop = function () {
        this._timer.stop();
        this._end = process.cpuUsage(this._start);
    };

    CPUClock.prototype.usage = function () {
        var ms = this._timer.microseconds();
        return {
            user    : this._end.user / ms,
            system  : this._end.system / ms
        };
    };

    CPUClock.prototype.active = function () {
        return this._end.user + this._end.system;
    };

    CPUClock.prototype.idle = function () {
        return this._timer.microseconds() - this.active();
    };

    return CPUClock;
} ());

module.exports = CPUClock;
