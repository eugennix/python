l = list(map(int, input().split()))
minx = 2**110
for x in l:
    if x % 2 and x < minx:
        minx = x
print(minx)
