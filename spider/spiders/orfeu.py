import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class orfeu(scrapy.Spider):
    name = 'orfeu'
    start_urls = ["http://www.revistas.udesc.br/index.php/orfeu/issue/archive"]

    def parse(self, response):
        for link in response.xpath('//h4/a/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        for link in response.xpath('//div[contains(@id,"iss")]/a/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse3)

    def parse3(self, response):
        for link in response.xpath('//a[contains(@class,"file")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse4)

    def parse4(self, response):
        for link in response.xpath('//div/a[contains(@class,"action")]/@href').extract():
            loader = ItemLoader(item=SpiderItem(), selector=link)
            urlabsoluta = response.urljoin(link)
            loader.add_value('file_urls', urlabsoluta)
            yield loader.load_item()

