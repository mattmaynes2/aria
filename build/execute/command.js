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

    Command.parse = function (manifest, directive, target, all) {
        var matches, exp;

        manifest = dealias(manifest, directive);
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
                return Command.parse(manifest, directive, target, true);
            }));
        }

        return Object.keys(manifest).filter((target) => {
            return !!manifest[target][directive] &&
                !(all && /ignore/.test(manifest[target].all));
        }).map((target) => {
            return new Command(directive, target).script(manifest[target][directive]);
        });
    };

    function shellJoin (cmd) {
        return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
    }

    function dealias (manifest, directive) {
        Object.keys(manifest).map((target) => {
            var res, cmd = manifest[target][directive];
            cmd = 'string' === typeof cmd ? [cmd] : cmd;

            if (cmd) {
                res = cmd.map((x) => {
                    return /^self\./.test(x) ? manifest[target][x.slice(5)] : x;
                });
                manifest[target][directive] = [].concat.apply([], res);
            }

        });
        return manifest;
    }

    return Command;
} ());

module.exports = Command;
