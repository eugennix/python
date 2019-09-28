def fb(n):
    F1, F2 = 0, 1
    while n:
        n -= 1
        F1, F2 = F2, F1 + F2
    return F1



def fib(q: int) -> int:
    """ Effective Fibonacci function
    Формула Бине :)"""
    return pow(2 << q, q + 1, (4 << 2 * q) - (2 << q) - 1) % (2 << q)

# good
def fib(n):
    a = b = 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# рекурсия с кешированием результатов
from functools import lru_cache

@lru_cache()
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

# рекурсия с кешированием результатов
f={}
def fib(n):
    if n < 3: return 1
    if n in f: return f[n]
    f[n] = fib(n-2) + fib(n-1)
    return f[n]




for i in range(1, 100):
    print(i, fib(i))
