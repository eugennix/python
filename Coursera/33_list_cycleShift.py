l = list(map(int, input().split()))
if l:
    l.insert(0, l.pop())
print(*l)
