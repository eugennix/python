l = list(map(int, input().split()))
if l:
    l_last = l[-1]
    for i in range(len(l)-1, 0, -1):
        l[i] = l[i-1]
    l[0] = l_last
print(*l)
