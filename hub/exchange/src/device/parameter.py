from .data_types import DataType
class Parameter():

    def __init__(self,name,dataType,max_=None,min_=None,step=None,value=None):
        self.name=name
        self.min = min_
        self.max= max_
        self.step=step
        self.value=value
        self._dataType=dataType
       
        
    def __str__(self):
       return  "Parameter: [name: "+str(self.name)+", DataType: "+str(self.dataType.value)+\
       ", value: "+str(self.value)+", min "+str(self.min)+", max: "+str(self.max)+", step: "\
       +str(self.step)+"]"

    @property
    def dataType(self):
        return self._dataType

    @dataType.setter
    def dataType(self,value):
         if isinstance(dataType, DataType):
            self._dataType = dataType
         else:
            raise TypeError('Invalid DataType {}'.format(dataType))