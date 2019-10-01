a, b, c, d, e = [int(input()) for _ in range(5)]
result = 0
for x in range(1001):
    if x != e and not (a * x**3 + b * x**2 + c * x + d):
        result += 1
print(result)
