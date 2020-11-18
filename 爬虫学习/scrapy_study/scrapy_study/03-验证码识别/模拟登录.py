"""
需求：
    模拟登录，爬取某些用户的信息
对人人网进行模拟登录：
    点击登录按钮会发送post请求，post请求中携带相关的登录信息的参数
"""
import requests
from yundama import base64_api
from lxml import etree

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
session = requests.Session()
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
params = {
    '__VIEWSTATE': 'vtX3UO4hTANCg9rOK/HxM1HVOQ8\
    KDH2od6IFaaVrluCNneRlPlRHjIT0xcYoQwGMvOMc7I0REGjakDvdd5m6a/tlH3zatLIGZpm6Fxf0zC/TNpGKuWcj5fm2SOY=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'email': '1969397913@qq.com',
    'pwd': 'lh284259',
    'code': result,
    'denglu': '登录',
}
response = session.post(url=post_url, headers=headers, data=params)
print(response.status_code)
# 手动处理cookie，从网站上查看cookie值，放在请求头中
# headers = {
#     'Cookie' : 'xxx'
# }
"""
自动处理cookie
   cookie值的来源？cookie是在发送post请求的时候服务端创建的
   需要session会话对象，作用:在请求中出现了cookie，将cookie保存到session对象中
   使用session对象模拟登录post请求发送数据，在使用session发送get请求
"""
detail_url = 'https://so.gushiwen.cn/user/collect.aspx'
detail_page_text = session.get(url=detail_url, headers=headers).text
print(detail_page_text)
detail_tree = etree.HTML(detail_page_text)
a_text = detail_tree.xpath('//div[@class="searchleft"]/a')
print(a_text)
