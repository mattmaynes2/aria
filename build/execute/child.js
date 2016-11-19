let spawn   = require('child_process').spawn,
    Command = require('./command');

let Child = (function () {

    function Child (command, options) {
        this.command    = command || new Command();
        this.options    = options || {};
        this._child     = null;
    }

    Child.prototype.run = function () {
        return new Promise((resolve, reject) => {
            try {
                this.command.stat.start();
                this._child = spawn(this.command.script(), [], { shell : true });

                if (!this.options.quiet) {
                    this._child.stdout.on('data', (data) => { process.stdout.write(data); });
                    this._child.stderr.on('data', (data) => { process.stderr.write(data); });
                }

                this._child.on('close', (code) => {
                    this.command.stat.stop();
                    if (code !== 0 ) {
                        reject(`Process terminated with code ${code}`);
                    } else {
                       resolve();
                    }
                });
            } catch (e) {
                reject(e);
           }
        });
    };

    return Child;

} ());

module.exports = Child;
