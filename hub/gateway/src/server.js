let fs              = require('fs'),
    logger          = require('winston'),
    program         = require('commander'),
    TestAdapter     = require('./adapters/integration'),
    ExchangeAdapter = require('./adapters/exchange'),
    Gateway         = require('./gateway');

let DEFAULT_CONFIG = {
    port        : 8080,
    public      : '../remote/public/',
    exchange    : {
        port      : '7600',
        address   : 'localhost'
    },
    logfile     : 'gateway.log'
};

var adapter, gateway, config, dirname;

program
    .version('0.1.0')
    .arguments('[options ...]')
    .option('-c, --config', 'Path to configuration file [config.json]')
    .option('-l, --log-level [level]', 'Level of message logging to use')
    .option('-p, --port [port]', 'Port for gateway to serve client on')
    .option('-t, --test', 'Run the gateway with integration testing adapter');

program.parse(process.argv);

try {
    dirname = program.config || /\/$/g.test(__dirname) ? process.cwd() + '/bin' : __dirname;
    config = JSON.parse(fs.readFileSync(dirname + '/../config.json'));
} catch (e) {
    console.log('Failed to load config file. Using defaults');
    config = DEFAULT_CONFIG;
}

logger.configure({
    transports : [
        new (logger.transports.File) ({
            levels   : logger.config.syslog.levels,
            filename : config.logfile,
            level    : 'debug'
        }),
        new (logger.transports.Console) ({
            levels      : logger.config.syslog.levels,
            level       : program.logLevel || 'error',
            colorize    : true
        })
    ]
});

if (program.test) {
    adapter = new TestAdapter();
}
else {
    adapter = new ExchangeAdapter(config.endpoint);
}
gateway = new Gateway(adapter);

adapter.register().then(() => {
    var port = program.port || config.port;

    gateway.public = config.public;
    gateway.start(port);
    logger.info('Server running on port ', port);
}, () => {
    logger.warn('Failed to register adapter');
});


