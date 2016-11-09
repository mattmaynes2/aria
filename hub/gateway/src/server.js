var fs              = require('fs'),
    ExchangeAdapter = require('./exchange-adapter'),
    Gateway         = require('./gateway'),
    logger          = require('winston');

var adapter, gateway, config;

var DEFAULT_CONFIG = {
    port      : 8080,
    public    : '../remote/',
    exchange  : {
        port      : '7600',
        address   : 'localhost'
    }
};


try {
    config = JSON.parse(fs.readFileSync(__dirname + '../config.json'));
} catch (e) {
    console.log('Failed to load config file. Using defaults');
    config = DEFAULT_CONFIG;
}

logger.add(logger.transports.File, {filename: config.logfile, level:'debug'});

adapter = new ExchangeAdapter(config.endpoint);
gateway = new Gateway(adapter);

adapter.register().then(()=>{
        gateway.public = config.public;
        gateway.start(config.port);
        logger.info('Server running on port ', config.port);
    }, () => {
        logger.warn('Failed to register adapter');
    }
);


