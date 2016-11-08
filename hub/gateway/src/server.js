var config          = require('../config.json'),
    ExchangeAdapter = require('./exchange-adapter'),
    Gateway         = require('./gateway'),
    logger         = require('winston');

var adapter, gateway;

logger.add(logger.transports.File, {filename: config.logfile, level:'debug'});

adapter = new ExchangeAdapter(config.endpoint);
gateway = new Gateway(adapter);

adapter.register().then(()=>{
        gateway.public = config.public;
        gateway.start(config.port);
        logger.info("Server running on port ", config.port);
    }, ()=>{
        logger.warn("Failed to register adapter")
    }
);


