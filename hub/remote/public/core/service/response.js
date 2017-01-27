class Response {
    constructor (payload, status) {
        this.payload    = payload === undefined ? ''  : payload;
        this.status     = status  === undefined ? 200 : status;
    }
}

export default Response;
