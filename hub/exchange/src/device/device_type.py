class DeviceType:

    def __init__(self, name, protocol, maker = '', isSensor= False ,attributes = []):
        self.name       = name
        self.protocol   = protocol
        self.maker      = maker
        self.isSensor     =isSensor 
        self.attributes = attributes
    
    def __str__(self):
        return "DeviceType[name: "+self.name+", protocol: "+self.protocol+", maker: "+self.maker\
        +", sensor: "+self.isSensor+ ", Attributes: "+str(self.attributes)"]"
        