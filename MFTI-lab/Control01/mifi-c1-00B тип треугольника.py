''' # определить тип треугольника
    right для прямоугольного треугольника
    acute для остроугольного треугольника
    obtuse для тупоугольного треугольника
    impossible треугольника с такими сторонами не существует.
'''

a, b, c = int(input()), int(input()), int(input())
# = c - max
a, b, c = sorted([a, b, c])
a2b2, c2 = a**2 + b**2, c**2
if c >= a + b:
    print('impossible')
elif c2 == a2b2:
    print('right')
elif c2 < a2b2:
    print('acute')
else:
    print('obtuse')
