# високосный год
y = int(input())
if y % 4:
    print('NO')
elif y % 100:
    print('YES')
elif y % 400:
    print('NO')
else:
    print('YES')
