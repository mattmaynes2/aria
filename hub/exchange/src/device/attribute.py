
class Attribute:
    
    def __init__(name, dataType, min_=None, max_=None, step= None):
        self.name=name
        self.dataType= dataType
        self.min = min_
        self.max= max_
        self.step=step

    def __str__(self):
        return "Attribute [name: "+self.name+", dataType: "+self.dataType+", min "+self.min\
        +", max: "+self.max+", step: "+self.step+"]" 