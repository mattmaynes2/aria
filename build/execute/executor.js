let columnify   = require('./columnify'),
    Child       = require('./child');


let Executor = (function () {

    function Executor (commands, options) {
        this.commands   = commands || [];
        this.options    = options || {};
    }

    Executor.prototype.run = function () {
        let children = this.commands.map((cmd) => {
            return new Child(cmd, this.options);
        });
        exec(this.options, children).then(() => {
            if (this.options.stats) {
                console.log(columnify(this.commands.map((cmd) => {
                    return cmd.stat.data();
                })));
            }
        });

    };

    function exec (options, children, resolve) {
        let child   = children[0],
            msg     = `Executing '${child.command.directive}' on target '${child.command.target}'`;

        if (!options.silent) {
            console.log(msg);
        }
        if (options.verbose) {
            console.log('Executing ' + child.command);
        }

        child.run()
            .then(() => {
                if (children.length > 1) {
                    exec(options, children.slice(1), resolve);
                }
                else {
                    resolve();
                }
            })
            .catch((e) => {
                console.error(msg + ' failed');
                console.error(e);

                if (!options.stayAlive) {
                    process.exit(1);
                }
            });

        return resolve ? Promise.resolve() : new Promise((res) => { resolve = res; });
    }

    return Executor;

} ());

module.exports = Executor;

