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

class V4Strategy(V3Strategy):

    def __init__(self,saveFileName):
        super().__init__(saveFileName)
        self.eventMapping=DecisionTable()
        self.threshold=0.8
        self.windowSize=6

    def addDecision(self, triggeringEvent, action):
        triggerString = self.buildEventIdentifierFromDatabaseObject(triggeringEvent)
        self.eventMapping.addDecision(triggerString,\
        Decision(triggeringEvent['behaviour_id'],action))

    def getDecision(self,eventString):
       return [d.message for d in self.eventMapping.getDecision(eventString, self.threshold)]

    def processSession(self, events,state):
        events[:] = self.filterEvents(events,state)
        logger.debug('filtered events are {}'.format(events))
        for i, event in enumerate(events):
            eventString = self.buildEventIdentifierFromDatabaseObject(event)
            self.eventMapping.addEvent(eventString)
            if event['request_id']:
                logger.debug("Found a request made during the session")
                message=self.buildMessageFromEvent(event)
                for e in events[ i-self.windowSize if i-self.windowSize>0 else 0 : i] :
                    self.addDecision(e,message)

