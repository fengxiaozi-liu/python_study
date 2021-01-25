"""
无可视化界面(无头浏览器)：
    from selenium.webdriver.firefox.options import Options 实例化Options实现无可视化界面的操作
    就是让浏览器不显示打开的过程
    有Option和PhantomJs两个模块
具体操作
    firefox = Options()
    firefox.add_argument('--headless')
    firefox.add_argument('--disable-gpu')
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
# 不让他打开显示浏览器的打开过程(无头浏览器) phantomjs
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')

bro = webdriver.Firefox(executable_path='./geckodriver.exe', firefox_options=firefox_options)
bro.get('https://www.baidu.com')
page_text = bro.page_source
print(page_text)
sleep(3)
bro.quit()


