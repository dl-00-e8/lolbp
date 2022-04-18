#!python3
#-*- coding : utf-8 -*-

__version__ = '2022-04-18'

import requests

champion = []

# get Json File
datas = requests.get('https://ddragon.leagueoflegends.com/cdn/12.6.1/data/ko_KR/champion.json')
datas = datas.json()

# champion Name parsing
for data in datas["data"]:
    champion.append(data)


for champ in champion:
    save_path = "D:\Web\lol_banpick\championImage\ " + champ + ".png"
    image_url = "http://ddragon.leagueoflegends.com/cdn/12.7.1/img/champion/" + champ + ".png"

    download_image = requests.get(image_url)

    with open(save_path, 'wb') as file:
        file.write(download_image.content)


# champion Image URL = "http://ddragon.leagueoflegends.com/cdn/12.5.1/img/champion/"
# champion Name JSON = "https://ddragon.leagueoflegends.com/cdn/12.6.1/data/ko_KR/champion.json"
