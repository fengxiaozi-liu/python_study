"""
如何规避selenium爬取数据被阻止的风险：
    from selenium.webdriver import FirefoxOptions 实例化FirefoxOptions类实现反反爬
    option = FirefoxOptions()
    option.set_preference('excludeSwitches', ['enable-automation'])

"""
from selenium import webdriver
from time import sleep
# 实现无可视化界面的
from selenium.webdriver.firefox.options import Options
# 实现反反爬的方法
from selenium.webdriver import FirefoxOptions

# 不让他打开显示浏览器的打开过程(无头浏览器) phantomjs
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')

# 实现规避检测
option = FirefoxOptions()
option.set_preference('excludeSwitches', ['enable-automation'])

bro = webdriver.Firefox(executable_path='geckodriver.exe', firefox_options=firefox_options, options=option)
bro.get('https://www.baidu.com')
page_text = bro.page_source
print(page_text)
sleep(3)
bro.quit()
