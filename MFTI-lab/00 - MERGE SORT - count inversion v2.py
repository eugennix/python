"""
    Первая строка содержит число 1≤n≤105,
    вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 109.
    Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
    (Такая пара элементов называется инверсией массива.
    Количество инверсий в массиве является в некотором смысле его мерой
    неупорядоченности: например, в упорядоченном по неубыванию массиве
    инверсий нет вообще, а в массиве, упорядоченном по убыванию,
    инверсию образуют каждые два элемента.)
"""


def MergeSort_andInversions(A: list, l=0, r=None) -> int:
    ''' Sort A, ond count it's number of inversions '''
    if r is None:
        r = len(A) - 1
    inv = 0
    if l < r:
        m = (l + r) // 2
        inv += MergeSort_andInversions(A, l, m)
        inv += MergeSort_andInversions(A, m + 1, r)
        inv += merge_and_count_inversions(A, l, m, r)
    return inv


def merge_and_count_inversions(A: list, l, m, r) -> int:
    lenL = m - l + 1
    lenR = r - m
    # создаём части списки L и R
    L, R = [0] * lenL, [0] * lenR
    for i in range(lenL): L[i] = A[l + i]
    for j in range(lenR): R[j] = A[m + 1 + j]
    inv = 0
    i, j, k = 0, 0, l
    while i < lenL and j < lenR:
        if L[i] > R[j]:
            A[k] = R[j]
            j += 1
            # вот тут и считаются инверсии
            # элемент из R оббразует инверсию со всеми оставшимися из L
            inv += lenL - i
        else:
            A[k] = L[i]
            i += 1
        k += 1

    while i < lenL:
        A[k] = L[i]; i += 1; k += 1
    while j < lenR:
        A[k] = R[j]; j += 1; k += 1
    return inv



n = int(input())
A = list(map(int, input().split()))
# A = [2, 3, 9, 2, 9]
assert (n == len(A))
inv_tot = MergeSort_andInversions(A)
print(inv_tot)

'''
def merge(li1, li2):
    global inv
    res = []
    i = 0
    j = 0
    len1 = len(li1)
    len2 = len(li2)
    while True:
        if i == len1 and j == len2:
            break
        elif i == len1:
            res.append(li2[j])
            j += 1
        elif j == len2:
            res.append(li1[i])
            i += 1
        elif li1[i] == li2[j]:
            res.append(li1[i])
            i += 1
        elif li1[i] < li2[j]:
            res.append(li1[i])
            i += 1
        else:
            inv += len1 - i
            res.append(li2[j])
            j += 1
    return res


def merge_sort(li):
    if len(li) <= 1:
        return li
    m = len(li) // 2
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))


def main():
    n = int(input())
    init_list = [int(i) for i in input().split()]
    merge_sort(init_list)

'''

'''
count = 0


def merge_sort(array):
    if len(array) <= 1:  # base case
        return array
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])
    return merge(left, right)


def merge(left, right):
    lst = []
    global count
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            count += left_len - i
            j += 1
    lst += left[i:]
    lst += right[j:]
    return lst


s, lst = input(), [int(i) for i in input().split()]
merge_sort(lst)
print(count)
'''