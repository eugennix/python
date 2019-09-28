import requests

url0 = 'http://example.com'
r = requests.get(url0)
if r.status_code == 200:
    print("ok")
else:
    print("NOk ", r.status_code)
par = {'key1': 'val1', 'key2': 'val2'}
r = requests.get(url0, params=par)
print(r.url)
# print(r.content)
# print(r.text)
