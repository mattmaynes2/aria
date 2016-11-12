import sys
import logging
import logging.config
sys.path.append('../lib')

from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import AriaAdapter, HubAdapter, Message, WemoAdapter

hub         = None
cli         = None
exchange    = None

logging.config.fileConfig('log.config',disable_existing_loggers=False)

def main ():
    global hub, cli, exchange
    argv = args.parse()
    if argv.daemonize:
        daemon.daemonize()
    
    hub         = Hub(argv, exit)
    cli         = CLI(hub)
    exchange    = create_exchange(hub, cli)
    exchange.discovered(Device('hub', '', Message.DEFAULT_ADDRESS))

    cli.start()
    exchange.start()


def create_exchange (hub, cli):
    global exchange
    exchange = Exchange(hub, cli)

    exchange.register('hub'     , HubAdapter(hub))
    exchange.register('aria'    , AriaAdapter())
    exchange.register('wemo'    , WemoAdapter())
    return exchange

def exit ():
    global exchange
    exchange.teardown()

if (__name__ == '__main__'):
    main()
