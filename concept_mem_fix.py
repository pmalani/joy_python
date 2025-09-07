from functools import cache


@cache
# cache is shortcut for
# @lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

print(fib(45))