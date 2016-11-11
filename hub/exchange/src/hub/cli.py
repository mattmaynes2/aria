import logging
from threading import Thread

logger=logging.getLogger(__name__)
formatter=logging.Formatter('%(asctime)s %(threadName)s %(name)-12s %(levelname)-8s %(message)s')

class CLI (Thread):
    LEVEL_EMERGENCY = logging.FATAL
    LEVEL_CRITICAL  = logging.CRITICAL
    LEVEL_ERROR     = logging.ERROR
    LEVEL_WARN      = logging.WARN
    LEVEL_INFO      = logging.INFO
    LEVEL_DEBUG     = logging.DEBUG
    PROMPT          = ''
    COMMANDS        = {
        'status'    : 'Returns the system status',
        'help'      : 'Print this message and exit',
        'exit'      : 'exit the main server'
    }

    def __init__ (self, listener, level = LEVEL_WARN, filename=None):
        super().__init__()
        logger.setLevel(level)
        ch = logging.StreamHandler()
        print('setting level to '+str(level))
        ch.setLevel(level)
        ch.setFormatter(formatter)
        # add to root logger
        logging.getLogger('').addHandler(ch)
        self.listener = listener
        self.running  = True
        
        if(filename):
            fh=logging.FileHandler(filename)
            # log everything to file
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            logging.getLogger('').addHandler(fh)

    def command (self):
        cmd = input(CLI.PROMPT)

        # TODO Add support for commands
        if cmd == 'help':
            self.help()
        elif cmd == 'exit':
            self.running = False
            self.listener.exit()
        elif cmd not in CLI.COMMANDS.keys():
            print('Unknown command ' + cmd + '. See help for details')
        else:
            print(self.listener.command(cmd))


    def log (self, msg, level = LEVEL_INFO):
        logger.log(level,msg)

    def help (self):
        print('Commands')
        for command in CLI.COMMANDS:
            print(command + '\t' + CLI.COMMANDS[command])


    def run (self):
        while (self.running):
            self.command()

