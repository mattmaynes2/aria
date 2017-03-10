from uuid import UUID
from ipc import Message
from .v3_strategy import V3Strategy
from .decision import Decision
from functools import partial
from .decision_table import DecisionTable
import json
import pickle

import logging


logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('Decisions.log')
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

class V4Strategy(V3Strategy):

    def __init__(self,saveFileName):
        super().__init__(saveFileName)
        self.eventMapping=DecisionTable()
        # using a threshold of 80% to determine if a decision is should be triggered on an event
        # this is calculated as decision_count / event_count > threshold
        self.threshold=0.8
        # the window is the number of events each decision is
        self.windowSize=6

    def addDecision(self, triggeringEvent, action):
        triggerString = self.buildEventIdentifierFromDatabaseObject(triggeringEvent)
        self.eventMapping.addDecision(triggerString,\
        Decision(triggeringEvent['behaviour_id'],action))

    def getDecision(self,eventString):
       return [d.message for d in self.eventMapping.getDecision(eventString, self.threshold)]

    def processSession(self, events,state):
        events = self.filterEvents(events,state)
        logger.debug('filtered events are {}'.format(events))
        for i, event in enumerate(events):
            eventString = self.buildEventIdentifierFromDatabaseObject(event)
            self.eventMapping.addEvent(eventString,event['behaviour_id'])
            if event['request_id']:
                logger.debug("Found a request made during the session")
                message=self.buildMessageFromEvent(event)
                for e in events[ max(0,i-self.windowSize) : i] :
                    self.addDecision(e,message)
        logger.debug("done processing session current table is {}".format(dict(self.eventMapping)))
    
    def save(self):
        '''
        Saves decisions to a file
        '''
        with open(self.saveFileName, 'wb') as f:
            pickle.dump(self.eventMapping, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        '''
        Saves decisions to a file
        '''
        try:
            with open(self.saveFileName, 'rb') as f:
                self.eventMapping=pickle.load(f)
        except FileNotFoundError:
            logger.info("Couldn't find {} not loading any decisions".format(self.saveFileName))
