"""
bs4解析：
    是我们python特有的数据解析
    进行数据解析的原理是进行标签的定位
    然后提取标签和标签属性中存储的数据
bs4实现数据解析得到原理
    实例化一个beautifulfsoup对象，并且将页面源码数据加载到该对象中
    通过调用beautifulsoup对象中相关的属性或者方法进行标签定位和数据解析
如何实例化BeautifulSoup对象
    soup = BeautifulSoup(page_text, 'lxml')
提供用于解析对象中的属性和和方法
soup.tagName 返回第一次出现的标签
soup.find('tagName') 等同于soup.tagName
soup.find('tagName', class_='属性名称') 用于定位到特定名称的标签
soup.find_all('tagName') 返回一个列表，里面包含符合条件的所有内容
soup.select('.class/#id') 返回的是一个列表，参数是某种选择器，符合条件的会保存在列表中
soup.select('. class > ul > li > a) 参数也可以是层级选择器，返回的是包含所有符合条件的列表
soup.select('. class > ul  a) 参数也可以是层级选择器，返回的是包含所有符合条件的列表， 空格是多个层级，>是一个层级
获取标签之间的文本信息：
    soup.a.text/string/get_text()
    text/get_text() 可以获得标签中所有的文本的内容，不是直系的也可以获取
    string 只可以获得该标签下直系的文本内容
获取标签中的属性：
    soup.tagName['属性名称']
"""
import requests
from bs4 import BeautifulSoup

fp = open('../01-requests模块的学习/爬虫数据/武沛齐.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.a)  # soup.tag_name 返回的是第一次出现的标签
# print(soup.find('div')) # find()函数的第一种用法
# print(soup.find('div', class_='vrwrap'))  # 可以进行属性定位
print(soup.a.text)
# print(soup.a.string)
# print(soup.a.get_text())
print(soup.select('.vrwrap > .vrTitle a'))
print(soup.select('.vrwrap > .vrTitle a')[0]['href'])
print(soup.select('.vrwrap > .vrTitle a')[0].get_text())
