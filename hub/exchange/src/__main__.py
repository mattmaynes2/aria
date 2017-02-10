import sys
import logging
import logging.config
from pkg_resources import resource_stream
from pkg_resources import resource_filename
sys.path.append('../lib')

from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import AriaAdapter, HubAdapter, WemoAdapter, SoftwareAdapter
from adapter.zwave_adapter import ZWaveAdapter
from database import Database
from ipc import Message
from device     import SoftwareDeviceFactory
from hub.commands import GetDeviceEventsCommand,GetEventWindowCommand,GetBehavioursCommand,\
 CreateBehavioursCommand, CreateSessionCommand, ActivateSessionCommand, DeactivateSessionCommand
_log_config_file = 'configs/log.config'
_log_config_location = resource_filename(__name__, _log_config_file)

hub         = None
cli         = None
exchange    = None
database    = None

logging.config.fileConfig(_log_config_location, disable_existing_loggers=False)

def main ():
    global hub, cli, exchange
    argv = args.parse()
    if argv.daemonize:
        daemon.daemonize()

    database    = Database()
    hub         = Hub(argv, exit)
    cli         = CLI(hub)
    setupCommands(hub,database)
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
    #exchange.register('zwave'    , ZWaveAdapter())
    softwareAdapter = SoftwareAdapter()
    SoftwareDeviceFactory.setDeviceListener(softwareAdapter.add_device)
    exchange.register('software', softwareAdapter)
    
    # setup delegates
    exchange.addDelegate(ariaAdapter)

    return exchange

def exit ():
    global exchange
    exchange.teardown()

def setupCommands(hub,database):
    hub.addCommand(GetDeviceEventsCommand(database))
    hub.addCommand(GetEventWindowCommand(database))
    hub.addCommand(GetBehavioursCommand(database))
    hub.addCommand(CreateBehavioursCommand(database))
    hub.addCommand(CreateSessionCommand(database))
    hub.addCommand(ActivateSessionCommand(database))
    hub.addCommand(DeactivateSessionCommand(database))


if (__name__ == '__main__'):
    main()
