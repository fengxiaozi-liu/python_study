"""
需求：
    爬取糗事百科的图片
用正则表达式进行解析迭代案列
步骤：
    先爬取整张页面的数据，然后再获取指定标签的数据，实现聚焦爬虫
"""
import requests, re, os

if not os.path.exists('糗图'):
    os.mkdir('糗图')
for i in range(1, 3):
    if i == 1:
        url = 'https://www.qiushibaike.com/imgrank/'
    url = 'https://www.qiushibaike.com/imgrank/page/' + str(i)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    page_text = requests.get(url=url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_list = re.findall(ex, page_text, re.S)
    for img in img_list:
        url = 'https:' + img
        response = requests.get(url=url).content
        img_name = img.split('/')[-1]
        img_path = '糗图/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(response)

print('爬取结束')
