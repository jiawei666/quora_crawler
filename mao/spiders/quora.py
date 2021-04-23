import scrapy


class QuoraSpider(scrapy.Spider):
    name = 'quora'
    allowed_domains = ['www.quora.com']
    start_urls = ['https://www.quora.com/topic/Electronics']

    def start_requests(self):  # 控制爬虫发出的第一个请求
        proxy = "http://127.0.0.1:8889"
        yield scrapy.Request(self.start_urls[0], meta={"proxy": proxy})

    def parse(self, response):
        print("----------------")
        print(response.text)

        pass
