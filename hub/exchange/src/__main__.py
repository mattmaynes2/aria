import sys

sys.path.append('../lib')

from hub        import Hub, Exchange, CLI, args
from device     import Device

from adapter import AriaAdapter, HubAdapter, Message

hub         = None
cli         = None
exchange    = None

def main ():
    global hub, cli, exchange
    argv = args.parse()

    hub         = Hub(argv, exit)
    cli         = CLI(hub)
    exchange    = create_exchange(hub, cli)
    exchange.discovered(Device('hub', '', Message.default))

    cli.start()
    exchange.start()

def create_exchange (hub, cli):
    global exchange
    exchange = Exchange(hub, cli)

    exchange.register('hub'     , HubAdapter(hub))
    exchange.register('aria'    , AriaAdapter())

    return exchange

def exit ():
    global exchange
    exchange.teardown()

if (__name__ == '__main__'):
    main()
