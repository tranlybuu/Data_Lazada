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
    # Thương hiệu sản phẩm
    p_brand = scrapy.Field()
    # Giá sản phẩm
    p_price = scrapy.Field()
    # Đánh giá sản phẩm
    p_rating = scrapy.Field()
    # Số lượng đánh giá cho sản phẩm
    p_number_reviews = scrapy.Field()
    # Ảnh sản phẩm
    p_image = scrapy.Field()
    # Tên nhà bán hàng
    s_name = scrapy.Field()
    # Tỉ lệ đánh giá tốt cho nhà bán hàng
    s_rating = scrapy.Field()
    # Tỉ lệ nhà bán hàng giao hàng đúng hạn
    s_ship_ontime = scrapy.Field()
    # Tỉ lệ nhà bán hàng trả lời tin nhắn
    s_response_rate = scrapy.Field()

    # Số lượng sao đánh giá cho sản phẩm từ 1->5 sao
    p_rate5star = scrapy.Field()
    p_rate4star = scrapy.Field()
    p_rate3star = scrapy.Field()
    p_rate2star = scrapy.Field()
    p_rate1star = scrapy.Field()