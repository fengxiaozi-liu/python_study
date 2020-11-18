"""
需求：
    爬取站长素材中免费的简历模板
"""
import requests
from lxml import etree
import os

if not os.path.exists('简历模板'):
    os.mkdir('简历模板')

url = 'http://aspx.sc.chinaz.com/query.aspx?keyword=免费&classID=864'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
model_a_list = tree.xpath('//div[@id="main"]/div/div/a')
for a in model_a_list:
    model_url = a.xpath('./@href')[0]
    model_name = a.xpath('./img/@alt')[0] + '.rar'
    model_page_text = requests.get(url=model_url, headers=headers).text
    model_tree = etree.HTML(model_page_text)
    download_url = model_tree.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
    print(download_url)
    response = requests.get(url=download_url, headers=headers).content
    with open('简历模板/' + model_name, 'wb') as fp:
        fp.write(response)

print('爬取结束')

