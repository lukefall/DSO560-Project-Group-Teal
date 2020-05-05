import scrapy
from ..items import ClothingDescriptionsItem
import time
class FarfetchSpider(scrapy.Spider):
    name = 'farfetchlinks'
    page_num = 2
    start_urls = [
        'https://www.farfetch.com/ca/shopping/women/clothing-1/items.aspx?view=180'
    ]

    def parse(self, response):
        items = ClothingDescriptionsItem()

        clothing_instances = response.css("li._c29d78._d85b45")
        for item in clothing_instances:
            link = item.css('a::attr(href)').extract_first()
            #name = item.css('p._d85b45::text').extract()
            #items['name'] = name
            items['link'] = link
            yield items

        next_page = f'https://www.farfetch.com/ca/shopping/women/clothing-1/items.aspx?page={str(FarfetchSpider.page_num)}&view=180'
        #time.sleep(30)
        if FarfetchSpider.page_num <= 504:
            FarfetchSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)