def make_Pisano_period(m):
    ''' возвращает последовательность Пизано,
        цикличная последовательность чисел Фибоначи по модулю m > 0
        всегда начинается с 0, 1. Если встретились значение 0, 1 -
        значит пошла следующая цепочка.
        для m == 1 длина 1, для 2 - 3, 3 - 8 и т.д.
    '''
    pisano = [0, 1]
    # три последовательных числа Фибоначи
    F0, F1, F2 = 0, 1, 1
    if m == 1:
        return pisano[:1]
    for i in range(6 * m):
        # F0 чтобы не обращаться лишний раз к pisano[-1]
        F0, F1, F2 = F1, F2, (F1 + F2) % m
        if F0 == 0 and F1 == 1:
            # последный элемент уже с другой цепочки, обрезаем
            return pisano[:-1]
        pisano.append(F1)


def fib_mod(n, m):
    pisano = make_Pisano_period(m)
    print(len(pisano), pisano)
    return pisano[n % len(pisano)]

# 1025 55  5
# 1598753 25897 - 20305
# n, m = 1598753, 25897
n, m = 10, 2

print(fib_mod(n, m))

'''
def fib_mod(n, m):
    pisano = [0,1]
    f0, f1 = 0,1
    for i in range(6*m):
        f0,f1=f1,(f1+f0)%m
        pisano += [f1]
        if pisano[-2:]==[0,1]:
            break
    return pisano[n%(len(pisano)-2)]
'''