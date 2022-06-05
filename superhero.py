import requests


def get_data_superheros(url):
    headers = {'Autorization': '2619421814940190'}
    resp = requests.get(url, headers=headers)
    for name in resp.json().values():
        res = name
    res_name = res[0]['name']
    res_intelligence = int(res[0]['powerstats']['intelligence'])
    return {res_name: res_intelligence}


def get_intelligence():
    Hulk = get_data_superheros('https://superheroapi.com/api.php/2619421814940190/search/Hulk')
    Captain_America = get_data_superheros('https://superheroapi.com/api.php/2619421814940190/search/Captain_America')
    Thanos = get_data_superheros('https://superheroapi.com/api.php/2619421814940190/search/Thanos')
    hero_dict = {**Hulk, **Captain_America, **Thanos}
    intelligence_hero = max(hero_dict, key=hero_dict.get)
    print(f'Самый умный герой: {intelligence_hero}')


if __name__ == '__main__':
    get_intelligence()



