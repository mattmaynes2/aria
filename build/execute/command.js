let ProcStat = require('./procstat');

let Command = (function () {

    function Command (directive, target) {
        this._children   = [];
        this._script     = '';
        this.directive  = directive || '';
        this.target     = target    || '';
        this.stat       = new ProcStat();
        this.root       = __dirname;
    }

    Command.prototype.addChild = function (cmd) {
        if (!(cmd instanceof Command)) {
            throw new TypeError('Invalid command type');
        }
        this._children.push(cmd);
        return this;
    };

    Command.prototype.children = function (children) {
        if (arguments.length === 0) {
            return this._children;
        }
        this._children = children || [];
        return this;
    };

    Command.prototype.script = function () {
        return `cd ${this.root} && ` + shellJoin(this.flatten().map((cmd) => {
            return cmd._script;
        }));
    };

    Command.prototype.map = function (iterator) {
        return this.flatten().map(iterator);
    };

    Command.prototype.flatten = function () {
        return [this].concat(this._children.map((child) => { return child.flatten(); }));
    };

    Command.prototype.toString = function () {
        return `${this.directive} ${this.target} ` + this.script();
    };

    Command.populate = function (manifest, command) {
        var target;

        if (command.target) {
            if (!(command.target in manifest)) {
                throw new Error(`Target ${command.target} not found in manifest`);
            }
            command._script = manifest[command.target][command.directive] || '';
        } else {
            for (target in manifest) {
                command.addChild(
                    Command.populate(
                        manifest,
                        new Command(command.directive, target)
                    )
                );
            }
        }
        return command;
    };

    function shellJoin (cmd) {
        return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
    }

    return Command;
} ());

module.exports = Command;
