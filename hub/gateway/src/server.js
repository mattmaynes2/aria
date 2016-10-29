var config          = require('../config.json'),
    ExchangeAdapter = require('./exchange-adapter'),
    Gateway         = require('./gateway');

var adapter = new ExchangeAdapter(config.endpoint);

adapter.register();
new Gateway(adapter).start(config.port);

