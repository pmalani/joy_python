
times = lambda x, y: x * y

double = lambda x: times(2, x)

def do_something_useful(n, f):
    f(n)

def acc(n):
    def inner():
        nonlocal n
        temp = n
        n += 1
        return temp
    return inner

print('times', times(2, 3))
do_something_useful(2, print)

a = acc(10)
print('acc', a())
print('acc', a())
print('acc', a())

print('double', double(10))