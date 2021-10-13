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
    # Sản phẩm chính hãng
    p_mall = scrapy.Field()
    # Danh mục sản phẩm
    p_cate = scrapy.Field()
    # Giá sản phẩm
    p_price = scrapy.Field()
    # Đánh giá sản phẩm
    p_rating = scrapy.Field()
    # Số lượng đánh giá cho sản phẩm
    p_number_reviews =  scrapy.Field()
    # Tên nhà bán hàng
    s_name = scrapy.Field()
    # Tỉ lệ đánh giá tốt cho nhà bán hàng
    s_rating = scrapy.Field()
    # Tỉ lệ nhà bán hàng giao hàng đúng hạn
    s_ship_ontime = scrapy.Field()
    # Tỉ lệ nhà bán hàng trả lời tin nhắn
    s_response_rate = scrapy.Field()

    # Số lượng sao đánh giá cho sản phẩm từ 1->5 sao
    p_5star_rating = scrapy.Field()
    p_4star_rating = scrapy.Field()
    p_3star_rating = scrapy.Field()
    p_2star_rating = scrapy.Field()
    p_1star_rating = scrapy.Field()