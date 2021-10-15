import scrapy
from ..items import CategoryItem

class UrlBotSpider(scrapy.Spider):
    name = 'url_bot'
    allowed_domains = ['lazada.vn']
    start_urls = ['http://lazada.vn/']

    def parse(self, response):
        
        # Lấy tất cả đường dẫn url danh mục sản phẩm
        cate1 = response.xpath('//li[@class="lzd-site-menu-sub-item"]/a').getall()
        cate2 = response.xpath('//li[@class="sub-item-remove-arrow"]/a').getall()



        item = CategoryItem()
        item["cate1"] = cate1
        item["cate2"] = cate2
        yield item
