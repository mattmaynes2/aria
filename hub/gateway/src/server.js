var fs              = require('fs'),
    ExchangeAdapter = require('./exchange-adapter'),
    Gateway         = require('./gateway'),
    logger          = require('winston');

var adapter, gateway, config, dirname;

var DEFAULT_CONFIG = {
    port        : 8080,
    public      : '../remote/',
    exchange    : {
        port      : '7600',
        address   : 'localhost'
    },
    logfile     : 'gateway.log'
};


try {
    dirname = /\/$/g.test(__dirname) ? process.cwd() + '/bin' : __dirname;
    config = JSON.parse(fs.readFileSync(dirname + '/../config.json'));
} catch (e) {
    console.log('Failed to load config file. Using defaults');
    config = DEFAULT_CONFIG;
}

// TODO add command line flag to switch to logging to stdout
logger.add(logger.transports.File, { filename: config.logfile, level: 'debug' });

adapter = new ExchangeAdapter(config.endpoint);
gateway = new Gateway(adapter);

adapter.register().then(() => {
        gateway.public = config.public;
        gateway.start(config.port);
        logger.info('Server running on port ', config.port);
    }, () => {
        logger.warn('Failed to register adapter');
    }
);


