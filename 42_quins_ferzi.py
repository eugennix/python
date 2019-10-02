# дана расстановка 8 ферзей, ? - есть ли среди них пара бьющих друг друга
# для каждого ферзя посчитаем сколько его бьют, для упрощения - когда
# в пару попал один и тотже ферзь считаем количество битых с -1

queen_positions = [tuple(map(int, input().split())) for _ in range(8)]
attack = -8
for x1, y1 in queen_positions:
    for x2, y2 in queen_positions:
        attack += int(not (x1-x2)*(y1-y2)*(abs(x1-x2)-abs(y1-y2)))
print('YES' if attack else 'NO')
