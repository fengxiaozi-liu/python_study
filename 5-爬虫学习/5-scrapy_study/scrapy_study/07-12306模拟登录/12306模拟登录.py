"""
12306模拟登录
    超级鹰验证码
用selenium打开页面
对登录页面进行截图
在对登录验证图片部分进行部分截图
然后通过动作链来实现登录
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
from chaojiying import get_coordinate, get_coordinate_list
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.options import Options

# firefox_options = Options()
# firefox_options.add_argument('--headless')
# firefox_options.add_argument('--disable-gpu')
#
option = FirefoxOptions()
option.set_preference('excludeSwitches', 'enable-automation')
bro = webdriver.Firefox(executable_path='./geckodriver.exe', options=option)
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
bro.find_element_by_link_text('扫码登录').click()
bro.find_element_by_link_text('账号登录').click()
bro.find_element_by_id('J-userName').send_keys('18340087898')
bro.find_element_by_id('J-password').send_keys('lh284259')

action = ActionChains(bro)


# 将页面进行全局截图并且保存
def confirm_img():
    bro.save_screenshot('全局页面.png')

    # 获取img标签
    code_img_ele = bro.find_element_by_xpath('//img[@id="J-loginImg"]')
    # 获取验证码的左上角坐标
    location = code_img_ele.location
    # 验证码标签对应的长和宽
    size = code_img_ele.size
    x = int(location['x']) + 220
    y = int(location['y']) + 70
    x2 = int(location['x']) + size['width'] + 300
    y2 = int(location['y']) + size['height'] + 120
    rangle = (x, y, x2, y2)

    # 实例化一个Image对象
    i = Image.open('全局页面.png')
    code_img_name = '验证码.png'
    # crop根据指定区域进行图片的裁剪
    frame = i.crop(rangle)
    # 进行保存裁剪的图片
    frame.save(code_img_name)
    # 获得相关的坐标
    coordinates = get_coordinate('验证码.png')
    print(coordinates)

    # 将得到的所有的图片坐标放入的一个列表中
    coordinate_list = get_coordinate_list(coordinates)
    # 遍历列表中的所有元素，使用动作链进行一系列操作
    for every in coordinate_list:
        x, y = every[0], every[1]
        action.move_to_element_with_offset(code_img_ele, x, y).click().perform()
        time.sleep(0.5)


confirm_img()
bro.find_element_by_id('J-login').click()
action.move_by_offset(300, 0)
bro.quit()
