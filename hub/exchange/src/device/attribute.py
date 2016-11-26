from device import DataType
class Attribute:
    
    def __init__(self,name, dataType, min_=None, max_=None, step= None):
        self.name=name
        if isinstance(dataType, DataType):
            self.dataType = dataType
        else:
            raise TypeError('Invalid DataType {}'.format(dataType))
        self.min = min_
        self.max= max_
        self.step=step

    def __str__(self):
        return "Attribute [name: "+self.name+", dataType: "+str(self.dataType.value)+", min "+str(self.min)\
        +", max: "+str(self.max)+", step: "+str(self.step)+"]" 