'''
непрерывный рюкзак

количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106
предмета (n, W, ci, wi — целые числа).
Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
'''

'''
!!!!!
import sys
# создаём генератор для чтения вместо input()
reader = (tuple(map(int, line.split())) for line in sys.stdin)
n, need_weight = next(reader)
# читаем сразу всё ;-)
items = list(reader)
# проверка длины
assert (len(items) == n)
'''

n, need_weight = map(int, input().split())
#             (cost, weight)
items = [tuple(map(int, input().split())) for i in range(n)]

# предметы сортируем по их стоимость/объём
items.sort(key=lambda x: x[0]/x[1], reverse=True)

total_cost = 0
for (cost, weight) in items:

    if weight <= need_weight:
        total_cost += cost
        need_weight -= weight
        continue
    else:
        # берём часть последнего предмета
        partial_cost = need_weight/weight * cost
        total_cost += partial_cost
        break

print(f'{total_cost:.3f}')
