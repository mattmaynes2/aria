var dgram = require('dgram')
var packets = require('./ccp')
var uuid = require('node-uuid')
var config = require('../config.json')

var senderId = new Buffer(16)
uuid.v4(null, senderId, 16)

var sendMessageToCommServer = function(type, payload){

    return new Promise(function(resolve, reject){
        var client = dgram.createSocket('udp4')

        var packet = {
            type: type,
            sender: senderId,
            destination: new Buffer(16).fill(0),
            payload: payload
        }

        message = packets.serialize(packet)

        var timeoutCallback = function() {
            client.close()
            reject(Error("Response wait period timed out"))
        }


        timeout = setTimeout(timeoutCallback, 5000)

        client.on('message', function(message, remote){
            console.log('Received response from comm server')
            client.close()
            clearTimeout(timeout)
            resolve(message)
        })


        client.send(message, 0, message.length, 7600, config.communicationServer, function(err, bytes) {
            if (err) {
                clearTimeout(timeout)
                reject(Error(err))
            }
            console.log("Sent UDP message")
        })
    })
}

var registerWithCommServer = function(){
    sendMessageToCommServer(1, {}).then(function(response){
        console.log('Got a response to discovery request')
        var parsed = packets.parse(response)

        if (parsed.type !== 4)
        {
            console.log('Communication server responded with an unexpected packet type', parsed)
        }

    }, function(err){
        console.log('Error in discovery request', err)
    })
}

module.exports.gateway= function(expressApp, transport){

    expressApp.get('/system/state', function(req, res) {
        sendMessageToCommServer(2, {'message': 'test'}).then(function(response){
            res.send(response)
        }, function(err){
            console.log("Error requesting system state from communication server", err)
        })
    })

    if (transport)
    {
        dgram = transport
    }

    registerWithCommServer()
}



