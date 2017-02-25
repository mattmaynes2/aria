import logging
from .data_types import DataType
from enum import Enum

log = logging.getLogger(__name__)

class Parameter():

    def __init__(self,name,dataType,max_=None,min_=None,step=None,value=None,enum=None):
        self.name=name
        self.min = min_
        self.max= max_
        self.step=step
        self.value=value
        self._dataType=dataType
        self.enum=enum
        if(self.dataType == DataType.Enum and not enum):
            log.warning("Using enum without a list of possible values may not "\
                        +"display properly in the UI")
       
        
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
    
    def isValidValue(self,value):
        if self.max and self.min :
            return self.min< value and self.max> value
        return True 

    def __iter__(self):
        for key,val in vars(self).items():
            if isinstance(val,Enum) :
                yield key, val.value
            else:
                yield key,val 