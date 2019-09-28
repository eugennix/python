'''
 получению n-ого числа из Последовательности Люка.

Как и в последовательности Фибоначчи у нас есть 2 начальных члена, но на сей раз это произвольные числа.
Например, 12345 и 67890. Их сумма даст нам следующий элемент. И так далее.

Т.е. Ln = Ln−1 + Ln−2
L(2n)=L(n)^2 − 2∗(−1)^n;
L(3n)=L(n)^3 − 3∗(−1)^n∗L(n);
L(4n)=L(n)^4 − 4∗(−1)^n∗L(n)^2 + 2;
L(5n)=L(n)^5 − 5∗(−1)^n∗L(n)^3 + 5∗L(n);
L(6n)=L(n)^6 − 6∗(−1)^n∗L(n)^4 + 9∗L(n)^2−2∗(−1)^n
'''

count = 0
Ld = {1: 2, 2: 1, 3: 3, 4: 4, 5: 7, 6: 11, 7: 18, 8: 29, 9: 47}

from functools import lru_cache
@lru_cache(maxsize=None)
def Lucas(n):
    nx = n
    if n < 9:
        return (2, 1, 3, 4, 7, 11, 18, 29, 47, 76)[n - 1]
    if not n % 6:
        n6 = n // 6
        L6 = Lucas(n6)
        if n6 % 2: return L6**6 + 6 * L6**4 + 9 * L6**2 + 2
        else:     return L6**6 - 6 * L6**4 + 9 * L6**2 - 2
    elif not n % 5:
        n5 = n // 5
        L5 = Lucas(n5)
        if n5 % 2: return L5**5 + 5 * L5**3 + 5 * L5
        else:     return L5**5 - 5 * L5**3 + 5 * L5
    elif not n % 4:
        n4 = n // 4
        L4 = Lucas(n4)
        if n4 % 2: return L4**4 + 4 * L4**2 + 2
        else:     return L4**4 - 4 * L4**2 + 2
    elif not n % 3:
        n3 = n // 3
        L3 = Lucas(n3)
        if n3 % 2: return L3**3 + 3 * L3
        else:     return L3**3 - 3 * L3
    elif not n % 2:
        n2 = n // 2
        if n2 % 2: return Lucas(n2)**2 + 2
        else:     return Lucas(n2)**2 - 2

    Ln = Lucas(n - 1) + Lucas(n - 2)
    return Ln



print(*[Lucas(i) for i in range(1, 20)], sep=', ')

import time
start = time.time()
x = 810101
lc = str(Lucas(x))
print(f'Lucas {x} = {len(lc)}')
print(f"time - {time.time()-start} sec")

