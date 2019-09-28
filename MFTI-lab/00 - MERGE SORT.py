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

