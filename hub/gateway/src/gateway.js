const dgram = require('dgram')

module.exports.gateway= function(expressApp){

    expressApp.get('/system/state', function(req, res) {
        res.send('Hello, World!\n')

        var client = dgram.createSocket('udp4')
        message = new Buffer('test')

        client.on('message', function(message, remote){
            console.log('Received message')
            client.close()
        })

        client.send(message, 0, message.length, 7600, 'localhost', function(err, bytes) {
            if (err) throw err
            console.log("Sent UDP message")
        })
    })
}


