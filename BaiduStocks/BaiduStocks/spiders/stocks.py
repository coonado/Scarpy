import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stock_list.html']

    def parse(self, response):
    	# 循环获取列表中a标签的链接信息
        for href in response.css('a::attr(href)').extract():
            try:
            	# 通过正则表达式获取链接中想要的信息
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                # 生成百度股票对应的链接信息
                url = 'http://gu.qq.com/' + stock + '/gp'
                # yield是生成器
                #将新的URL重新提交到scrapy框架
                # callback给出了处理这个响应的处理函数为parse_stock
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

       # 定义如何存百度的单个页面中提取信息的方法
    def parse_stock(self, response):
    	# 因为每个页面返回 的是一个字典类型，所以定义一个空字典
        infoDict = {}
        stockName = response.css('.title_bg')
        stockInfo = response.css('.col-2.fr')
        name = stockName.css('.col-1-1').extract()[0]
        code = stockName.css('.col-1-2').extract()[0]
        info = stockInfo.css('li').extract()
        # 将提取的信息保存到字典中
        for i in info[:13]:
            key = re.findall('>.*?<', i)[1][1:-1]
            key = key.replace('\u2003', '')
            key = key.replace('\xa0', '')
            try:
                val = re.findall('>.*?<', i)[3][1:-1]
            except:
                val = '--'
            infoDict[key] = val

            # 对股票的名称进行更新
        infoDict.update({'股票名称': re.findall('\>.*\<', name)[0][1:-1] + \
        							re.findall('\>.*\<', code)[0][1:-1]})
        yield infoDict