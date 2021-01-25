import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from multiPro.items import MultiproItem
from redis import Redis


class MultiSpider(CrawlSpider):
    name = 'multi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']
    coon = Redis(host='127.0.0.1', port=6379)
    link = LinkExtractor(allow=r'/frim/index1-\d\.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            detail_url = 'http://www.4567kan.com'+li.xpath('./div/a/@href').extract_first()
            ex = self.coon.sadd('url', detail_url)
            if ex == 1:
                print('这个电影没有爬取过')
                yield scrapy.Request(detail_url, callback=self.parse_detail)
            else:
                print('数据没有更新暂无数据可以爬取')

    def parse_detail(self, response):
        title = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        introduce = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[3]/text()').extract()
        introduce = ''.join(introduce)
        item = MultiproItem()
        item['title'] = title
        item['introduce'] = introduce
        yield item
