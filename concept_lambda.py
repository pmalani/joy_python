from functools import partial

times = lambda x, y: x * y
print('times', times(2, 3))

double = lambda x: times(2, x)
print('double', double(10))

def do_something_useful(n, f):
    f(n)
do_something_useful(2, print)

def acc(n):
    def inner():
        nonlocal n
        temp = n
        n += 1
        return temp
    return inner
a = acc(10)
print('acc', a())
print('acc', a())
print('acc', a())

def m(p, q):
    return p * q
print(m(5, 10))

m2 = partial(m, 2)
print(m2(10))

# without partial
def n(r):
    return m(r, 2)

print(n(20))

# partial using lambda
o = lambda x: m(x, 2)
print(o(40))

def inner1():
    print("inner1")

def outer1(i):
    print("outer1")
    i()

outer1(inner1)

# same as calling outer1(inner2)
@lambda x: outer1(x)
def inner2():
    print("inner2")
