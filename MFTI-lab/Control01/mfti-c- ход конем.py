''''''
kx, ky, hx, hy = [int(input()) for _ in range(4)]
# добавляю +1 к шахматной доске, чтоб не пересчитывать координаты от 0
# max траектория длиной 6, => необработанное ставим == 99
# новые клетки передаём через очередь to_process = list()
pole = [[99]*9 for _ in range(9)]
hody = ((-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1))

# начальный случай
to_process = [(x1, y1)]
pole[x1][y1] = 0

# обсчитываем доску
while to_process:
    X, Y = to_process.pop(0)
    curr_min = pole[X][Y]
    # делаем все ходы
    for dx, dy in hody:
        nextX, nextY = X + dx, Y + dy
        if 0 < nextX < 9 and 0 < nextY < 9:
            f_next = pole[nextX][nextY]
            if f_next > curr_min + 1:
                pole[nextX][nextY] = curr_min + 1
                to_process.append((nextX, nextY))

# print(*pole, sep='\n')
result = pole[x2][y2]
print(-1 if result > 2 else result)
