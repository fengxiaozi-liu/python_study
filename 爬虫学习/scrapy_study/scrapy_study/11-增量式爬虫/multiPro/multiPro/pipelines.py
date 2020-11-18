# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MultiproPipeline:
    coon = None

    def open_spider(self, spider):
        self.coon = spider.coon

    def process_item(self, item, spider):
        dic = {'name': item['title'], 'desc': item['introduce']}
        print(dic)
        self.coon.lpush('movie_data', dic)
        return item
