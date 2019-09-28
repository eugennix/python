import requests
from lxml import etree

url0 = r'https://docs.python.org/3/'
res = requests.get(url0)
print(res.headers['Content-Type'])
if res.status_code == 200:
    parser = etree.HTMLParser()
    page_root = etree.fromstring(res.text, parser)

#for elem in page_root.iter('a'):
#    print(elem.attrib)

for elem in page_root.iter():
    if elem.attrib.get('class'):
        print(elem.attrib['class'], elem.attrib, elem.text)