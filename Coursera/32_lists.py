'''
Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
'''

l = list(map(int, input().split()))

for i in range(1, len(l), 2):
    l[i-1], l[i] = l[i], l[i-1]

print(*l)
