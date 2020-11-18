import requests
from selenium import webdriver
from lxml import etree
import os
from multiprocessing.dummy import Pool
from concurrent.futures import ProcessPoolExecutor

"""
需求：
    爬取梨视频的视频数据
线程池的使用原则：
    线程池处理的是阻塞且耗时的操作
"""
if not os.path.exists('视频'):
    os.mkdir('视频')

url = 'https://www.pearvideo.com/category_5'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(url)

page_text = driver.page_source
tree = etree.HTML(page_text)
a_list = tree.xpath('//div[@id="listvideoList"]/ul/li/div/a')
video_content = []
for a in a_list:
    video_url = 'https://www.pearvideo.com/' + a.xpath('./@href')[0]
    video_name = a.xpath('./div[@class="vervideo-title"]/text()')[0] + '.mp4'
    driver.get(video_url)
    video_page = driver.page_source
    video_content_url = etree.HTML(video_page).xpath('//video/@src')[0]
    print(video_content_url)
    temp = {'name': video_name, 'url': video_content_url}
    video_content.append(temp)


def get_video(dic):
    content_url = dic['url']
    response = requests.get(url=content_url, headers=headers).content
    with open('视频/' + dic['name'], 'wb') as fp:
        fp.write(response)


pool = Pool(4)
pool.map(get_video, video_content)

driver.quit()
