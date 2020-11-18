import requests
from lxml import etree
import json

url = 'https://blog.csdn.net/qq_42685969/article/details/82085067'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
p_list = tree.xpath('//div[@id="content_views"]/p')
fp = open('python笔试题.txt', 'w', encoding='utf-8')
all_list = []
for p in p_list:
    content = p.xpath(''+'.//text()')[0]+'\n'
    fp.write(content)

fp.close()