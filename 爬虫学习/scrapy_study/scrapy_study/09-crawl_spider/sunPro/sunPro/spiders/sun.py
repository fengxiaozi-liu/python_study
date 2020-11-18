import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
需求：
    爬取小姐威客网上的 信息分类 和信息标题 详情内容
分析：
    爬取的数据没有在同一张页面上如何进行请求传参
    -链接提取器可以提取相关的页面
    -用链接提取器提取所有的详情页链接
"""


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.shuaisf.vip/xxk_list.asp?&typeid=&areaid=68']
    # 链接提取器对象
    link = LinkExtractor(allow=r'\?page=\d+&typeid=&areaid=68')
    link_detail = LinkExtractor(allow=r'ShowInfo\.asp\?id=\d+')
    rules = (
        # 规则解析器：将链接提取器提取的链接进行指定规则的解析
        # LinkExtractor 链接提取器
        # callback 对应的是一个解析方法
        # follow=True:可以将链接提取器 继续作用到 连接提取器提取到的链接 所对应的页面中
        # 链接提取器提取到指定的url后会进行请求的封装再交给过滤器进行指纹去重
        Rule(link, callback='parse_item', follow=False),
        Rule(link_detail, callback='detail')
    )

    def parse_item(self, response):
        # xpath 解析不到tbody
        tr_list = response.xpath('/html/body/div[3]/div/div[8]/div[2]/div[2]/div//tr')
        for tr in tr_list:
            news_kind = tr.xpath('./td[1]//text()').extract_first()
            news_title = tr.xpath('./td[3]/a/strong//text()').extract_first()
            print(news_kind, news_title)

    # 解析详情页的内容
    def detail(self, response):
        news_content_list = response.xpath('/html/body/div[3]/div/div[9]/div/div[1]/div[1]/table//tr//text()').extract()
        news_content = ''.join(news_content_list)
        print(news_content)
