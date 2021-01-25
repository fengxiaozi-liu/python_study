"""
selenium的其他操作：
    -发起请求： get(url)
    -标签定位： find系列的方法
    -标签交互:  send_keys('xxx')
    -执行js程序： execute_script('js_code')
    -前进，后退  back(), forward()
    -关闭浏览器  quit()

selenium处理iframe
     iframe 可以实现网页的嵌套
     如果定位的标签存在于iframe中，则必须使用switch_to.frames(id) 进行定位
     如果定位的标签是存在iframe标签中的，必须通过switch_to 来调用相关的iframe实现

动作链：
    要触发一系列连续的动作就要使用动作链
    动作量的导入 from selenium.webdriver import ActionChains
    实例化一个动作链的对象：action = ActionChains(bro)
    长按和点击：          action.click_and_hold(div)
    进行拖动：move_by_offset(x,y).perform 让动作链立即执行
    释放动作链对象： action.release
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

bro = webdriver.Firefox(executable_path='geckodriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')  # 相当于把定位标签的作用域做了一个指定
div = bro.find_element_by_id('draggable')

# 动作链：要触发一系列连续的动作

action = ActionChains(bro)  # 实例化一个动作量
action.click_and_hold(div)  # 点击长按指定的div

for i in range(5):
    # move_by_offset(17, 0)有两个参数表示(x,y)
    action.move_by_offset(17, 0).perform()  # perform 表示立即执行
    time.sleep(0.3)

action.release()
bro.quit()




















