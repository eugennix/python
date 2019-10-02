""" Даны два целочисленных списка A и B, упорядоченных по неубыванию.
 Объедините их в один упорядоченный список С. Решение оформите в виде функции
 merge(A, B) - Алгоритм должен иметь сложность O(len(A)+len(B)).
 Модифицировать исходные списки запрещается.
 Использовать функцию sorted и метод sort запрещается
"""

def merge(li1, li2):
    i, j, len1, len2, res = 0, 0, len(li1), len(li2), []
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
            res.append(li2[j])
            j += 1
    return res


print(*merge(list(map(int, input().split())), list(map(int, input().split()))))
