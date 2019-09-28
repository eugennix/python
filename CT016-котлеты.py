"""
На сковородку одновременно можно положить k котлет.
Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно.
За какое наименьшее время удастся поджарить с обеих сторон n котлет?

Программа получает на вход три числа: k,m,n.
"""

capacity, fryTime, kotlet = int(input()), int(input()), int(input())
sides = kotlet * 2
if kotlet < capacity:
    fryPans = 2
else:
    fryPans = sides // capacity
    if sides % capacity:
        fryPans += 1
print(fryPans * fryTime)
