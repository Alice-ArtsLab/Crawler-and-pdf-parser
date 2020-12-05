import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class permusi(scrapy.Spider):
    name = 'permusi'
    start_urls = ["https://periodicos.ufmg.br/index.php/permusi/"]

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"obj")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        dl = response.xpath('//a[contains(@class,"download")]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()

