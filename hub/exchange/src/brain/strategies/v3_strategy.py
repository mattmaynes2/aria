from uuid import UUID
from ipc import Message
from .v2_strategy import V2Strategy
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

    def getDecisionString(self, key, decisions):
        '''
        Returns a formatted string representation of a decision that is appropriate to store in a 
        file
        '''
        jsonMessageList = []
        for decision in decisions:
            jsonMessageList.append(Message.encode_to_json(decision))

        return jsonMessageList
    
    def decide(self, val):
        print(self.eventMapping)
        return super().decide(val)


    def load(self):
        decisionList = {}
        with open(self.saveFileName, 'r') as f:
            contents = f.read()
            outerList = json.loads(contents)
            for item in outerList:
                for key, val in item.items():
                    decisionList[key] = []
                    for decision in val:
                        d = Message.decode_from_json(decision)
                        decisionList[key].append(d)

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
