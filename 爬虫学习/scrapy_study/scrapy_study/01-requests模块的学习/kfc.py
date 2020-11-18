import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
value = input('请输入你想要查询的内容')

params = {
    'op': 'keyword',
    'cname': '',
    'pid': '',
    'keyword': value,
    'pageIndex': '1',
    'pageSize': '10',
}
response = requests.post(url=url, data=params, headers=headers)
page_text = response.text
with open(value + '.json', 'w', encoding='utf-8') as fp:
    json.dump(page_text, fp, ensure_ascii=False)

print('爬取结束')
