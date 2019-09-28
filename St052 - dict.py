'''
Для каждого файла известно, с какими действиями можно к нему обращаться:
запись W,
чтение R,
запуск X.
В первой строке содержится число N — количество файлов
В N строчках содержатся имена файлов и допустимых с ними операций
разделенные пробелами.
чиcло M — количество запросов к файлам.
В M строках указан запрос вида
Операция Файл.
К одному и тому же файлу может быть применено любое колличество запросов.

программа для каждого запроса должна будет возвращать
 OK если над файлом выполняется допустимая операция, или же
 Access denied, если операция недопустима.
'''
n, rules = int(input()), dict()
for _ in range(n):
    fn, rwx = input().split(maxsplit=1)
    rules.setdefault(fn, rwx.split())
# одной строкой
# [rules.setdefault(fn, rwx.split()) for fn, rwx in (input().split(maxsplit=1) for _ in range(n))]
# print(rules)

m, op = int(input()), {'read': 'R', 'write': 'W', 'execute': 'X'}
for _ in range(m):
    command, fn = input().split()
    print('OK' if op[command] in rules[fn] else 'Access denied')

''' или считываем всё сразу ~ не оптимально
commands = list(input().split() for _ in range(m))
# print(commands)
for command, fn in commands:
    print('OK' if op[command] in rules[fn] else 'Access denied')
'''



'''input
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog


output
OK
Access denied
Access denied
OK
OK
'''