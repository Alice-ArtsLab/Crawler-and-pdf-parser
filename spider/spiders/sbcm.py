import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class sbcm(scrapy.Spider):
    name = 'sbcm'
    start_urls = ["http://compmus.ime.usp.br/sbcm/"]

    def parse(self, response):
        for link in response.xpath('//following::li/a[3]/@href').extract():
            loader = ItemLoader(item=SpiderItem(), selector=link)
            urlabsoluta = response.urljoin(link)
            loader.add_value('file_urls', urlabsoluta)
            yield loader.load_item()

