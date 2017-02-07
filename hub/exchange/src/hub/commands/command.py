from .command_type import CommandType
class Command:
    def __init__(self,commandType,name):
        self.name=name
        self.commandType=commandType
    
    @property
    def commandType(self):
        return self.__commandType

    @commandType.setter
    def commandType(self, value):
        if(not isinstance(value,CommandType)):
            raise TypeError('Invalid CommandType {}'.format(value))
        self.__commandType=value

    def execute(hub,params=None):
        pass
