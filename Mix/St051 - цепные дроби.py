chislitel, znamenatel = (map(int, input().split('/')))
# s = []
while znamenatel:
    a, znamenatel, chislitel = *divmod(chislitel, znamenatel), znamenatel
    print(a, end=' ')
# print(*s)

'''
a, b = map(int, input().split('/'))
while b:
    print(a // b, end=' ')
    a, b = b, a % b
'''