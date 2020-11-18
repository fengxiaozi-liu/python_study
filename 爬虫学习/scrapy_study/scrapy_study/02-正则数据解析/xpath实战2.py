import requests
from lxml import etree
import os

if not os.path.exists('beautiful_girl'):
    os.mkdir('beautiful_girl')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
for i in range(1, 21):
    if i == 1:
        url = 'http://pic.netbian.com/4kmeinv/'
    url = 'http://pic.netbian.com/4kmeinv/index_%s.html' % i
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        img_src = li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0].encode('iso-8859-1').decode('gbk') + '.jpg'
        img_url = 'http://pic.netbian.com' + img_src
        img = requests.get(url=img_url, headers=headers).content
        with open('beautiful_girl/' + img_name, 'wb') as fp:
            fp.write(img)
        print('美女已就绪')
    print('一页的美女已就绪')
print('所有的美女已就绪，请于庆崇指示')
