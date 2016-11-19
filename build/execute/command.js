let ProcStat = require('./procstat');

let Command = (function () {

    function Command (directive, target) {
        this._script     = '';
        this._root       = __dirname;
        this.directive  = directive || '';
        this.target     = target    || '';
        this.stat       = new ProcStat(target);
    }

    Command.ALL = ['enviro', 'deps', 'build', 'test'];

    Command.prototype.children = function (children) {
        if (arguments.length === 0) {
            return this._children;
        }
        this._children = children || [];
        return this;
    };

    Command.prototype.script = function (script) {
        if (arguments.length === 0) {
            return `cd ${this._root} && ` + shellJoin(this._script);
        }
        this._script = script || '';
        return this;
    };

    Command.prototype.root = function (root) {
        if (arguments.length === 0) { return this._root; }
        this._root = root;
        return this;
    };

    Command.prototype.toString = function () {
        return `[${this.directive}] <${this.target}> ` + this.script();
    };

    Command.parse = function (manifest, directive, target) {
        var matches, exp;

        if (target) {
            exp = new RegExp(target);
            matches = Object.keys(manifest).filter((target) => { return exp.test(target); });

            if (matches.length === 0) {
                throw new Error(`Target ${target} not found in manifest`);
            }

            return matches.map((target) => {
                return new Command(directive, target).script(manifest[target][directive]);
            });
        }
        else if (directive === 'all') {
            return [].concat.apply([], Command.ALL.map((directive) => {
                return Command.parse(manifest, directive, target);
            }));
        }

        return Object.keys(manifest).filter((target) => {
            return !!manifest[target][directive];
        }).map((target) => {
            return new Command(directive, target).script(manifest[target][directive]);
        });
    };

    function shellJoin (cmd) {
        return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
    }

    return Command;
} ());

module.exports = Command;
