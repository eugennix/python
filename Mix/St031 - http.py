import requests
import re
'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, 
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, 
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

'''
urlA, urlB = input(), input()
# urlA = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# urlB = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

def parse_A_href(txt):
    ''' 
    :param txt: text/html as string
    :return: list of string [link1, ....] in tags <a href="link">
    '''
    patternA = r'<a.*?href=[\'"](.*?)[\'"]'
    return re.findall(patternA, txt)

def parse_A_href(txt):
    '''
    :param txt: text/html as string
    :return: list of string [link1, ....] in tags <a href="link">
    '''
    #patt_href = r'href\s*=\s*[\'"](.+?)[\'"]'
    return re.findall(r'href\s*=\s*[\'"](.+?)[\'"]', txt)


r = requests.get(urlA)
result = 'No'
if r.status_code == 200:
    pageA_links = parse_A_href(r.text)
    for lnk in pageA_links:
        r = requests.get(lnk)
        if r.status_code == 200 and urlB in parse_A_href(r.text):
            result = 'Yes'
            break
print(result)


pat = r'href\s*=\s*[\'"](.+?)[\'"]'

import requests, re
urls = [input() for cmd in range(2)]
p = 'No'

for i in re.findall(r'<a.*href="(.*)">', requests.get(urls[0]).text):
    if urls[1] in re.findall(r'<a.*href="(.*)">', requests.get(i).text):
        p = 'Yes'
        break
print(p)