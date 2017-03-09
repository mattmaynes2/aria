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
        
    def addEvent(self,event):
        if event in self.table:
            row = self.table[event]
            row.count+=1
        else:
            row = self.table[event]=TableRow()

    def getDecision(self,eventString,threshold):
        """
        return a list of decisions if the number of times the event was seen
        divided by the number of times the event has been associated with the
        decision is greater than the threshold 
        """
        row=self.table.get(eventString,TableRow())
        return filter( lambda x: x.count/ row.count > threshold, row.decisions)

    def __str__(self):
        return str(self.__dict__)


class TableRow():
    def __init__(self):
         self.count=1
         self.decisions=[]
    
    def addDecision(self,decision):
        for d in self.decisions:
            if d == decision:
                logger.debug("found same existing decision")        
                d.count+=1
                logger.debug("incremented count count is now {}".format(d.count))
                return
        logger.debug("adding new decision")
        self.decisions.append(decision)

    def __str__(self):
        return str(self.__dict__)