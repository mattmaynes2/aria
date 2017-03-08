from uuid import UUID
from ipc import Message
from .v3_strategy import V3Strategy
from .decision import Decision
from functools import partial
from .decision_table import DecisionTable
import json

import logging


logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('Decisions.log')
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

class V3Strategy(V3Strategy):

    def __init__(self,saveFileName):
        super().__init__(saveFileName)
        self.eventMapping=DecisionTable()
        self.threshHold=0.8
        self.windowSize=6

    def addDecision(self, triggeringEvent, action):
        triggerString = self.buildEventIdentifierFromDatabaseObject(triggeringEvent)
        logger.debug("Adding decision for trigger string " + triggerString)
        logger.debug("The action taken will be " + str(action))
        self.eventMappings.addDecision(triggeringEvent,\
        Decision(triggeringEvent['behaviour_id'],action))

    def getDecision(self,eventString):
       return self.eventMapping.getDecision(eventString, self.threshold)

    def processSession(self, events,state):
        events[:] = self.filterEvents(events,state)
        for i, event in enumerate(events):
            self.eventMapping.addEvent(event)
            if event['request_id']:
                logger.debug("Found a request made during the session")
                message=self.buildMessageFromEvent(event)
                for e in events[ i-windowSize if i-windowSize>0 : 0 : i] :
                    self.addDecision(e,message)

