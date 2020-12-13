"""
需求：
    解析出所有城市的名称
"""
import requests
from lxml import etree
import os
import json

if not os.path.exists('城市'):
    os.mkdir('城市')
url = 'https://www.aqistudy.cn/historydata/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
all_city_a = tree.xpath('//div[@class="hot"]//div/ul/li/a | \
//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a')
all_city_list = []
for a in all_city_a:
    city_name = a.xpath('./text()')[0]
    all_city_list.append(city_name)
json.dump(all_city_list, open('城市/'+'all_city.json', 'w', encoding='utf-8'), ensure_ascii=False)