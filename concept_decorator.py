from functools import wraps

def add1(a, b):
    return a + b

print(add1(1, 2))

def logged(f):
    print(f"adding logged to {f.__name__}")
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"you called {f.__name__}{args}{kwargs}")
        result = f(*args, **kwargs)
        print(f"it returned {result}")
        return result
    return wrapper

@logged
def add2(a, b):
    return a + b
print(add2(1, 2))

add3=logged(add1)
print(add3(1, 2))

def logged1(fmt):
    def log(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(fmt.format(fn=f, a=args, k=kwargs))
            result = f(*args, **kwargs)
            print(f"it returned {result}")
            return result
        return wrapper
    return log

@logged1("calling {fn.__name__}{a}{k}")
def add4(a, b):
    return a + b
print(add4(1, 2))

def log_methods(cls):
    for k, v in vars(cls).items():
        if callable(v):
            setattr(cls, k, logged(v))
    return cls

@log_methods
class Person:
    def full_name(self):
        return 'Maggie Simpson'

ms = Person()
print(ms.full_name())