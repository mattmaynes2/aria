import args

from exchange   import Exchange
from hub        import Hub

from adapter import AriaAdapter, HubAdapter

hub         = None
exchange    = None

def main ():
    global hub
    argv = args.parse()

    hub         = Hub(argv, exit)
    exchange    = create_exchange()
    exchange.start()


def create_exchange ():
    global exchange
    exchange = Exchange(hub)

    exchange.register('hub'     , HubAdapter(hub))
    exchange.register('aria'    , AriaAdapter())

    exchange.setup()
    return exchange

def exit ():
    global exchange
    exchange.teardown()

if (__name__ == '__main__'):
    main()
