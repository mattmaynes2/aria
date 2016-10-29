var config          = require('../config.json'),
    ExchangeAdapter = require('./exchange-adapter'),
    Gateway         = require('./gateway');

var adapter, gateway;

adapter = new ExchangeAdapter(config.endpoint);
gateway = new Gateway(adapter);

adapter.register();

gateway.public = config.public;
gateway.start(config.port);

