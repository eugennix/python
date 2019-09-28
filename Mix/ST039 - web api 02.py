import requests

def num_facts(n):
    '''    :return: ('Boring' or 'Interesting', fact )
    '''
    api_url = 'http://numbersapi.com/' + str(n) + '/math?json=true'
    # params = {'json': 'true'}
    res = requests.get(api_url)
    if res.status_code == 200:
        ans = res.json()
        return ('Interesting', ans['text']) if ans['found'] else ('Boring', ans['text'])
    return None

with open('dataset.txt') as test_nums:
    for t_num in test_nums:
        bifact = num_facts(t_num.strip())
        print(bifact[0], bifact[1])
