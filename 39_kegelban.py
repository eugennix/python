""" N кеглей выставили в один ряд, слева направо от 1 до N. Затем по этому ряду
 бросили K шаров, при этом i-й шар сбил все кегли от lᵢ до rᵢ включительно
https://www.coursera.org
/learn/python-osnovy-programmirovaniya/programming/mD2c9/kieghiel-ban
"""
n, k = map(int, input().split())
result = set(range(1, n+1))
for _ in range(k):
    li, ri = map(int, input().split())
    falls = set(range(li, ri+1))
    result.difference_update(falls)

print(*[('I' if i in result else '.') for i in range(1, n+1)], sep='')
