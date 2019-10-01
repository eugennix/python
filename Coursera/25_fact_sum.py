n, su, fak = int(input()), 0, 1
for x in range(1, n+1):
    fak *= x
    su += fak
print(su)
