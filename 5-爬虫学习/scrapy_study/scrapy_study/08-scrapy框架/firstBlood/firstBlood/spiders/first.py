import scrapy
from firstBlood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称：就是爬虫源文件的一个唯一标识
    name = 'first'
    # 允许的域名: 是用来限定start_url那些url可以进行请求发送
    # allowed_domains = ['www.baidu.com']
    # 起始url列表:起始url的特征是该列表中存放的url会被scrapy自动请求的发送
    start_urls = ['https://www.qiushibaike.com']

    # parse是用来做数据解析的，对响应对象中的响应数据进行解析，parse调用的次数由start_url列表中的元素个数决定
    def parse(self, response):
        # 解析作者的名称+段子美容
        div_list = response.xpath('//div[@id="content"]/div/div[2]/div')
        writer_content_list = []
        for div in div_list:
            # xpath返回的是列表，但是列表中元素一定是Selector类型的对象
            # extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            # 列表调用了extract之后，表示将每一个selector对象中的data对应的字符串提取出来
            content = div.xpath('./a/div[@class="content"]/span//text()').extract_first()
            content = ''.join(content)
            # 实例化一个item对象
            item = FirstbloodItem()
            item['author'] = author
            item['content'] = content
            # 将item封装的数据提交给管道
            yield item
