from brain.strategies import V2Strategy,  V3Strategy, V4Strategy
from database import Database,Retriever
from ipc import Message
from uuid import UUID
import sys

def main(argv):
    dbName="training.db"
    if len(argv) >= 1 :
        dbName= argv[0] 
    strategies =[V2Strategy, V3Strategy, V4Strategy]
    #oracle=Oracle()
    database    = Database(dbName)
    evaluator=Evaluator(database)
    for strategyType in strategies:
        print("--------------------------------------------------------------")
        print("Running Evaluation for {}".format(strategyType.__name__))
        evaluator.runTraining(strategyType)
        print("--------------------------------------------------------------")

class Evaluator():
    def __init__(self,database):
        self.database=database
    def runTraining(self,strategyType):
        # This line might be the cause of a bug may need a better way to initialize state
        retriever = Retriever(self.database)
        behaviours= self.database.execute("SELECT id, name from behaviour")
        for behaviour in behaviours:
            strategy=strategyType()
            print("")
            print("running behaviour {}".format(behaviour['name']))
            sessions =  self.database.execute("SELECT id, name from session where behaviour_id = ?",[behaviour['id']])
            for session in sessions:
                print('running session {}'.format(session['name']))
                events=retriever.getSessionEvents(session['id'])
                print("There are {} events in this session".format(len(events)))
                strategy.processSession(events,self.buildState())
                self.evaluateDecisions(strategy,behaviour['id'])
            

    def buildState(self):
        state = {}
        devices = self.database.execute("Select address, name, type from  device")
        for device in devices:
            attributes = self.database.execute("select id, name from attribute where device_type = ?",
            [device['type']])
            for attribute in attributes:
                attribute['parameters']= self.database.execute("select name, null as value from parameter\
                where attribute_id= ?", [attribute['id']])
            state[device['address']]={"attributes": attributes}
        return state

    def evaluateDecisions(self,strategy,behaviourId):
        if isinstance(strategy, V4Strategy):
            decisions = self.buildDecisionsV4(strategy.eventMapping,behaviourId)
        else:
            decisions= {event: [self.parseMessage(d) for d in decisions] for event, 
            decisions in strategy.eventMapping.items() 
            if len(decisions)>0}
        for event,decisions in decisions.items():
            print("\tEvent {}".format(self.parseEvent(event)))
            for d in decisions:
                print("\t\t{}".format(d))
            print("")
        

    def parseEvent(self,event):
        name = self.database.execute("select name from device where address = ?",
        [event[0:36]])[0]['name']

        return name +" "+ event[36:]

    def buildDecisionsV4(self,table, behaviourId):
        decisions = {}
        for event, row in table.table.items():
            if(row.behaviourCounts.get(behaviourId)):
                for decision in row.decisions:
                    if(decision.behaviourId == behaviourId):
                        bCount = row.behaviourCounts[decision.behaviourId]
                        ratio = decision.count / bCount
                        if ratio > 0.8:
                            if(event in decisions):
                                decisions[event].append(self.parseMessage(decision.message))
                            else:
                                decisions[event] = [self.parseMessage(decision.message)]
        return decisions

    def parseMessage(self,message):
        receiver = UUID(bytes=message.receiver)
        name=self.database.execute("select name from device where address = ?",[str(receiver)])[0]['name']
        paramName=message.data['value'][0]['name']
        value=message.data['value'][0]['value']
        return "set {}'s {} to {} ".format(name,paramName,value)


if (__name__ == '__main__'):
    main(sys.argv[1:])
