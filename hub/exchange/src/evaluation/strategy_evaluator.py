from unittest.mock import Mock
from brain import DecisionBroker
from brain.model_builder import ModelBuilder
from brain.strategies import V1Strategy, V2Strategy, V3Strategy, V4Strategy
from .oracle import Oracle
from database import Database

def main():
    mockHub=Mock()
    
    strategies =[ V1Strategy(), V2Strategy(), V3Strategy(""), V4Strategy("")]
    oracle=Oracle()
    decisionBroker = DecisionBroker(oracle,mockHub)
    oracle.registerForEvents(decisionBroker)
    for strategy in strategies:
        mockHub.isNormalMode().return_value=False
        runTraining(decisionBroker,strategy)
        mockHub.isNormalMode().return_value=True
        runEvaluation(oracle)

def runTraining(decisionBroker,strategy):
    database    = Database("training.db")
    modelBuilder = ModelBuilder(Retriever(database),decisionBroker,strategy,hub.devices.values())

if (__name__ == '__main__'):
    main()
