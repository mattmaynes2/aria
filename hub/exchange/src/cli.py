import threading

class CLI (threading.Thread):
    COMMANDS = {
        'status'    : 'Returns the system status',
        'help'      : 'Print this message and exit',
        'exit'      : 'exit the main server'
    }

    def __init__ (self, listener):
        threading.Thread.__init__(self)
        self.listener = listener
        self.running = True

    def command (self):
        cmd = input('> ')

        # TODO Add support for commands
        if cmd == 'help':
            self.help()
        elif cmd == 'exit':
            self.running = False
            self.listener.exit()
        elif cmd not in CLI.COMMANDS.keys():
            print('Unknown command ' + cmd + '. See help for details')
        else:
            self.listener.command(cmd)

    def help (self):
        print('Commands')
        for command in CLI.COMMANDS:
            print(command + '\t' + CLI.COMMANDS[command])


    def run (self):
        while (self.running):
            self.command()

