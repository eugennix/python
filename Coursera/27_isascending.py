def IsAscending(l: list):
    i = 1
    while i < len(l) and l[i] > l[i-1]:
        i += 1
    return i == len(l)


l = list(map(int, input().split()))
print(('NO', 'YES')[IsAscending(l)])
