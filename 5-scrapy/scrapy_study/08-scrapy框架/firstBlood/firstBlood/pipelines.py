# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class FirstbloodPipeline:
    # 专门用来处理item类型的对象的
    # 该方法可以接收到爬虫文件提交过来的item对象
    # 该方法每接收一个item就会调用一次
    fp = None

    def open_spider(self, spider):
        """
        重写父类的方法，该方法只在爬虫开始的时候调用一次
        :param spider:
        :return:
        """
        print('开始爬虫')
        self.fp = open('qiushi.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content + '\n')
        # return item之后传递给下一个即将被执行的管道类
        return item

    def close_spider(self, spider):
        """
        在爬虫结束的时候只调用一次
        :param spider:
        :return:
        """
        print('结束爬虫')
        self.fp.close()


# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class MysqlPipeLine:
    coon = None
    cursor = None

    def open_spider(self, spider):
        self.coon = pymysql.Connect(host='localhost', port=3306, user='liu', password='lh284259',
                                    db='scrapy_study',
                                    charset='utf8')
        self.cursor = self.coon.cursor(pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        try:
            self.cursor.execute('insert into qiushi(author, content) values(%s,%s) ', [author, content])
            self.coon.commit()
        except Exception as e:
            print(e)
            self.coon.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.coon.close()
