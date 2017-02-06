from enum import Enum

class CommandType (Enum):
    CREATE      = 'create'
    SET         = 'set'
    UPDATE      = 'update'
    DELETE      = 'delete'
    ACTIVATE    = 'activate'
    DEACTIVATE  = 'deactivate'
    GET         = 'get'