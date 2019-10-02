""" Даны два списка, упорядоченных по возрастанию (каждый список состоит из
 различных элементов). Найдите пересечение множеств элементов этих списков,
 то есть те числа, которые являются элементами обоих списков.
 Алгоритм должен иметь сложность O(len(A)+len(B)).
"""

def intersect(li1, li2):
    i, j, len1, len2, res = 0, 0, len(li1), len(li2), []
    while i < len1 and j < len2:
        if li1[i] == li2[j]:
            res.append(li1[i])
            i += 1
            j += 1
        elif li1[i] < li2[j]:
            i += 1
        else:
            j += 1
    return res


print(*intersect(list(map(int, input().split())),
                 list(map(int, input().split()))))
