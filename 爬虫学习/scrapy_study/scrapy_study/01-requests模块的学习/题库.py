import requests
from lxml import etree
from selenium import webdriver

bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('http://www.xiangpi.com/chuti/zsd')
x = bro.find_element_by_xpath('/html/body/div[3]/div/ul/li[2]/a').click()

