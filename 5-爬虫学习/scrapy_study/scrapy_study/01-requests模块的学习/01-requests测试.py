"""
爬虫任务：
    爬去搜狗首页的页面数据
"""
import requests

# 第一步：指定url, 以字符串的形式进行指定

url = 'https://www.baidu.com/'

# 第二步：发起请求，用request模块的get方法，发起get请求

requests.get(url=url)  # 根据指定的url发起请求

# 第三步：得到一个相应对象
response = requests.get(url=url)

# 第四步：获取响应数据,会拿到字符串的响应数据
page_text = response.text
with open('爬虫数据/baidu.html', 'w', encoding='utf8') as fp:
    fp.write(page_text)

print('ok')
