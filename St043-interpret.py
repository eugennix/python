'''
На вход подаётся строка с выражением, состоящим из двух чисел,
объединённых бинарным оператором: a operator b, где вместо operator  использоваться
 plus, minus, multiply, divide -  целочисленного деления.

Формат ввода:
a operator b, 0≤a,b≤1000. Оператор может быть plus, minus, multiply, divide.

--> Строка, содержащая целое число − результат вычисления.
'''
oper = {'plus': int.__add__, 'minus': int.__sub__,
        'multiply': int.__mul__, 'divide': int.__floordiv__}
'''
import operator
opers = {'plus': operator.add, 'minus': operator.sub,
         'multiply': operator.mul, 'divide': operator.floordiv}
'''
a, op, b = input().split()
print(oper[op](int(a), int(b)))


'''
# Обернул в функцию, тогда можно обойтись без лямбды в значениях словаря
def calc(a, op, b):
    c = {   "plus": a + b,
            "minus": a - b,
            "multiply": a * b,
            "divide": a // b
        }
    return c[op]

s = input().split()
print(calc(int(s[0]), s[1], int(s[2])))
'''

'''
ops = {'plus': lambda x,y: x+y,
       'minus': lambda x,y: x-y,
      'multiply': lambda x,y: x*y,
      'divide': lambda x,y: x//y}
print(ops[op](int(a), int(b)))'''

'''
print(eval (input()
    .replace("plus", "+")
    .replace("minus", "-")
    .replace("multiply", "*")
    .replace("divide", "//")))
'''

'''
Технически, это решение в 2 строчки. Мое решение повторяет идею данного решения. 
Если вы посмотрите, то увидите, что не так много решений 
объединяют print() и input() в одну строку.

operator_dict = {
    'plus' : lambda x,y: x + y,
    'minus' : lambda x,y: x - y,
    'multiply' : lambda x,y: x * y,
    'divide' : lambda x,y: x // y
    }

print(eval("operator_dict['{1}']({0}, {2})".format(*input().split())))
'''