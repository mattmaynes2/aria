def synchronized(lock):
    def decorator(function):
        def wrapper(*args, **kwargs):
            with lock:
                return function(*args, **kwargs)
        return wrapper
    return decorator