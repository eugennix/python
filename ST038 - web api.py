import requests

city = input("input city:")
api_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Moscow',
    'units': 'metric',
    'appid': '11c0d3dc6093f7442898ee49d2430d20'
}

res = requests.get(api_url, params=params)
if res.status_code == 200:
    # print(res.headers['Content-Type'])
    ans = res.json()
    # print(ans)
    weather = ans['weather']
    main = ans['main']
    print(f"Current temperature in {params['q']} is {main['temp']} C")