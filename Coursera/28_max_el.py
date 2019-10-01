l = list(map(int, input().split()))
mx, mxi = l[0], 0
for i, x in enumerate(l):
    if x > mx:
        mx, mxi = x, i
print(mx, mxi)
