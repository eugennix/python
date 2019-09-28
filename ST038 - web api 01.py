import requests

'''
    API сайта artsy.net
    API проекта Artsy предоставляет информацию о некоторых деятелях искусства, 
    
    Вам даны идентификаторы художников в базе Artsy.
    Для каждого идентификатора получите информацию о имени художника и годе рождения.
    Выведите имена художников в порядке неубывания года рождения. 
    В случае если у художников одинаковый год рождения, 
    выведите их имена в лексикографическом порядке.
    
    Name	        eugenga
    Client Id	    270bb355036b1ad322a2
    Client Secret	9e82a074484b9f24a0c7196faa0b039b

'''

cl_id = '270bb355036b1ad322a2'
cl_sec = '9e82a074484b9f24a0c7196faa0b039b'
api_url = 'https://api.artsy.net/api/tokens/xapp_token'

#  запрос на получение токена
token = requests.post(api_url, data={"client_id": cl_id, "client_secret": cl_sec}).json()['token']
''' {'type': 'xapp_token', 
    'token': '....', 
    'expires_at': '2019-08-31T07:16:38+00:00', 
    '_links': {}}
'''
headers = {"X-Xapp-Token": token}
url_artists = 'https://api.artsy.net/api/artists/'
templ = lambda a: f"{a['sortable_name']:30} {a['birthday']}{'+' if a['deathday'] else ' '}" +\
                  f"{ 'M' if a.get('gender') == 'male' else 'F'} " +\
                  f"{a.get('nationality', 'xx'):>15} - {a.get('hometown', 'xx'):25}"

artists = list()
with open('dataset.txt') as infi:
    for artist_id in infi:
        r = requests.get(url_artists + artist_id.strip(), headers=headers,)
        r.encoding = 'utf-8'
        j = r.json()
        # print(j)
        # print(templ(j))
        artists.append(j)

# print('\norigin', *[templ(a) for a in artists], sep='\n')

artists.sort(key=lambda x: (x['birthday'], x['sortable_name']))

# print('\nsorted', *[templ(a) for a in artists], sep='\n')

print('\nsorted\n')
with open("result.txt", "w", encoding="utf8") as oufi:
    for ar in artists:
        # print(templ(ar))
        print(ar['sortable_name'], file=oufi)
