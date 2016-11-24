import io from 'socket.io-client';

var socket;

class Service {
    static get socket () {
        if (!socket) {
            socket = io();
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
                        resolve(xhr.responseText ? JSON.parse(xhr.responseText) : {});
                    }
                    else {
                        reject(xhr.responseText);
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
