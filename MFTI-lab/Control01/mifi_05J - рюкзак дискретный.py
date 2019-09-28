'''
дискретный рюкзак

Дано N предметов. Каждый из них имеет вес w i и стоимость p i .
Также имеется рюкзак вместимостью W.
найти такой набор предметов, что их суммарная стоимость максимальна,
а суммарный вес не превосходит вместимость рюкзака.
 Ответом на задау надо будет вывести стоимость такого набора.

Формат входных данных
На первых двух строках даны натуральные числа N и W, не превосходящие 100.
 На следующих 2*M строках даны пары чисел натуральных w i ≤ 100 и p i ≤ 1000.
'''
'''
import sys
def group(iterable, count):
    """ Группировка элементов последовательности по count элементов """
    return zip(*[iter(iterable)] * count)

n, need_weight = int(sys.stdin.readline()), int(sys.stdin.readline())
#       [(weight, cost)]
items = list(group([int(line.strip()) for line in sys.stdin.readlines()], 2))
items_l = len(items)
# print(*items)
'''

n, need_weight = int(input()), int(input())
#       [(weight, cost)]

items =list((int(input()), int(input())) for _ in range(n))

# предметы сортируем по их стоимость/объём
items.sort(key=lambda x: x[1]/x[0], reverse=True)
items = [[0, 0]] + items
print(*items)
# нулевые границы не используем
#
Fij = [[[0, 0]] * (n+1) for _ in range(n+1)]

'''
for i in range(1, n+1):
    for j in range (1, n+1):
        wj, cost_j = items[j]
        w1, cost_1 = Fij[i-1][j]
        w2, cost_2 = Fij[i][j-1]
        cost_1, cost_2 = cost_1 + cost_j, cost_2 + cost_j
        w1, w2 = w1 + wj, w2 + wj
        if w1 <= need_weight and cost_1 > cost_2:
            Fij[i][j] = [w1, cost_1]
        elif w2 <= need_weight and cost_1 < cost_2:
            Fij[i][j] = [w2, cost_2]
        elif w1 <= need_weight:
            Fij[i][j] = [w1, cost_1]
        elif w2 <= need_weight:
            Fij[i][j] = [w2, cost_2]
        elif w1 < w2:
            Fij[i][j] = [w1 - wj, cost_1 - cost_j]
        else:
            Fij[i][j] = [w2 - wj, cost_2 - cost_j]

print(*Fij, sep='\n')

'''
