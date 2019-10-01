def MinDivisor(n):
    if not n % 2:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if not n % i:
            return i
    return n

n = int(input())
print(MinDivisor(n))
