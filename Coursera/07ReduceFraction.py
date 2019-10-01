def GCD(a, b):
    '''
    Наибольший общий делитель a, b
    '''
    while b:
        a, b = b, a % b
    return a


def ReduceFraction(n, m):
    gcd = GCD(n, m)
    if gcd == 1:
        return n, m
    else:
        return ReduceFraction(n//gcd, m//gcd)

n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
