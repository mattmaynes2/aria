var express = require('express'),
    app = express(),
    config = require('../config.json'),
    gateway = require('./gateway.js')

api = gateway.gateway(app)

app.listen(config.port)
