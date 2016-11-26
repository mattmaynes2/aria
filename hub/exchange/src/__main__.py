import sys
import logging
import logging.config
sys.path.append('../lib')

from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import AriaAdapter, HubAdapter, WemoAdapter
from database import Database
from ipc import Message

hub         = None
cli         = None
exchange    = None
database    = None

logging.config.fileConfig('log.config',disable_existing_loggers=False)

def main ():
    global hub, cli, exchange
    argv = args.parse()
    if argv.daemonize:
        daemon.daemonize()

    database    = Database()
    hub         = Hub(database,argv, exit)
    cli         = CLI(hub)
    exchange    = create_exchange(hub, cli, database)
    exchange.discovered(hub)

    cli.start()
    exchange.start()


def create_exchange (hub, cli, database):
    global exchange
    exchange = Exchange(hub, cli, database)
    ariaAdapter=AriaAdapter()
    
    # setup adapters
    exchange.register('hub'     , HubAdapter(hub))
    exchange.register('aria'    , ariaAdapter)
    exchange.register('wemo'    , WemoAdapter())

    # setup delegates
    exchange.addDelegate(ariaAdapter)

    return exchange

def exit ():
    global exchange
    exchange.teardown()

if (__name__ == '__main__'):
    main()
