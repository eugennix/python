def C_n_k(n, k, f={}):
    # кэшируем в словаре f
    if k == n or not k or not n:
        return 1
    if k == 1:
        return n
    if (n, k) not in f:
        f[(n, k)] = C_n_k(n-1, k) + C_n_k(n-1, k-1)
    return f[(n, k)]


print(C_n_k(int(input()), int(input())))
