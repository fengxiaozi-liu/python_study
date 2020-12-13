import requests

"""
UA伪装：
    user_agent:这个请求头信息表示请求载体的身份标识
    ua检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器
           说明该请求时正常的请求，但是如果检测到请求的载体身份标识不是基于浏览器的，就表示它是爬虫
           这个服务器就很有可能拒绝该次请求。
    ua伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
"""

url = 'https://www.sogou.com/web'

# 处理url携带的参数：封装到字典中
value = input('输入一个关键字')
# 进行ua伪装 伪装成基于某一款浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
param = {
    'query': value
}
# 对指定的url发起请求时携带参数的，并且在请求的过程了处理了参数
response = requests.get(url=url, params=param, headers=headers)

page_text = response.text
file_name = value
with open(file_name + '.html', 'w', encoding='utf-8') as file:
    file.write(page_text)
print('数据爬取完毕')
