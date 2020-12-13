import json

import requests

# 指定url
post_url = 'https://fanyi.baidu.com/sug'
# post请求的处理流程

# ua伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

# 进行参数的处理
value = input('你想要翻译的内容')
data = {
    'kw': value
}
# 请求发送
response = requests.post(url=post_url, data=data, headers=headers)
# 获取响应数据
page_text = response.json()  # json方法返回的是一个字典对象，如果确认响应数据是json类型的才可以进行返回
with open(value + '.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(page_text, ensure_ascii=False))

print('翻译结束')
