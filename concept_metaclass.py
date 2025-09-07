from functools import wraps

def logged(f):
    '''
    Logging decorator on a function
    '''
    print(f"adding logged to {f.__name__}")
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"you called {f.__name__}{args}{kwargs}")
        result = f(*args, **kwargs)
        print(f"it returned {result}")
        return result
    return wrapper

def log_methods(cls):
    '''
    Logging decorator on a class
    '''
    for k, v in vars(cls).items():
        if callable(v):
            setattr(cls, k, logged(v))
    return cls

class loggedtype(type):
    def __new__(meta, name, bases, methods):
        cls = super().__new__(meta, name, bases, methods)
        cls = log_methods(cls)
        return cls

class Person(metaclass=loggedtype):
    def full_name(self):
        return 'Maggie Simpson'

ms = Person()
print(ms.full_name())