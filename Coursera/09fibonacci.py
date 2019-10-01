def fib(n, f={}):
    # кэшируем в словаре f
    if n < 3:
        return 1
    if n in f:
        return f[n]
    f[n] = fib(n-2) + fib(n-1)
    return f[n]


print(fib(int(input())))
