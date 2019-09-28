# Tribonacci
T0, T1, T2 = 0, 0, 1
n, count = int(input()), 2
#if n:
while n:
    count += 1
    T0, T1, T2 = T1, T2, T0 + T1 + T2
    if T2 > n:
        break
print(count)
