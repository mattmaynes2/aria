class DeviceType:

    def __init__(self, name, protocol, maker = '', isControllable= False ,attributes = []):
        self.name       = name
        self.protocol   = protocol
        self.maker      = maker
        self.isControllable = isControllable 
        self.attributes = attributes
    
    def __str__(self):
        return "DeviceType[name: "+self.name+", protocol: "+self.protocol+", maker: "+self.maker\
        +", isControllable: "+str(self.isControllable)+ ", Attributes: "+str(self.attributes)+"]"
        