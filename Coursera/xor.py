def is_in_area(x, y):
    return x and not y or not x and y

x, y = int(input()), int(input())
print((0, 1)[xor(x, y)])
