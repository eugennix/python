def is_in_area(x, y):
    return ((x+1)**2 + (y-1)**2) <= 4 \
        and y >= -x and y >= (x + 1) * 2 \
        or ((x+1)**2 + (y-1)**2) >= 4 \
        and y <= -x and y <= (x + 1) * 2

x, y = float(input()), float(input())
print(('NO', 'YES')[is_in_area(x, y)])
