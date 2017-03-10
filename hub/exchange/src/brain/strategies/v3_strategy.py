from uuid import UUID
from ipc import Message
from .v2_strategy import V2Strategy
from functools import partial
import json

import logging


logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('Decisions.log')
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

class V3Strategy(V2Strategy):

    def __init__(self, saveFileName):
        super().__init__()
        self.saveFileName = saveFileName
        self.load()

    def processSession(self, events,state):
        logger.debug("Processing data from a new session using v3")
        # remove events that don't change the state
        events = self.filterEvents(events,state)
        logger.debug('after filter events are: {}'.format(events))
        super().processSession(events)

    def filterEvents(self,events,state):
        return list(filter(partial(changedState,state),events))

    def findLastEventBefore(self, index, eventList):
        for event in reversed(eventList[:index]):
                logger.debug("Found a trigger event for the request")
                return event

    def getDecisionString(self, key, decisions):
        '''
        Returns a formatted string representation of a decision that is appropriate to store in a 
        file
        '''
        jsonMessageList = []
        for decision in decisions:
            jsonMessageList.append(Message.encode_to_json(decision))

        return jsonMessageList
    
    def load(self):
        decisionList = {}
        try:
            with open(self.saveFileName, 'r') as f:
                contents = f.read()
                outerList = json.loads(contents)
                for item in outerList:
                    for key, val in item.items():
                        decisionList[key] = []
                        for decision in val:
                                d = Message.decode_from_json(decision)
                                decisionList[key].append(d)
        except FileNotFoundError:
            logger.debug("No saved decisions found")
        except ValueError:
            logger.debug("Error decoding json")

        self.eventMapping = decisionList

    def save(self):
        '''
        Saves decisions to a file
        File Format:
        One decision per line, in the form 'key: jsonMessage'
        '''
        with open(self.saveFileName, 'w') as f:
            decisionArray = []
            for key, decisions in self.eventMapping.items():
                decisionArray.append({key: self.getDecisionString(key, decisions)})
        
            f.write(json.dumps(decisionArray, default=Message.json_encode))

def changedState(state,event):
    # need to keep all requests
    if(event['request_id']):
        return True
    device=event['source']
    attributeName=event['attribute_name']
    paramName=event['parameter_name']
    storedDevice=state.get(device,None)
    # if we have an event from a device we haven't seen before system state has changed
    if (not storedDevice):
        return True
    attributes = storedDevice['attributes']
    # check if the parameter changed
    parameters= next((x['parameters'] for x in attributes if x['name']== attributeName),[])
    for param in parameters:
        if param['name'] == paramName:
            if(param['value'] != event['value']):
                param['value'] = event['value']
                return True
            return False
    return True