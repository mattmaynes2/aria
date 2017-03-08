
class Decision():
    def __init__(self,behaviourId,message):
        self.behaviourId=behaviourId
        self.message=message
        self.count=1

    def increaseCount(self):
        self.count+=1
    