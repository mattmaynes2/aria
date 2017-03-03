import sys
import os
import signal
import logging
import logging.config
from pkg_resources import resource_stream
from pkg_resources import resource_filename
sys.path.append('../lib')

from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import AriaAdapter, HubAdapter, WemoAdapter, SoftwareAdapter
from adapter.sonos_adapter import SonosAdapter
from database import Database, Retriever
from ipc import Message
from device     import SoftwareDeviceFactory
from hub.commands import GetDeviceEventsCommand,GetEventWindowCommand,GetBehavioursCommand,\
 CreateBehavioursCommand, CreateSessionCommand, ActivateSessionCommand, DeactivateSessionCommand
from brain.model_builder import ModelBuilder
from brain.decision_broker import DecisionBroker
from brain.strategies import V2Strategy


_log_config_file = 'configs/log.config'
_log_config_location = resource_filename(__name__, _log_config_file)

hub         = None
cli         = None
exchange    = None
database    = None

logging.config.fileConfig(_log_config_location, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def main ():
    global hub, cli, exchange
    argv = args.parse()
    if argv.daemonize:
        daemon.daemonize()
        
    pid = os.getpid()
    signal.signal(signal.SIGTERM, signalHandler)

    database    = Database()
    hub         = Hub(argv, exit)
    cli         = CLI(hub)
    setupCommands(hub,database)
    exchange    = create_exchange(hub, cli, database)
    exchange.discovered(hub)

    cli.start()
    exchange.start()

def signalHandler(signum, frame):
    exit()
    sys.stdout.write('Initiating graceful shutdown')
    sys.exit(0)

def create_exchange (hub, cli, database):
    global exchange
    exchange = Exchange(hub, cli, database)
    ariaAdapter=AriaAdapter()
    
    # setup adapters
    exchange.register('hub'     , HubAdapter(hub))
    exchange.register('aria'    , ariaAdapter)
    exchange.register('sonos'   , SonosAdapter())
    #exchange.register('wemo'    , WemoAdapter())

    try:
        from adapter.zwave_adapter import ZWaveAdapter
        exchange.register('zwave'    , ZWaveAdapter())
    except:
        logger.warn("Unable to load Zwave adapter")

    softwareAdapter = SoftwareAdapter()
    SoftwareDeviceFactory.setDeviceListener(softwareAdapter.add_device)
    exchange.register('software', softwareAdapter)
    
    # setup  Machine learning
    #TODO add past events to strategy
    strategy = V2Strategy()
    decisionBroker = DecisionBroker(exchange,hub)
    modelBuilder = ModelBuilder(Retriever(database),decisionBroker,strategy)

    # setup delegates
    exchange.addDelegate(ariaAdapter)
    exchange.addDelegate(decisionBroker)
    exchange.addDelegate(modelBuilder)

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
    hub.addCommand(DeactivateSessionCommand())


if (__name__ == '__main__'):
    main()
