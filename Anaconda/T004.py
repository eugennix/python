n = int(input())
countEql = 1 if n else 0
numEql = n
countMax = countEql
while n != 0:
    n = int(input())
    if n == numEql:
        countEql += 1
    else:
        if countEql > countMax:
            countMax = countEql
        numEql = n
        countEql = 1
print(countMax)
