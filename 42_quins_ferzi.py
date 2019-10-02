""" Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них
 пара бьющих друг друга
"""

positions = [tuple(map(int, input().split())) for _ in range(8)]
pole = [[0]*8 for _ in range(8)]
print(pole, positions)

for queen_x, queen_y in positions:
    pass

