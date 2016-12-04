from device import DataType
from .parameter import Parameter

class Attribute:
    
    def __init__(self,name, parameters=[], isControllable=True):
        self.name=name
        self.parameters=parameters
        self.isControllable=isControllable

    def __str__(self):
        return "Attribute [name: "+self.name+", parameters: "+str(self.parameters)+"]"

    @property
    def parameters(self):
        return self._parameters
    
    @parameters.setter
    def parameters(self,value):
        if( not isinstance(value,list)):
            raise TypeError('Parameters must be a list of Parameters')
        self._parameters=value

    def addParameter(self,param):
        if(not isinstance(param, Parameter)):
            raise TypeError('{} not a valid Parameter'.format(param))
        self._parameters.append(param) 
