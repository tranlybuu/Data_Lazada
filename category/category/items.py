# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # Danh mục sản phẩm
    cate1 = scrapy.Field()
    cate2 = scrapy.Field()
