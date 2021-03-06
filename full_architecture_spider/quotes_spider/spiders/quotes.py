# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        # define itemloader
       	l = ItemLoader(item =QuotesSpiderItem(), reponser = response) # callback function

        h1_tag = response.xpath('.//h1/a/text()').extract_first()
        tags = response.xpath('.//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()