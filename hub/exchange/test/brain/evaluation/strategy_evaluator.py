from unittest.mock import Mock
from brain import DecisionBroker
from brain.model_builder import ModelBuilder
from brain.strategies import V1Strategy, V2Strategy, V3Strategy, V4Strategy
from oracle import Oracle
from database import Database
from ipc import Message

def main():
    mockHub=Mock()
    
    strategies =[ V1Strategy(), V2Strategy(), V3Strategy(""), V4Strategy("")]
    oracle=Oracle()
    decisionBroker = DecisionBroker(oracle,mockHub)
    oracle.registerForEvents(decisionBroker)
    database    = Database("training.db")
    for strategy in strategies:
        mockHub.isNormalMode().return_value=False
        runTraining(decisionBroker,strategy,database)
        mockHub.isNormalMode().return_value=True
        runEvaluation(oracle)

def runTraining(decisionBroker,strategy,database):
    # This line might be the cause of a bug may need a better way to initialize state
    modelBuilder = ModelBuilder(Retriever(database),decisionBroker,strategy,{})
    sessions= database.execute("SELECT id from session")
    for session in sessions:
        message=Message()
        message.data={"activate":"session", "id":session}
        modelBuilder.received(message)
        message.data={"deactivate":"session", "id":session}
        
        

def runEvaluation(oracle):
    pass

if (__name__ == '__main__'):
    main()
