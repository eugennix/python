def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))


'''
Погуглил что-то что остановит итерации само, когда найдет первый подходящий элемент
any() - вернёт True и остановит итерации когда первый встреченый элемент итератора будет True
all() который вернёт False и остановит итерации когда первый встреченый элемент итератора будет False
'''
def isPrime(n):
    return not any(i for i in range(2, int(n ** 0.5) + 1) if not n % i)
'''55429286448
12.232199907302856  sec'''

def isPrimeX2(n):
    # четные делители не проверяем, т.к. n подаём только нечётное
    return not any(i for i in range(3, int(n ** 0.5) + 1, 2) if not n % i)
'''
55429286448
6.405800104141235  sec'''

def isPrimeX235(n):
    # не подаём кратные 2 или 3
    # if not n % 2:  return False
    # if not n % 3:  return False
    if not n % 5:  return False

    k, qn = 7, int(n ** 0.5) + 1
    while k <= qn:
        if not n % k: return False
        k += 4
        if not n % k: return False
        k += 2
        if not n % k: return False
        k += 4
        if not n % k: return False
        k += 2
        if not n % k: return False
        k += 4
        if not n % k: return False
        k += 6
        if not n % k: return False
        k += 2
        if not n % k: return False
        k += 6
    return True
''' самое быстрое
55429286448
4.297800064086914  sec
'''

def primesGen1():
    '''  все простые == 12k+1, 12k+5, 12k+7 или 12k+11
    '''
    # при k == 0 обрабатываем отдельно, т.к. 1 - не простое, а 2 и 3 наоборот - простые
    for n in [2, 3, 5, 7, 11]: yield n
    n = 13              # k == 1   -> 12k + 1 == 13
    while True:
        if not any(i for i in range(3, int(n ** 0.5) + 1, 2) if not n % i): yield n
        n += 4          # 12k + 5
        if not any(i for i in range(3, int(n ** 0.5) + 1, 2) if not n % i): yield n
        n += 2          # 12k + 7
        if not any(i for i in range(3, int(n ** 0.5) + 1, 2) if not n % i): yield n
        n += 4          # 12k + 11
        if not any(i for i in range(3, int(n ** 0.5) + 1, 2) if not n % i): yield n
        n += 2          # 12(k+1) + 1
'''
55429286448
6.5137999057769775  sec'''


def primesGen(): # проверяем функцией isPrimeX235
    '''  все простые == 12k+1, 12k+5, 12k+7 или 12k+11
    '''
    # при k == 0 обрабатываем отдельно, т.к. 1 - не простое, а 2 и 3 наоборот - простые
    for n in [2, 3, 5, 7, 11]: yield n
    n = 13              # k == 1   -> 12k + 1 == 13
    while True:
        if isPrimeX235(n): yield n
        n += 4          # 12k + 5
        if isPrimeX235(n): yield n
        n += 2          # 12k + 7
        if isPrimeX235(n): yield n
        n += 4          # 12k + 11
        if isPrimeX235(n): yield n
        n += 2          # 12(k+1) + 1
'''
isPrime
55429286448
6.458399772644043  sec

isPrimeX235
55429286448
4.23259973526001  sec  самое быстрое
'''




# запоминаем простые. очень медленно для больших чисел
def primes1():
    x, lst_primes = 3, set()
    yield 2
    yield 3
    while True:
        x += 2
        if not any(x % div == 0 for div in lst_primes):
            lst_primes.add(x)
            yield x
'''
Громоздко, зато самое быстрое ! НЕТ ! для больших n
проверяет только по простым числам, найденым ранее 
как находит новое простое, выдаёт его и запоминает
'''
def primes2():
    primes = [2, 3, 5, 7]
    for x in primes:
        yield x
    i = 0
    while True:
        i += 10
        for end in [1, 3, 7, 9]:
            check = True
            num = i + end
            for p in primes:
                if num % p == 0:
                    check = False
                    break
                if p ** 2 > num:
                    break
            if check:
                primes.append(num)
                yield num



import itertools, time
start = time.time()
print(sum(list(itertools.takewhile(lambda x : x <= 11223431, primesGen()))))
print(time.time() -  start, ' sec')









""" непонятно
Долго думал...

Пока не вспомнил математику начальных классов, и тот факт, что если число Х делится на У, то и число (Х + У) тоже делится на У - значит оно заведомо составное.

[+] Test #1. OK

1 of 1 test(s) passed.
# Генерация бесконечной последовательности простых чисел.
def primes():
    # Словарь составных чисел (ключи) и их простых делителей (список значений)
    D = {}
    # Начало последовательности простых чисел
    q = 2
    while True:
        if q not in D:
            # q новое простое число.
            # выдаем его в генератор и запихиваем в словарь составных
            # в ключи квадрат этого простого числа, а в список значений - само простое число
            yield q
            D[q * q] = [q]
        else:
            # q составное. D[q] содержит список простых чисел, на которые оно делится
            # чистим память, удаляя из словаря по ключу текущее составное число и его делители
            # так как оно нам больше не потребуется, но предварительно занесем в словарь новые
            # составные числа, полученные сложением ключа и значения, так как по математике
            # если х/у то и (х+у)/у а значит число х+у тоже составное
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

"""

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# ## or starting with half sieve

def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]