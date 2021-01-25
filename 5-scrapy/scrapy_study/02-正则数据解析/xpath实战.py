"""
需求：
    爬取58二手房的房源信息
"""
import requests
from lxml import etree
import json
url = 'https://bj.58.com/ershoufang/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
title = tree.xpath('//div[@class="list-info"]/h2/a/text()')
family_url = tree.xpath('//div[@class="list-info"]/h2/a/@href')
family_dict = {title[i]:family_url[i] for i in range(len(title))}
fp = open('房源.json', 'w', encoding='utf-8')
json.dump(family_dict, fp, ensure_ascii=False)
