var fs              = require('fs'),
    ExchangeAdapter = require('./exchange-adapter'),
    Gateway         = require('./gateway');

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

adapter = new ExchangeAdapter(config.endpoint);
gateway = new Gateway(adapter);

adapter.register().then(()=>{
        gateway.public = config.public;
        gateway.start(config.port);
    }, ()=>{
        console.log('Failed to register adapter');
    }
);


