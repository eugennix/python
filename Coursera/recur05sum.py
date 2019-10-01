def sum(a, b):
    if b:
        return sum(a, b-1) + 1
    elif a:
        return sum(a-1, b) + 1
    else:
        return 0

a, b = int(input()), int(input())
print(sum(a, b))
