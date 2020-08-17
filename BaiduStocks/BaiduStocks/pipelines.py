# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class BaidustocksInfoPipeline(object):
    def process_item(self, item, spider):
        return item

class BaidustocksInfoPipeline(object):
	# 当爬虫被调用时
    def open_spider(self, spider):
        self.f = open('gupiao.txt', 'w')

        # 当爬虫关闭时
    def close_spider(self, spider):
        self.f.close()

        # 对每一个item处理时
    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line) 
        except:
            pass
        return item