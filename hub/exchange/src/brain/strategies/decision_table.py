from .decision import Decision

class DecisionTable():
    
    def __init__(self):
        self.table={}

    def addDecision(self,event,decision):
        if event in table:
            row =table[event]
        else:
            row = table[event]=TableRow()
        row.addDecision(decision)
        
    def addEvent(self,event):
       if event in table:
            row =table[event]
            row.count+=1
        else:
            row = table[event]=TableRow()

    def getDecision(self,eventString,threshold):
        return filter( lambda x: x.count/ x.decision.count > threshold,self.get(eventString,[]))


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