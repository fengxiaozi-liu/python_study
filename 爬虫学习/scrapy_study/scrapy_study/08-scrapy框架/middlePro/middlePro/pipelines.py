# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MiddleproPipeline:
    fp = None

    def open_spider(self, spider):
        self.fp = open('网易新闻.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(item)

    def close_spider(self, spider):
        self.fp.close()
