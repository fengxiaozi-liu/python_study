"""
问题：selenium与爬虫有什么样的关系？
    作用：
        1.便捷获取网站中动态加载的数据
        2.便捷的实现模拟登录
什么是selenium：
    基于浏览器自动化的一个模块。让浏览器自己操作
selenium的使用流程：
    -环境的配置 pip install selenium
    -下载一个浏览器的驱动程序：基于谷歌浏览器的驱动程序
        路径：http://chromdriver.storage.googleapis.com/index.html
    实例化一个浏览器对象那个，一定要传入对应的浏览器对象
"""
from selenium import webdriver
from lxml import etree
import time

# 实例化一个浏览器对象，一定要传入浏览器的驱动程序
driver = webdriver.Firefox(executable_path='./geckodriver.exe')
# 让浏览器向指定的url发请求
driver.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取当前页面动态加载出来的数据
page_text = driver.page_source
# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

time.sleep(2)

driver.quit()
