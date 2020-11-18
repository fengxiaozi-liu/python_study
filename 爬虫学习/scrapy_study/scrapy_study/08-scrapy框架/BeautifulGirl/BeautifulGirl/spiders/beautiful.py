import scrapy
from BeautifulGirl.items import BeautifulgirlItem


class BeautifulSpider(scrapy.Spider):
    name = 'beautiful'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.daxues.cn/xiaohua/ziliao/']
    url = 'https://news.daxues.cn/xiaohua/ziliao/index_%s.html'
    num = 2

    def parse(self, response):
        dl_a_list = response.xpath('//div[@class="xh_list"]/dl/dt/a')
        for a in dl_a_list:
            name = a.xpath('./text()').extract_first()
            item = BeautifulgirlItem()
            item['name'] = name
            yield item
        if self.num <= 3:
            new_url = self.url % self.num
            self.num += 1
            # callback回调函数用来进行数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)

