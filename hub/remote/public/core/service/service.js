import io       from 'socket.io-client';
import Notify   from '../notify/notify';
import Response from './response';

var socket, Request;

class Service {
    static get Request ()       { return Request ? Request : XMLHttpRequest;   }
    static set Request (req)    { Request = req;    }
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

    static delete (endpoint, data) {
        return Service.send('DELETE', endpoint, data);
    }

    static send (method, endpoint, data) {
        data = data || '';
        return new Promise((resolve, reject) => {
            var req = new Service.Request();

            req.onreadystatechange = () => {
                var res;

                if (req.readyState === 4) {
                    try {
                        res = JSON.parse(req.responseText);
                    } catch (e) {
                        res = req.responseText || '';
                    }

                    if (req.status === 200) {
                        resolve(
                            new Response(res),
                            req.status
                        );
                    }
                    else if (req.status === 0) {
                        Notify.error('Aria is offline - Check connection and try again');
                        reject(new Response(res, req.status));
                    }
                    else {
                        if (res.error) {
                            Notify.error('Request Failed: ' + res.error);
                        }
                        reject(new Response(res, req.status));
                    }
                }
            };
            req.open(method, endpoint, true);
            req.setRequestHeader('Content-Type', 'application/json');
            req.send(typeof data === 'string' ? data : JSON.stringify(data));
        });

    }
}


export default Service;
