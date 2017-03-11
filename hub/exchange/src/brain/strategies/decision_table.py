from .decision import Decision
import logging

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('Decisions.log')
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

class DecisionTable():
    def __init__(self):
        self.table={}

    def addDecision(self,event,decision):
        if event in self.table:
            row = self.table[event]
        else:
            row = self.table[event]=TableRow()

        logger.debug("adding decision {} event {}".format(decision.message,event))
        row.addDecision(decision)
        
    def addEvent(self,event,behaviourId):
        if event in self.table:
            row = self.table[event]
        else:
            row = self.table[event]=TableRow()
        row.incrementCount(behaviourId)

    def getDecision(self,eventString,threshold):
        """
        return a list of decisions if the number of times the event was seen
        divided by the number of times the event has been associated with the
        decision is greater than the threshold 
        """
        row=self.table.get(eventString,TableRow())
        return filter( lambda x: x.count/ row.getCount(x.behaviourId) > threshold, row.decisions)

    def removeBehaviour(self,behaviourId):
        for row in self.table.values():
            row.removeBehaviour(behaviourId)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        yield "table", {key:dict(val) for key,val in self.table.items()}

class TableRow():
    def __init__(self):
         self.behaviourCounts = {}
         self.decisions=[]
    
    def addDecision(self,decision):
        for d in self.decisions:
            if d == decision:
                logger.debug("found same existing decision")        
                d.count+=1
                logger.debug("incremented count now {}".format(d.count))
                return
        logger.debug("adding new decision")
        self.decisions.append(decision)

    def incrementCount(self,behaviourId):
        if( behaviourId in self.behaviourCounts):
            self.behaviourCounts[behaviourId]+=1
            logger.debug("Behaviour {} count now {}".format(behaviourId,
                self.behaviourCounts[behaviourId]))
        else:
            logger.debug("adding new behaviour count for id {}".format(behaviourId))
            self.behaviourCounts[behaviourId]=1

    def getCount(self,behaviourId):
        logger.debug("looking for behaviour {}".format(behaviourId))
        return self.behaviourCounts.get(behaviourId,None) 

    def removeBehaviour(self,behaviourId):
        logger.debug("deleting behaviour {}".format(behaviourId))
        self.behaviourCounts.pop(behaviourId,None)
        logger.debug("after pop counts are {}".format(self.behaviourCounts))
        self.decisions= [d for d in self.decisions if d.behaviourId != behaviourId]
        logger.debug("after delete decisions are {}".format([d.behaviourId for d in self.decisions]))
                
    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        yield 'decisions' , [dict(d) for d in self.decisions]
        yield 'behaviourCounts' , self.behaviourCounts
