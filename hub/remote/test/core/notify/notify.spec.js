import Notify from '../../../public/core/notify/notify';

describe('Notify', function () {
    afterEach(function () {
        Notify.reset();
    });

    it('Displays an info notification', function () {
        Notify.info('Info');
        expect(Notify.history[0]).toEqual({ text : 'Info', type : 'info' });
    });

    it('Displays a warn notification', function () {
        Notify.warn('Warn');
        expect(Notify.history[0]).toEqual({ text : 'Warn', type : 'warn' });
    });

    it('Displays a success notification', function () {
        Notify.success('Success');
        expect(Notify.history[0]).toEqual({ text : 'Success', type : 'success' });
    });

    it('Displays an error notification', function () {
        Notify.error('Error');
        expect(Notify.history[0]).toEqual({ text : 'Error', type : 'error' });
    });

    it('Adds multiple events to the notification history', function () {
        Notify.warn('Warn');
        Notify.error('Error');
        expect(Notify.history).toEqual([
            { type : 'warn'     , text : 'Warn'  },
            { type : 'error'    , text : 'Error' }
        ]);
    });
});

