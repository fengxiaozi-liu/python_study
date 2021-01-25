import scrapy
from imgPro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # 在爬虫中遇到了图片软加载，一定要使用伪属性
            src = div.xpath('./div/a/img/@src2').extract_first()
            item = ImgproItem()
            item['img_url'] = src
            # yield的作用是根据返回类型的不同，引擎会处理不同的方式，如果返回的是Request类型，会交给下载器再一次向互联网发请求
            # 如果是scrapy.Item类型，会交给指定的管道类进行处理
            yield item
