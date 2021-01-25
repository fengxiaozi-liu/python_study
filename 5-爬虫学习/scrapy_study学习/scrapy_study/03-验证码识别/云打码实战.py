import requests
from lxml import etree
from yundama import base64_api
import os

if not os.path.exists('验证码图片'):
    os.mkdir('验证码图片')

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
img_url = tree.xpath('//img[@id="imgCode"]/@src')[0]
img_url = 'https://so.gushiwen.cn' + img_url
img_name = '验证码.gif'
img = requests.get(url=img_url, headers=headers).content
with open('验证码图片/' + img_name, 'wb') as fp:
    fp.write(img)
img_path = '验证码图片/' + img_name
result = base64_api('fengxiaozi', 'lh284259', img_path)
print(result)
