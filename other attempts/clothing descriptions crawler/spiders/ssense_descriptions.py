import scrapy
from ..items import ClothingDescriptionsItem
from pymongo import MongoClient
import re

class SsenseDSpider(scrapy.Spider):
    name = 'ssensedescriptions'

    connection = MongoClient('localhost', 27017)
    db = connection.ssenselinks
    data = db.links_tb
    linklist = data.find()

    start_urls = ['https://www.farfetch.com/'+l['link'] for l in linklist]

    def parse(self, response):
        items = ClothingDescriptionsItem()

        description = response.css('.product-description-text span:nth-child(1)').extract()
        # if 'new season' in description[0].lower():
        #     description = description[1]
        # else:
        #     description = description[0]
        # description = re.sub(r'\t|\n|\'|\"', '', description)
        items['description'] = description
        yield items