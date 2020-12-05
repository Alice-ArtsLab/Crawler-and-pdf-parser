import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class revistamusica(scrapy.Spider):
    name = 'revistamusica'
    start_urls = ["https://www.revistas.usp.br/revistamusica/issue/archive",
                "https://www.revistas.usp.br/revistamusica/issue/archive/2"]

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"tit")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        for link in response.xpath('//a[contains(@class,"cover")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse3)

    def parse3(self, response):
        for link in response.xpath('//a[contains(@class,"obj")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse4)

    def parse4(self, response):
        dl = response.xpath('//a[contains(@class,"download")]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()
