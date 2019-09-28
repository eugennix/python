import requests
import re

'''
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида
<a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов.
То есть, это последовательность символов, которая следует сразу после символов
протокола, если он есть, до символов порта или пути, если они есть, за исключением
 случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
'''
# urlA = input().strip()
# urlA = 'http://yandex.ru/'
urlA = 'http://pastebin.com/raw/7543p0ns'
# urlA = 'http://pastebin.com/raw/hfMThaGb'

from urllib.parse import urlparse

r = requests.get(urlA)
d_sites = dict()
pattern = r'<a\s.*?\bhref\s*?=\s*?([\'\"])(\w+://)?(\w.*?)(:\d{1,5})?(/.*?)*\1.*?>.*'
# <a\s.*?\bhref\s*?=\s*?([\'\"]) от начала тега <a до значения атрибута href
# (\w+://)? протокол (1 или 0 вхождение)
# (\w.*?) искомый адрес сайта, начинается с буквы/числа (\w), чтобы отсечь '..'
# (:\d{1,5})? порт (1 или 0 вхождение)
# (/.*?)* относительный путь на сервере (0 или много вхождений)
# \1 закрывающая кавычка атрибута href
# .*?>.* символы до закрывающей скобки тега a, скобка >, остаток строки после тега <a>

if r.status_code == 200:
    sites = set([match.group(3) for match in re.finditer(pattern, r.text)])
    print(*sorted(sites), sep='\n')
# print(*sorted(d_sites), sep='\n')
# print(len(d_sites))

correct = set()
with open("result.txt") as r:
    for ln in r.readlines():
        correct.add(ln.strip())
print(correct)

for co in correct:
    if co not in sites:
        print('нету -- ', co)

for my in sites:
    if my not in correct:
        print('лишнее -- ', my)


pattern = r'<a\s.*?\bhref\s*?=\s*?([\'\"])(\w+://)?(?P<host>\w.*?)(:\d{1,5})?(/.*?)*\1.*?>.*'
# <a\s.*?\bhref\s*?=\s*?([\'\"]) от начала тега <a до значения атрибута href
# (\w+://)? протокол (1 или 0 вхождение)
# (\w.*?) искомый адрес сайта, начинается с буквы/числа (\w), чтобы отсечь '..'
# (:\d{1,5})? порт (1 или 0 вхождение)
# (/.*?)* относительный путь на сервере (0 или много вхождений)
# \1 закрывающая кавычка атрибута href
# .*?>.* символы до закрывающей скобки тега a, скобка >, остаток строки после тега <a>



link_regex = r'''<a.*href=["|'](?!../)(?:\w+://)?([\w\._-]+)'''
content = requests.get(sys.stdin.read())
links = re.findall(link_regex, content.text)
print(*sorted(set(links)), sep='\n')
