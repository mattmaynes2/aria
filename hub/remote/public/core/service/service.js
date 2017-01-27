import io       from 'socket.io-client';
import Notify   from '../notify/notify';
import Response from './response';

var socket;

class Service {
    static get socket () {
        if (!socket) {
            socket = io();
            socket.on('reconnect', () => {
                Notify.success('Aria has successfully reconnected');
            });
            socket.on('disconnect', () => {
                Notify.error('Aria has been disconnected');
            });

        }
        return socket;
    }

    static get (endpoint, data) {
        return Service.send(data ? 'POST' : 'GET', endpoint, data || '');
    }

    static set (endpoint, data) {
        return Service.send('POST', endpoint, data);
    }

    static send (method, endpoint, data) {
        return new Promise((resolve, reject) => {
            var xhr = new XMLHttpRequest();

            xhr.onreadystatechange = () => {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        resolve(
                            new Response(xhr.responseText ? JSON.parse(xhr.responseText) : {}),
                            xhr.status
                        );
                    }
                    else if (xhr.status === 0) {
                        Notify.error('Aria is offline - Check connection and try again');
                        reject(new Response({}, xhr.status));
                    }
                    else {
                        reject(new Response(xhr.responseText, xhr.status));
                    }
                }
            };
            xhr.open(method, endpoint, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(typeof data === 'string' ? data : JSON.stringify(data));
        });

    }
}


export default Service;
