
def fac1(n):
    return 1 if n <= 1 else n * fac1(n-1)
print(fac1(5))
# print(fac1(10_000))

def fac2(n, acc=1):
    if n <= 1:
        return acc
    return fac2(n-1, n*acc)
print(fac2(5))
print(fac2(10_000))
