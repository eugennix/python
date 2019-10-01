'''
 Поменяйте местами минимальный и максимальный элемент
'''

l = list(map(int, input().split()))
if l:
    mi, mii, ma, mai = l[0], 0, l[0], 0
    for i, x in enumerate(l):
        if x > ma:
            ma, mai = x, i
        if x < mi:
            mi, mii = x, i
    l[mai], l[mii] = mi, ma

print(*l)
