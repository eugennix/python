def GCD(a, b):
    '''
    Наибольший общий делитель a, b
    '''
    while b:
        a, b = b, a%b
    return a

a, b = 14159572, 63967072
print(GCD(a, b))
print(GCD(b, a))
