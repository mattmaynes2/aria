const dgram = require('dgram')
const packets = require('./ccp')
const uuid = require('node-uuid')
const config = require('../config.json')

var senderId = new Buffer(16)
uuid.v4(null, senderId, 16)

var registerWithCommServer = function(){
    sendMessageToCommServer(1, {}, function(message){
    })
}

var sendMessageToCommServer = function(type, payload, responseCallback){
    var client = dgram.createSocket('udp4')

    var packet = {
        type: type,
        sender: senderId,
        destination: new Buffer(16).fill(0),
        payload: payload
    }

    message = packets.serialize(packet)

    client.on('message', function(message, remote){
        console.log('Received response from comm server')
        client.close()

        responseCallback(message)
    })

    var timeoutCallback = function() {
        client.close()
        responseCallback('')
        console.log("CCP udp status request timed out")
    }

    setTimeout(timeoutCallback, 5000)

    client.send(message, 0, message.length, 7600, config.communicationServer, function(err, bytes) {
        if (err) throw err
        console.log("Sent UDP message")
    })
}

module.exports.gateway= function(expressApp){

    expressApp.get('/system/state', function(req, res) {

        sendMessageToCommServer(2, {'message': 'test'}, function(response){
            res.send(response)
        })
    })

    registerWithCommServer()
}



