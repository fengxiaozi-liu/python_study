"""
需求：
    模拟登录qq空间
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
bro = webdriver.Firefox(executable_path='./geckodriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
bro.find_element_by_id('switcher_plogin').click()
sleep(1)
bro.find_element_by_id('u').send_keys('1969397913')
sleep(1)
bro.find_element_by_id('p').send_keys('1969397913lh@')
sleep(1)
bro.find_element_by_id('login_button').click()
sleep(3)
bro.quit()