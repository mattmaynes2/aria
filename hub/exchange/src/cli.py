from threading import Thread

class CLI (Thread):
    LEVEL_EMERGENCY = 'FATAL'
    LEVEL_ALERT     = 'ALERT'
    LEVEL_CRITICAL  = 'CRITICAL'
    LEVEL_ERROR     = 'ERROR'
    LEVEL_WARN      = 'WARN'
    LEVEL_NOTIFY    = 'NOTIFY'
    LEVEL_INFO      = 'INFO'
    LEVEL_DEBUG     = 'DEBUG'
    PROMPT          = ''
    COMMANDS        = {
        'status'    : 'Returns the system status',
        'help'      : 'Print this message and exit',
        'exit'      : 'exit the main server'
    }

    def __init__ (self, listener, level = LEVEL_WARN):
        super().__init__()
        self.level    = level
        self.listener = listener
        self.running  = True

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
        if (self.level >= level):
            print('[' + level + '] ' + msg + CLI.PROMPT)

    def help (self):
        print('Commands')
        for command in CLI.COMMANDS:
            print(command + '\t' + CLI.COMMANDS[command])


    def run (self):
        while (self.running):
            self.command()

