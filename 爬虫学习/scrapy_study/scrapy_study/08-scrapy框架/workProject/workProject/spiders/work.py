import scrapy
from workProject.items import WorkprojectItem

"""
boss直聘这个网站巨他妈牛逼，以我现在的知识解决不了，等一会的
"""


class WorkSpider(scrapy.Spider):
    name = 'work'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=2']

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[3]/div/div[2]/ul/li')
        print(li_list)
        for li in li_list:
            job_name = li.xpath('./div[@class="job-primary"]//a/text()').extract_first()
            print(job_name)
