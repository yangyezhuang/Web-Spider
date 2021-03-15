import requests
import json

url = 'https://quanmin.baidu.com/wise/growth/api/home/tabmorelist?rn=12&pn=2&timestamp=1603466231717&session_id=1603466228293&tab_name=funny&_format=json'

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
for i in range(1, 3):
    params = {
        'rn': '12',
        'pn': f'{i}',
        'timestamp': '1603466231717',
        'session_id': '1603466228293',
        'tab_name': 'funny',
        '_format': 'json',
    }
    r = requests.get(url=url, params=params, headers=headers)
    html = r.json()
    lis = html['data']['list']['video_list']
    for li in lis:
        play_url = li['play_url']
        title = li['title']
        filename = 'E:\python\Spider\异步视频/全民小视频/' + title + '.mp4'
        response_2 = requests.get(url=play_url, headers=headers)
        with open(filename, mode='wb') as f:
            f.write(response_2.content)
            print(title, play_url)