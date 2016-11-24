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

class Notify {
    static info (text) {
        toastr.info(text);
    }
    static warn (text) {
        toastr.warn(text);
    }
    static success (text) {
        toastr.success(text);
    }
    static error (text) {
        toastr.error(text);
    }
}

export default Notify;
