from device import DataType
class Attribute:
    
    def __init__(self,name, dataType, parameters=[]):
        self.name=name
        self.parameters=parameters

    def __str__(self):
        return "Attribute [name: "+self.name+", parameters: "+str(self.parameters)+"]" 