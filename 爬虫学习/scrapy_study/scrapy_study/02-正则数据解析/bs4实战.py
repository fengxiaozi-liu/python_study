"""
需求：
    爬取三国演义中所有的章节标题和章节内容
"""
import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('三国演义'):
    os.mkdir('三国演义')

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
menu_list = soup.select('.book-mulu > ul > li')
fp = open('三国演义/三国演义.txt', 'w', encoding='utf-8')
for li in menu_list:
    new_url = 'https://www.shicimingju.com'+li.a['href']
    title = li.a.string
    print(title)
    detail_page_text = requests.get(url=new_url, headers=headers).text
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div', class_='chapter_content')
    content = div_tag.text
    print(content)
    fp.write(title+':'+content+'\n')
    print(title, '爬取成功')
fp.close()


print('爬取结束')
