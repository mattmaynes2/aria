import logging

log= logging.getLogger(__name__)
class DeviceType:

    def __init__(self, name, protocol, maker = '', isControllable= True ,attributes = []):
        self.name       = name
        self.protocol   = protocol
        self.maker      = maker
        self.isControllable = isControllable 
        self.attributes = attributes
    
    def __str__(self):
        return "DeviceType[name: "+self.name+", protocol: "+self.protocol+", maker: "+self.maker\
        +", isControllable: "+str(self.isControllable)+ ", Attributes: "+str(self.attributes)+"]"
    
    def getAttribute(self,attributeName):
        for attribute in self.attributes:
            if(attribute.name ==attributeName):
                return attribute
            log.warning('no attribute named '+attributeName+' found in deviceType '+self.name)
            return None