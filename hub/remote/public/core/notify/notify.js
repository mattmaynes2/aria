import toastr from 'toastr';

toastr.options = {
  'closeButton'       : true,
  'debug'             : false,
  'newestOnTop'       : false,
  'progressBar'       : false,
  'positionClass'     : 'toast-top-right',
  'preventDuplicates' : false,
  'onclick'           : null,
  'showDuration'      : '300',
  'hideDuration'      : '1000',
  'timeOut'           : '5000',
  'extendedTimeOut'   : '1000',
  'showEasing'        : 'swing',
  'hideEasing'        : 'linear',
  'showMethod'        : 'fadeIn',
  'hideMethod'        : 'fadeOut'
};

var history = [];

class Notify {
    static get history () {
        return history;
    }
    static reset () {
        history = [];
    }
    static info (text) {
        history.push({ type : 'info', text : text });
        toastr.info(text);
    }
    static warn (text) {
        history.push({ type : 'warn', text : text});
        toastr.warning(text);
    }
    static success (text) {
        history.push({ type : 'success', text : text });
        toastr.success(text);
    }
    static error (text) {
        history.push({ type : 'error', text : text});
        toastr.error(text);
    }
}

export default Notify;
