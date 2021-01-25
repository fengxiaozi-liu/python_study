"""
爬取电影的数据

"""
import json

import requests

# 指定url
url = 'https://movie.douban.com/j/chart/top_list'
# ua伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
param = {
    'type': '15',
    'interval_id': '100:90',
    'action': '',
    'start': '1',  # 从库中的第几部去取
    'limit': '20'   # 一次请求取出的个数
}
# 获取数据
response = requests.post(url=url, data=param, headers=headers)
json.dump(response.json(), open('爬虫数据/喜剧.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('爬取结束')
