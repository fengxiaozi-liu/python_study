import scrapy
from selenium import webdriver
from middlePro.items import MiddleproItem
from selenium.webdriver.firefox.options import Options
# 实现反反爬的方法
from selenium.webdriver import FirefoxOptions


class MiddleSpider(scrapy.Spider):
    """
    爬取百度
    对请求进行拦截进行ua伪装和代理ip

    爬取网易新闻（新闻中标题和内容）
    在首页中解析出五大板块的url(不是动态加载的)
    每一个板块对应的新闻标题都是动态加载出来的
    通过解析出每一条新闻详情页的url获取详情信息（标题和内容）
    对响应数据进行篡改
    """
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://www.baidu.com/s?wd=ip']
    start_urls = ['https://news.163.com/']

    model_url_list = []

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        option = FirefoxOptions()
        option.set_preference('excludeSwitches', ['enable-automation'])
        self.bro = webdriver.Firefox(executable_path='geckodriver.exe', firefox_options=firefox_options, options=option)

    # 解析五大板块对应的详情页
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        a_list = [4, 5, 6, 7, 8, 9]
        for index in a_list:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_url_list.append(model_url)

        # 依次对每一个板块对应的页面进行请求
        for url in self.model_url_list:
            yield scrapy.Request(url, callback=self.parse_model)

    # 板块的内容是动态加载出来的
    def parse_model(self, response):
        div_list = response.xpath('//div[@class="newsdata_wrap"]/ul/li/div/div')
        print(div_list)
        for div in div_list:
            div_title = div.xpath('./div/div/h3/a/text()').extract_first()
            div_detail_url = div.xpath('./div/div/h3/a/@href').extract_first()
            item = MiddleproItem()
            item['title'] = div_title
            yield scrapy.Request(url=div_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        content = response.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p//text()').extract()[0]
        item = response.meta['item']
        item['content'] = content
        yield item
