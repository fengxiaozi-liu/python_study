import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fbsPro.items import FbsproItem, DetailItem
from scrapy_redis.spiders import RedisCrawlSpider


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'sun'
    link = LinkExtractor(allow=r'\?page=\d+&typeid=&areaid=68')
    link_detail = LinkExtractor(allow=r'ShowInfo\.asp\?id=\d+')
    rules = (
        Rule(link, callback='parse_item', follow=False),
        Rule(link_detail, callback='detail')
    )

    def parse_item(self, response):
        tr_list = response.xpath('/html/body/div[3]/div/div[8]/div[2]/div[2]/div//tr')
        for tr in tr_list:
            news_kind = tr.xpath('./td[1]//text()').extract_first()
            news_title = tr.xpath('./td[3]/a/strong//text()').extract_first()
            item = FbsproItem()
            print(news_kind, news_title)
            item['news_kind'] = news_kind
            item['news_title'] = news_title
            yield item

    def detail(self, response):
        news_content_list = response.xpath('/html/body/div[3]/div/div[9]/div/div[1]/div[1]/table//tr//text()').extract()
        news_content = ''.join(news_content_list)
        item = DetailItem()
        item['news_content'] = news_content
        print(news_content)
        yield item
