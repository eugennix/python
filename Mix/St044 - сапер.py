'''
Поле для игры сапёр - сетку размером n×m. В ячейке сетки может находиться мина.
программу, выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной,
 указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)

На первой строке указываются два натуральных числа 1≤n,m≤100,
 после чего в n строках содержится описание поля в виде последовательности точек '.'
 и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
 n строк поля, в каждой ячейке которого будет либо число от 0 до 8,
 либо мина (обозначенная символом "*"), при этом число означает
 количество мин в соседних ячейках поля.
'''

n, m = map(int, input().split())
pole = [list(x) for x in [input() for i in range(n)]]
# print(*[''.join(l) for l in pole], sep='\n')

for y, lin in enumerate(pole):
    for x, col in enumerate(lin):
        if col != '*':
            count = 0
            for b in range(max(x-1, 0), min(x+2, len(lin))):
                for a in range(max(y-1, 0), min(y+2, len(pole))):
                    if pole[a][b] == '*':
                        count += 1
            pole[y][x] = str(count)
print(*[''.join(l) for l in pole], sep='\n')

'''
# stars - это список координат всех звездочек

n, m = [int(x) for x in input().split()]
stars = [(i, j) for i in range(n) for j, c in enumerate(input()) if c == '*']

for i in range(n):
    for j in range(m):
        if (i, j) in stars:
            print('*', end='')
        else:
            print (sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if (x, y) in stars), end='')
    print()
'''
sorted(r)
'''
for i in range(n):
    for j in range(m):
        if mines[i][j] != '*':
            x = [mines[x][y] for x in [i-1, i, i+1] if 0<=x<=(n-1) for y in [j-1, j, j+1] if 0<=y<=(m-1)]
            print(x.count('*'), end='')
        else:
            print('*', end='')
    print()
'''