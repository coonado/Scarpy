import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    #修改为要爬取的链接
    start_urls = ['http://python123.io/ws/demo.html']

    #完善爬取方法的具体功能
    #self面向对象，类所属关系的标记
    # response从网页返回内容所存储或对应的对象
    def parse(self, response):
    	# 定义存储文件的名字
    	# 从响应的URL中提取名字作为本地的文件名
    	fname = response.url.split('/')[-1]
    	# 将返回的内容保存为本地
    	with open(fname, 'wb') as f:
    		f.write(response.body)
    	self.log('Saved file %s.' % name)

