var Timer = (function () {

    function Timer () {
        this._start = [0, 0];
        this._end = [0, 0];
    }

    Timer.prototype.start = function () {
        this._start = process.hrtime();
        return this;
    };

    Timer.prototype.stop = function () {
        this._end = process.hrtime(this._start);
        return this;
    };

    Timer.prototype.seconds = function () {
        return this._end[0] + (this._end[1] / 1000000000);
    };

    Timer.prototype.milliseconds = function () {
        return (this._end[0] * 1000) + (this._end[1] / 1000000);
    };

    Timer.prototype.microseconds = function () {
        return (this._end[0] * 1000000) + (this._end[1] / 1000);
    };

    return Timer;
} ());

module.exports = Timer;
