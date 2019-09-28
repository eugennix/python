'''
белый король и черный конь. Конь неподвижен, король может ходить на одну клетку
вправо, на одну клетку вверх или наискосок вправо-вверх.
 Посчитайте, сколькими способами король может дойти до клетки
  h8, начав с клетки a1. Королю нельзя попадать под атаку коня.
  Самого коня есть тоже нельзя.

Строки шахматной доски пронумерованы числами от 1 до 8,
столбцы буквами от a до h. Строка 1 - самая нижняя, столбец a - самый левый.

Формат входных данных
В единственной строке - позиция коня.
Позиция - это два символа, буква столбца и номер строки, например a3.

'''
transl = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
horse = input()
hx, hy = transl[horse[0]],  int(horse[1])
# print(f'Horse {hx} {hy}')
# добавляю +1 к шахматной доске, чтоб не пересчитывать координаты от 0
pole = [[0]*9 for _ in range(9)]

horse_moves = ((-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1))
# запрещённые позиции, бьются конём

pole[hx][hy] = 'H'
for dx, dy in horse_moves:
    nextX, nextY = hx + dx, hy + dy
    if 0 < nextX < 9 and 0 < nextY < 9:
        pole[nextX][nextY] = 'H'
print(*pole, '\n', sep='\n')


# начальный случай
kx, ky = 1, 1
to_process = []
if pole[kx][ky] != 'H':
    to_process = [(kx, ky)]
    pole[kx][ky] = 1

king_moves = ((-1, 0), (0, -1), (-1, -1))

# обсчитываем доску
for X in range(1, 9):
    for Y in range(1, 9):
        if pole[X][Y] != 'H':
            for dx, dy in king_moves:
                predX, predY = X + dx, Y + dy
                if 0 < predX < 9 and 0 < predY < 9 and pole[predX][predY] != 'H':
                    pole[X][Y] += pole[predX][predY]

print(*pole, sep='\n')
result = pole[8][8]
print(result if result != 'H' else 0)
