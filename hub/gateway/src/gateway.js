const dgram = require('dgram')
const packets = require('./ccp')
const uuid = require('node-uuid')

module.exports.gateway= function(expressApp){

    expressApp.get('/system/state', function(req, res) {

        var client = dgram.createSocket('udp4')

        var senderBuffer = new Buffer(16)
        uuid.v4(null, senderBuffer, 16)

        var packet = {
            type: 1,
            sender: senderBuffer,
            destination: new Buffer(16).fill(0),
            payload: {'message' : 'test'}
        }

        message = packets.serialize(packet)

        client.on('message', function(message, remote){
            console.log('received message')
            client.close()

            response = packets.parse(message)
            res.send(JSON.stringify({
                'version' : response.version
            }))
        })

        var timeoutCallback = function() {
            client.close()
            res.status = 500
            res.end()
            console.log("CCP udp status request timed out")
        }

        setTimeout(timeoutCallback, 5000)

        client.send(message, 0, message.length, 7600, 'localhost', function(err, bytes) {
            if (err) throw err
            console.log("Sent UDP message")
        })
    })
}


