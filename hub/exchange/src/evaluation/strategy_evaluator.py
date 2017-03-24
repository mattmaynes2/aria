from brain.strategies import V2Strategy,  V3Strategy, V4Strategy
from database import Database,Retriever
from ipc import Message
from uuid import UUID
import sys

def main(argv):
    dbName="training.db"
    if len(argv) >= 1 :
        dbName= argv[0] 
    strategies =[V2Strategy, V3Strategy, V4Strategy
    #oracle=Oracle()
    database    = Database(dbName)
    for strategyType in strategies:
        runTraining(strategyType,database)

def runTraining(strategyType,database):
    # This line might be the cause of a bug may need a better way to initialize state
    retriever = Retriever(database)
    behaviours= database.execute("SELECT id, name from behaviour")
    for behaviour in behaviours:
        strategy=strategyType()
        print("running behaviour {}".format(behaviour['name']))
        sessions =  database.execute("SELECT id, name from session where behaviour_id = ?",[behaviour['id']])
        for session in sessions:
            print('running session {}'.format(session['name']))
            events=retriever.getSessionEvents(session['id'])
            strategy.processSession(events,buildState(database))
            evaluateDecisions(strategy,behaviour['id'])
        

def buildState(database):
    state = {}
    devices = database.execute("Select address, name, type from  device")
    for device in devices:
        attributes = database.execute("select id, name from attribute where device_type = ?",
        [device['type']])
        for attribute in attributes:
            attribute['parameters']= database.execute("select name, null as value from parameter\
             where attribute_id= ?", [attribute['id']])
        state[device['address']]={"attributes": attributes}
    return state

def evaluateDecisions(strategy,behaviourId):
    if isinstance(strategy, V4Strategy):
        decisions = buildDecisionsV4(strategy.eventMapping,behaviourId)
    else:
        decisions= {event,decisions for  event,decisions in strategy.eventMapping.items() 
        if len(decisions)>0}
    print(decisions)

def buildDecisionsV4(table,behaviourId):
    decisions ={}
    for event,row in table.items():
        if(row.behaviourCounts.get(behaviourId)):
            for decision in row.decisions:
                if(decision.behaviourId == behaviourId) :
                    bCount = row.behaviourCounts[decision.behaviourId]
                    ratio = decision.count/bCount
                    if ratio > 0.8 :
                       if(event in decisions):
                            decision[event].append(decision)
                        else:
                            decision[event]=[decision]
                        print("behaviour {} triggers {} to {} on {} "
                        .format(decision.behaviourId, decision.message.data, 
                         receiver, event))
    return decisions


if (__name__ == '__main__'):
    main(sys.argv[1:])
