from enum import Enum

class CommandType (Enum):
    CREATE = 'create'
    SET    = 'set'
    UPDATE = 'update'
    DELETE = 'delete'
    START  = 'start'
    STOP   = 'stop'
    GET    = 'get'