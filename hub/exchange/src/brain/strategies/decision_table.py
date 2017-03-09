from .decision import Decision

class DecisionTable():
    def __init__(self):
        self.table={}

    def addDecision(self,event,decision):
        if event in self.table:
            row = self.table[event]
        else:
            row = self.table[event]=TableRow()
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
        return filter( lambda x: row.count/ x.count > threshold, row.decisions)


class TableRow():
    def __init__(self):
         self.count=1
         self.decisions=[]
    
    def addDecision(self,decision):
        for d in self.decisions:
            if d == decision:
                d.count+=1
                return
        self.decisions.append(decision)