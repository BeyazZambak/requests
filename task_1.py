from pprint import pprint

import requests

def test_request():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    responses = requests.get(url)
    responce_list = responses.json()
    max_intelligence = 0
    count = 0
    for powerstats in responce_list:
        if powerstats['name'] == 'Hulk' or powerstats['name'] == 'Captain America' or powerstats['name'] == 'Thanos':
            if count < int(powerstats['powerstats'].get('intelligence')):
                count = powerstats['powerstats'].get('intelligence')
                max_intelligence = powerstats['name']
            # pprint(powerstats['powerstats'].get('intelligence'))
    print(f'Самый сильный среди Hulk, Captain America и Thanos: {max_intelligence}')

if __name__ == '__main__':
    test_request()