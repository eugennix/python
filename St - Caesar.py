'''
Шифр Цезаря заключается в замене каждого символа входной строки на символ,
 находящийся на несколько позиций левее или правее его в алфавите.

Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему
 символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Используемый алфавит − пробел и малые символы латинского алфавита:
 ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число.
 Положительное число соответствует сдвигу вправо.
  На второй строке указывается непустая фраза для шифрования.
 Ведущие и завершающие пробелы не учитывать.
'''
'''v1
orig = ' abcdefghijklmnopqrstuvwxyz'
# обрезаем сдвиг по длине допустимых символов
n = int(input()) % len(orig)
txt = input().strip()
# разрезаем строку и переставляем, потом в словарь
shifted = orig[n:] + orig[:n]
caesar = dict(zip(orig, shifted))

print(f'Result : "{"".join([caesar[x] for x in txt])}"')
'''

#v2  - - translate !!

orig = ' abcdefghijklmnopqrstuvwxyz'
# обрезаем сдвиг по длине допустимых символов
n = int(input()) % len(orig)
txt = input().strip()
# разрезаем строку и переставляем, потом в словарь
shifted = orig[n:] + orig[:n]
caesar = dict((ord(o), c) for o, c in zip(orig, shifted))

print(f'Result : "{txt.translate(caesar)}"')


orig = ' abcdefghijklmnopqrstuvwxyz'
# обрезаем сдвиг по длине допустимых символов
n, txt = int(input()) % len(orig), input().strip()
# разрезаем строку и переставляем, потом в словарь
caesar = dict((ord(o), c) for o, c in zip(orig, orig[n:] + orig[:n]))
print(f'Result : "{txt.translate(caesar)}"')
