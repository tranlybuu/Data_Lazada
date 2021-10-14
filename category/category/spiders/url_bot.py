import scrapy
from ..items import CategoryItem

class UrlBotSpider(scrapy.Spider):
    name = 'url_bot'
    allowed_domains = ['lazada.vn']
    start_urls = ['http://lazada.vn/']

    def parse(self, response):
        
        # Lấy tất cả đường dẫn url danh mục sản phẩm
        cate = response.xpath('//li[@class="lzd-site-menu-sub-item"]/a').getall()



        item = CategoryItem()
        item["cate"] = cate
        yield item
