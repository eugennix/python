"""  Дан список. Выведите те его элементы, которые встречаются в списке только
 один раз. Элементы выводить в том порядке, в котором они встречаются в списке.
"""
from collections import Counter

c = Counter(map(int, input().split()))

print(*[elem for elem, count in c.items() if count == 1])
