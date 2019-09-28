import requests


url0 = 'https://stepic.org/media/attachments/course67/3.6.3/'
url1 = '699991.txt'
r = requests.get(url0+url1)
count = 1
while True:
    print(f'file {count}: ', url1, end=' ->')
    count += 1
    if r.status_code == 200:
        print("ok")
    else:
        print("NOk ", r.status_code)

        break
    txt = r.text
    if txt[:2] == 'We':
        break
    url1 = txt

    r = requests.get(url0+url1)


with open('result.txt', 'w') as res:
    res.write(txt)
print('TOTAL ', count)
