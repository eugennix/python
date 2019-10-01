def power(a, n):
    if n:
        if n % 2:
            return a * power(a, n - 1)
        else:
            return power(a * a, n//2)
    else:
        return 1

a, n = float(input()), int(input())
a, n = (a, n) if n >= 0 else (1 / a, -n)
print(power(a, n))
