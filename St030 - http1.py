import requests
url0 = 'https://docs.python.org/3/'
r = requests.get(url0)
print(r.status_code)
print(r.headers)
print(*r.headers, sep='\n')
# print(r.content)
# print(r.text)