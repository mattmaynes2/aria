from brain.strategies import (V1Strategy, V2Strategy, V3Strategy,
                                     V4Strategy)


def main():
    strategies =[ V1Strategy(), V2Strategy(), V3Strategy(""), V4Strategy("")]
    decisionBroker = DecisionBroker(exchange,hub)


def runTraining():
    modelBuilder = ModelBuilder(Retriever(database),decisionBroker,strategy,hub.devices.values())

if (__name__ == '__main__'):
    main()
