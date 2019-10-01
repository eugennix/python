def gcd(a, b):
    '''
    Наибольший общий делитель a, b
    '''
    while b:
        a, b = b, a % b
    return a

a, b = int(input()), int(input())
print(gcd(a, b))
