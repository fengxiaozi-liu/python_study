# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BeautifulgirlPipeline:
    fp = None

    def open_spider(self, spider):
        print('开始爬取校花的名字......')
        self.fp = open('xiaohua_name.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        name = item['name']
        self.fp.write(name+'\n')
        return item

    def close_spider(self, spider):
        print('爬取结束')
        self.fp.close()
