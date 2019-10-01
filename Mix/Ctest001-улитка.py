h = int(input())
up = int(input())
dn = int(input())
# test = ((10, 7, 6, 4), (10, 7, 1, 2), (10, 2, 1, 9), (10, 6, 1, 2))
# for h, up, dn, answ in test:
perDay = up - dn
hDayBeforeTop = h - up
daysMinus1 = (hDayBeforeTop + perDay - 1) // perDay
# print(f'\nH {h}  up {up}  dn {dn}   ==> {answ}')
# print(f"H per day = {perDay}, H day before top HDBT = {hDayBefore}")
# print(f"to HDBT {daysMinus1} days + 1 = {daysMinus1 + 1}")
print(daysMinus1 + 1)

"""
Улитка ползет по вертикальному шесту высотой H метров, поднимаясь за день на A метров, а за ночь спускаясь на B метров. 
На какой день улитка доползет до вершины шеста?

Программа получает на вход целые H, A, B. Гарантируется, что A > B ≥ 0."""
