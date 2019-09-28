"""
https://stepik.org/lesson/3369/step/11?unit=952
Выведите таблицу размером n?n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
x, y, dx, dy, n = 0, 0, 0, 1, int(input())
# init tables
p = [[0] * n for i in range(n)]
bad_xy = {-1, n}

# place numbers
for i in range(1, n * n + 1):
    p[x][y] = i
    #   indexes out of range                  or cell already used
    if ((x+dx) in bad_xy or (y+dy) in bad_xy) or p[x + dx][y + dy]:
        dx, dy = dy, -dx
    x += dx
    y += dy

[print(*l) for l in p]
def f(n):
    return n * 10 + 5
print(f(f(f(10))))
