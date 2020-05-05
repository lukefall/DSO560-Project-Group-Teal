import scrapy
from ..items import ClothingDescriptionsItem
class SsenseLSpider(scrapy.Spider):
    name = 'ssenselinks'
    page_num = 2
    start_urls = [
        'https://www.ssense.com/en-ca/women'
    ]

    def parse(self, response):
        items = ClothingDescriptionsItem()

        clothing_instances = response.css("div.browsing-product-list")
        for item in clothing_instances:
            link = item.css('a::attr(href)').extract_first()
            items['link'] = link
            yield items

        next_page = f'https://www.ssense.com/en-ca/women?page={str(FarfetchSpider.page_num)}'
        if FarfetchSpider.page_num <= 306:
            FarfetchSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)