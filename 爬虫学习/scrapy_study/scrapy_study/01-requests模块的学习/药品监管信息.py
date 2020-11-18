import requests
import json

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
all_list = []
for i in range(1,51):
    params = {
        'on': ' true',
        'page': i,
        'pageSize': ' 15',
        'productName': '',
        'conditionType': ' 1',
        'applyname': '',

    }
    page_text = requests.post(url=url, data=params, headers=headers).json()
    json.dump(page_text, open('爬虫数据/药品监管.json', 'w', encoding='utf-8'), ensure_ascii=False)
    list1 = page_text['list']
    id_list = []
    for every in list1:
        id_list.append(every['ID'])
    temp_list = []
    for every in id_list:
        param2 = {
            'id': every
        }
        response = requests.post(url=url2, data=param2, headers=headers).json()
        temp_list.append(response)
    all_list.extend(temp_list)
    print(f'到第{i}个了，别急')
json.dump(all_list, open('爬虫数据/药品监管详细信息.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('爬取结束')
