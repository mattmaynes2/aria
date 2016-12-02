
class Parameter():

    def __init__(self,name,dataType,max_=None,min_=None,step=None):
        self.min = min_
        self.max= max_
        self.step=step
        if isinstance(dataType, DataType):
            self.dataType = dataType
        else:
            raise TypeError('Invalid DataType {}'.format(dataType))
        
    def __str__(self):
       return  "Parameter: [name: "+self.name+", DataType: "+str(self.dataType.value)+\
       ", min "+str(self.min)+", max: "+str(self.max)+", step: "+str(self.step)+"]"