'''
 первой строке даны целое число 1≤n≤105 и массив A[1…n] из n различных
  натуральных чисел, не превышающих 109, в порядке возрастания,
   во второй — целое число 1≤k≤105 и k натуральных чисел b1,…,bk,
    не превышающих 109. Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n,
     для которого A[j]=bi, или −1, если такого j нет.
'''
massiv = tuple(map(int, input().split()))
keys = tuple(map(int, input().split()))
result = [-1] * len(keys)
# нулевые элементы не используем. там n, k
# print(massiv, keys)
for i in range(1, len(keys)):
    L, R = 1, len(massiv) - 1
    key = keys[i]
    while L <= R:
        M = (L + R) // 2
        if massiv[M] == key:
            # нашли
            result[i] = M
            break
        elif massiv[M] > key:
            R = M - 1
        else:
            L = M + 1
print(*result[1:])