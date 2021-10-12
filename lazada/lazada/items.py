# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LazadaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Tên sản phẩm
    p_name = scrapy.Field()
    # Danh mục sản phẩm
    p_cate = scrapy.Field()
    # Giá sản phẩm
    p_price = scrapy.Field()
    # Đánh giá sản phẩm
    p_rating = scrapy.Field()
    # Tên nhà bán hàng
    s_name = scrapy.Field()
    # Đánh giá nhà bán hàng
    s_rating = scrapy.Field()
    pass