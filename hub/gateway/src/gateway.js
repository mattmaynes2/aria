var express = require('express'),
app = express()//,
//config = require('../config.json')

app.get('/system/state', function(req, res) {
    res.send('Hello, World!\n')
})

//app.listen(config.port)
