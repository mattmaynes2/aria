
class Attribute:
    
    def __init__(name, dataType):
        self.name=name
        self.dataType= dataType

    def __str__(self):
        return "Attribute [name: "+self.name+", dataType: "+self.dataType+"]" 