
class Decision():
    def __init__(self,behaviourId,message):
        self.behaviourId=behaviourId
        self.message=message
        self.count=1

    def __eq__ (self, other):
        return  self.behaviourId  ==  other.behaviourId and \
                self.message      ==  other.message
    
    def __str__(self):
        return str(self.__dict__)

    