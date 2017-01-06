import sys
import logging
import logging.config
from pkg_resources import resource_stream
sys.path.append('../lib')

from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import AriaAdapter, HubAdapter, WemoAdapter, SoftwareAdapter
from adapter.zwave_adapter import ZWaveAdapter
from database import Database
from ipc import Message
from device     import SoftwareDeviceFactory
_log_config_file = 'configs/log.config'
_log_config_location = resource_stream(__name__, _log_config_file)


hub         = None
cli         = None
exchange    = None
database    = None

logging.config.fileConfig(_log_config_location.name,disable_existing_loggers=False)

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
    #exchange.register('wemo'    , WemoAdapter())
    exchange.register('zwave'    , ZWaveAdapter())
    softwareAdapter = SoftwareAdapter()
    SoftwareDeviceFactory.setDeviceListener(softwareAdapter.add_device)
    exchange.register('software', softwareAdapter)
    
    # setup delegates
    exchange.addDelegate(ariaAdapter)

    return exchange

def exit ():
    global exchange
    exchange.teardown()

if (__name__ == '__main__'):
    main()
